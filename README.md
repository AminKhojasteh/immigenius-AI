Clone this code and then use,
```
docker compose up --build
```

# this will create a image called ai-api
# and build 2 containers which named: check_chance, questioner
-------------------------------------------
## check_chance container:
this api only needs to called once, and it will return data after about 30 sec
its fastapi: 
```
Method = Post
URL = "/invoke/check-chance"
```
input must be UserInfo data model
Output is FinalResults data model, you can find it in ./check_chance/data_models.py

-------------------------------------------

## questioner container:
this api ask user about its info, so it might be called 10 times or more,
it is better to use this api with websocket,
fastapi route:
```
Method = POST
URL = "/invoke/questioner"
```
there is 2 inputs:  
1- is string and its user text input,  
2- is thread_id which is unique for each chat history and websocket  
args : input_data: str, thread_id: str  

output:
```
output = {
            "ai_response" : ai_response,
            "structure_output" : structured_ai_response
        }
```
***you must close the connection when all fields in structure_ouput are filled**
