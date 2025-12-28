import chromadb
# from openai import OpenAI
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
import os
from dotenv import load_dotenv
load_dotenv()

open_ai_api = os.getenv("OPEN_AI_API_KEY")
chroma_client = chromadb.PersistentClient('./check_chance/chroma_visa_data')

Collection = chroma_client.get_collection(name="visa_data",
                                                    embedding_function=OpenAIEmbeddingFunction(
                                                            api_key=open_ai_api,
                                                            model_name="text-embedding-3-small"))


