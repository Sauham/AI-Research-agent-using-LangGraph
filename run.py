from work import create_workflow

# Initialize compiled workflow
app = create_workflow()

# Execute with input
response = app.invoke({"query": "Explain LangGraph in simple terms"})
print("Final Answer:\n", response["draft"])