# AI Agentic Research System 🤖

A dual-agent system for deep web research and answer generation using:
- **Tavily** for web crawling
- **Hugging Face** models for local processing
- **LangGraph** for workflow management
- **Streamlit** for interactive UI

## Features ✨
- 🕸️ Web research with Tavily API
- 🤖 Dual-agent architecture (Researcher + Drafter)
- 📊 State management with LangGraph
- 🖥️ Streamlit web interface
- 🔄 Error recovery & quality checks

## Prerequisites 📋
- Python 3.8+
- [Tavily API Key](https://tavily.com/)
- 4GB+ RAM (8GB recommended)
- GPU (optional but recommended)

## Installation 🛠️

1. **Clone Repository**
```bash
git clone https://github.com/Sauham/AI-Research-agent-using-LangGraph
cd ai-research-system
Install Dependencies

bash
pip install -r requirements.txt
Configure Environment

bash
# Copy and edit .env file
cp .env.example .env
# Add your Tavily API key
nano .env  # TAVILY_API_KEY=your_key_here
Download Models (First Run Only)

bash
python -c "from transformers import AutoModel; AutoModel.from_pretrained('google/flan-t5-base')"
Usage 🚀
Command Line Interface
bash
# Run research workflow
python run.py --query "Explain quantum computing basics"

# Test system components
python test_tavily.py
Web Interface (Streamlit)
bash
streamlit run app.py
Access at: http://localhost:8501

Streamlit Interface Demo

Project Structure 📂
/research-system
├── agents/
│   ├── research_agent.py  # Web crawler & data processor
│   └── draft_agent.py     # Answer generator
├── work.py                # LangGraph workflow
├── app.py                 # Streamlit UI
├── utils/
│   └── config.py          # Environment management
├── requirements.txt
└── .env.example
Troubleshooting 🚨
Issue	Solution
Missing API Key	Verify .env file exists in root directory
Dependency Errors	Run pip install -r requirements.txt --force-reinstall
Slow Performance	Use google/flan-t5-small model instead
Model Download Failures	Set HF_HUB_ENABLE_HF_TRANSFER=1
Contributing 🤝
Fork the repository

Create your feature branch (git checkout -b feature/amazing-feature)

Commit changes (git commit -m 'Add amazing feature')

Push to branch (git push origin feature/amazing-feature)

Open Pull Request

License 📄
MIT License - See LICENSE for details