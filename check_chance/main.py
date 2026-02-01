import sys
from pydantic import BaseModel
sys.path.append("/check_chance")
from check_chance.agent_supervisor import super_agent
import json
from fastapi import FastAPI,Request,HTTPException

app = FastAPI(title="acceptance chance agent")

# input must be UserInfo
class UserInfo(BaseModel):
    full_name:str
    age: str
    nationality:str
    savings:str
    yearly_salary:str
    education:str
    language_proficiency_score:str 
    immigration_plan:str
    work_experience:str
    maritial_status:str
    number_of_kids:str
    preferred_countries : list[str]  

@app.post("/invoke/check-chance")
def invoke_questioner(req:UserInfo):
    docs = req.model_dump_json(ensure_ascii=False)
    model_input =[{"role":"human",'content':docs}]
    try:
        result = super_agent.invoke({'messages':model_input})
        output = {
            "structured_output" : result['structured_response']
        }
        return output
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Invocation failed: {str(e)}")
    



