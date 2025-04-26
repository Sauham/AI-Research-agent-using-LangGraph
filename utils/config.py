import os
from pathlib import Path
from dotenv import load_dotenv

def load_config():
    """Force load .env from project root with validation"""
    env_path = Path(__file__).parent.parent / '.env'
    
    if not load_dotenv(dotenv_path=env_path):
        raise FileNotFoundError(f"Missing .env file at {env_path}")
    
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise ValueError("TAVILY_API_KEY not found in .env")
    
    return api_key