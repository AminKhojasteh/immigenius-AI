

from typing import Optional
from pydantic import BaseModel, Field


class AcceptanceChanceOutputSchema(BaseModel):
    """visa acceptance chance data"""
    visa_name: str = Field(description="name of visa")
    description: str = Field(description="a short description about this visa")
    chance: int = Field(description="acceptance chance for this visa, scale 1-100")
    country: str = Field(description="visa country name")
    total_cost: str = Field(description="total cost for this visa, with local money")
    duration: str = Field(description="how long it takes to get this visa")
    processing_time: str = Field(description="processing time for this visa, how many months")
    reasons : str = Field(description="reasons for why user lost some score")
    improvements: str = Field(description="how to increase chance for this visa")


class AIresponse(BaseModel):
    visa_names : list[str] = Field(description="list of visa names plus their countries")


# input for api is like this, a json or dict with these keys
class UserInfo(BaseModel):
    full_name:Optional[str]   = Field(default="",description="full name of user") 
    age: Optional[str] = Field(default="",description="age of user") 
    nationality:Optional[str]  = Field(default="",description="user nationality ")
    savings:Optional[str]   = Field(default="",description="total savings of user")
    yearly_salary:Optional[str]  = Field(default="",description="yearly salary of user")
    education:Optional[str]  = Field(default="",description="education degree/level of user")
    language_proficiency_score:Optional[str]  = Field(default="",description="ilets or toefl or any other language test score")
    immigration_plan:Optional[str]  = Field(default="",description="immigration plan of user")
    work_experience:Optional[str]  = Field(default="",description="total years of user experience and field")
    maritial_status:Optional[str]  = Field(default="",description="single or married")
    number_of_kids:Optional[str]  = Field(default="",description="how many kids user has")
    preferred_countries : Optional[list[str]]   = Field(default=[""],description="list of countries user preferred to go,")

    
class FinalResults(BaseModel):
    user_info : UserInfo
    visas_acceptance_data : list[AcceptanceChanceOutputSchema] 
    total_used_tokens:int
    
