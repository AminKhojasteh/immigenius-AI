from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
load_dotenv()
grok_api = os.getenv("XAI_API_KEY")
model = init_chat_model(model="grok-4-1-fast-non-reasoning",xai_api_key=grok_api,temperature=0,)
smart_model = init_chat_model(model="grok-4-1-fast-reasoning",xai_api_key=grok_api,temperature=0,)

