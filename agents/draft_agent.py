
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

class DraftAgent:
    def __init__(self, llm):
        self.draft_prompt = PromptTemplate(
            template="Generate a structured answer for: {query}\nContext: {summaries}",
            input_variables=["query", "summaries"]
        )
        self.chain = self.draft_prompt | llm  # Modern LangChain syntax

    def draft(self, inputs):
        return self.chain.invoke(inputs)
# class DraftAgent:
#     def __init__(self, llm):
#         self.draft_prompt = PromptTemplate(
#             template="Generate a structured answer for: {query}\nContext: {summaries}",
#             input_variables=["query", "summaries"]
#         )
#         self.chain = LLMChain(llm=llm, prompt=self.draft_prompt)

#     def draft(self, inputs):
#         return self.chain.run(query=inputs["query"], summaries=inputs["summaries"])