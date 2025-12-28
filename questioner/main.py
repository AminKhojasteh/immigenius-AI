"""
This is questioner API, just call questioner and you get fields of UserInfo, check them and if all of them where filled,
Exit the program
"""

from fastapi import FastAPI, HTTPException
import questioner.ai as ai

app = FastAPI()


# input string and thread_id to this api, string is user input, thread_id is his unique id, output is a dict with ai_response and structure_output
# ai_response is ai model response, structure_output is format user info in dict
@app.post("/invoke/questioner")
def invoke_questioner(input_data: str, thread_id: str):
    model_input ={
        "messages": [
            {
                "role": "user",
                "content":input_data
            }
        ]
    }
    try:
        result = ai.questioner.invoke(
            model_input,
            config={"configurable": {"thread_id": thread_id}}
        )
        output = {
            "ai_response" : result['structured_response'].ai_response,
            "structure_output" : result['structured_response']
        }
        return output
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Invocation failed: {str(e)}")
    





