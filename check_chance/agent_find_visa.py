from langchain.agents import create_agent

from langchain_core.tools import tool
import check_chance.db as db
from check_chance.ai import smart_model

@tool
def find_visas(country:str) -> dict:
    """this tool query the vector database and find all of the visa names of given country
    available countries are these: ("Canada","Spain","UK=United Kingdom","Germany","USA,US =United States","UAE = United Arab Emirates","France","Australia","Italy","Turkey","Netherlands","Argentina","New Zealand","Portugal","Saudi Arabia","Finland","Sweden","Singapore","Denmark","Oman","Luxembourg","Iceland","Switzerland","Norway",)
    """
    metadata = db.Collection.get(where={"country":country.title()})


    return {"visa_names":metadata['documents']}


prompt = """
    you must use find_visas tool and query based on user preferred countries (use real names of countries,like [UAE = United Arab Emirates,UK = United Kingdom]),
    then based on user profile preferred immigration plan , 
    return only suitable visa for him/her but always consider Start-up visa for user
    -if uesr had no immigration plan, return study,work,start-up plans 
    -you must return top 5 visas 
    output format: 
recommended_visa = {
"visa_names": list[str]  [name of all recommended visas + their countries]
    }"""

find_visa_ai = create_agent(
    model=  smart_model,
    tools= [find_visas],
    system_prompt= prompt,
    name= "find_visa_ai",)