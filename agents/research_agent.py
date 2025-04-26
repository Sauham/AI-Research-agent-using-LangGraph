from tavily import TavilyClient
from utils.config import load_config
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain_huggingface import HuggingFacePipeline  # Updated import
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

class ResearcherAgent:
    def __init__(self):
        self.tavily = TavilyClient(api_key=load_config())
        
        # Initialize modern HuggingFace pipeline
        tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
        model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
        
        self.llm = HuggingFacePipeline(
            pipeline=pipeline(
                "text2text-generation",
                model=model,
                tokenizer=tokenizer,
                max_length=512
            )
        )

    def research(self, query):
        results = self.tavily.search(query=query, max_results=3)
        return {
            "query": query,
            "summaries": [
                self.llm.invoke(f"Summarize concisely: {result['content']}")
                for result in results["results"]
                if result.get("content")
            ]
        }