import streamlit as st
from work import create_workflow
from utils.config import load_config
import time

# Initialize
load_config()
workflow = create_workflow()

# UI
st.title("🔍 AI Research Agent")
query = st.text_input("Enter your research query:", "What is LangGraph?")

if st.button("Run Research"):
    with st.spinner("Researching..."):
        start_time = time.time()
        result = workflow.invoke({"query": query})
        duration = time.time() - start_time
    
    st.success(f"Research completed in {duration:.2f}s")
    st.subheader("Answer:")
    st.markdown(result["draft"])
    
    with st.expander("See research details"):
        st.json(result)