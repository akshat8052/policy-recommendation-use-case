

from langchain.chat_models import AzureChatOpenAI
import os
from langchain.schema import HumanMessage

from dotenv import load_dotenv
import os




# Make sure these are set in your environment or use os.environ[...] here
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

chat = AzureChatOpenAI(
    deployment_name=deployment_name,
    openai_api_version=api_version,
    openai_api_key=api_key,
    openai_api_base=endpoint,
    temperature=0.2
)

def call_llm(prompt: str) -> str:
    response = chat([HumanMessage(content=prompt)])
    return response.content
