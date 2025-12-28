
from dotenv import load_dotenv
from langchain_xai import ChatXAI
import os
from langchain.agents.middleware import SummarizationMiddleware
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages.utils import count_tokens_approximately
from typing import Optional
from pydantic import Field
from pydantic import BaseModel
load_dotenv()


# this is Pydantic output of model, it gives output like json
class UserInfo(BaseModel):
    ai_response : str = Field(description= "output of AI")
    full_name:Optional[str]   = Field(default="",description="full name of user") 
    age: Optional[str] = Field(default="",description="age of user") 
    nationality:Optional[str]  = Field(default="",description="user nationality ")
    savings:Optional[str]   = Field(default="",description="total savings of user")
    yearly_salary:Optional[str]  = Field(default="",description="yearly salary of user")
    education:Optional[str]  = Field(default="",description="education degree/level of user")
    language_proficiency_score:Optional[str]  = Field(default="",description="ilets or toefl or any other language test score")
    immigration_plan:Optional[str]  = Field(default="no immigration plan",description="immigration plan of user")
    work_experience:Optional[str]  = Field(default="",description="total years of user experience and field")
    maritial_status:Optional[str]  = Field(default="",description="single or married")
    number_of_kids:Optional[str]  = Field(default="",description="how many kids user has")
    preferred_countries : Optional[list[str]]   = Field(default=["No preferred country"],description="list of countries user preferred to go,")


main_prompt = """you are Visa and immigration assistant named Mira and you are tasked to get these info from user,
this is needed info = (name,age,maritial status, number of kids, nationality, education degree/level , work experience)
RULES :
-aks questions one by one and be friendly with user,
-keep your questions short
-if any info was missing ask again,
-Do not answer to any other question, just answer about why you are asking information from user
"""

# must be put in .env file, api for grok 
grok_api = os.getenv("XAI_API_KEY")

chat = ChatXAI(
    xai_api_key=grok_api,
    model="grok-4-fast-non-reasoning",
)

# this node will summarize whole chat history if it exceeds 3500 token
summarization_node = SummarizationMiddleware(
    token_counter=count_tokens_approximately,
    model=chat,
    max_tokens_before_summary=3500,  # Summarize when history exceeds this

)

# save history in memory
memory = MemorySaver()
questioner = create_agent(
    model=chat,
    system_prompt= main_prompt , 
    name="Questioner",
    middleware= [summarization_node],
    checkpointer=memory,
    response_format=UserInfo,
        )

