

from langchain.chat_models import AzureChatOpenAI
import os
from langchain.schema import HumanMessage

from dotenv import load_dotenv
import os
load_dotenv()
# Make sure these are set in your environment or use os.environ[...] here



deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
print("Deployment Name:", os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"))
print("API Version:", os.getenv("AZURE_OPENAI_API_VERSION"))
print("API Key:", os.getenv("AZURE_OPENAI_API_KEY"))
print("Endpoint:", os.getenv("AZURE_OPENAI_ENDPOINT"))



# Check if all required environment variables are loaded
if not all([deployment_name, api_version, api_key, azure_endpoint]):
    raise ValueError("One or more Azure OpenAI environment variables are missing. Please check your .env file.")


chat = AzureChatOpenAI(
    azure_deployment=deployment_name,
    azure_endpoint=azure_endpoint,
    openai_api_version=api_version,
    openai_api_key=api_key,
    temperature=0.2
)

def call_llm(prompt: str) -> str:
    response = chat([HumanMessage(content=prompt)])
    return response.content
