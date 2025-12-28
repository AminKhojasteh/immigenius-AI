import sys
sys.path.append("/check_chance")
from check_chance.agent_supervisor import super_agent



import json
from fastapi import FastAPI,Request,HTTPException


app = FastAPI(title="acceptance chance agent")




# input must be UserInfo
# class UserInfo(BaseModel):
    # full_name:Optional[str]   = Field(default="",description="full name of user") 
    # age: Optional[str] = Field(default="",description="age of user") 
    # nationality:Optional[str]  = Field(default="",description="user nationality ")
    # savings:Optional[str]   = Field(default="",description="total savings of user")
    # yearly_salary:Optional[str]  = Field(default="",description="yearly salary of user")
    # education:Optional[str]  = Field(default="",description="education degree/level of user")
    # language_proficiency_score:Optional[str]  = Field(default="",description="ilets or toefl or any other language test score")
    # immigration_plan:Optional[str]  = Field(default="",description="immigration plan of user")
    # work_experience:Optional[str]  = Field(default="",description="total years of user experience and field")
    # maritial_status:Optional[str]  = Field(default="",description="single or married")
    # number_of_kids:Optional[str]  = Field(default="",description="how many kids user has")
    # preferred_countries : Optional[list[str]]   = Field(default=[""],description="list of countries user preferred to go,")
@app.post("/invoke/check-chance")
async def invoke_questioner(req:Request):
    docs = await req.json()
    model_input =[{"role":"human",'content':str(docs)}]
    try:
        result = super_agent.invoke({'messages':model_input})
        output = {
            "structure_output" : result['structured_response']
        }
        return output
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Invocation failed: {str(e)}")
    



