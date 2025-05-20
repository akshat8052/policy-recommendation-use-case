

from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage

import os

# Make sure these are set in your environment or use os.environ[...] here
deployment_name = "gpt-4o"
api_version = "2025-01-01-preview"
api_key = "AnuXnEw1fmHLzMOfSvX8RlBXw8HuMd5peMVRvwSvR5kwJWFEMQAxJQQJ99BBACHYHv6XJ3w3AAABACOGIFW3"
endpoint = "https://genaisolution04.openai.azure.com"

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
