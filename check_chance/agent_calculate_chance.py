from langchain.agents import create_agent
from langchain_core.tools import tool
import check_chance.db as db
from check_chance.ai import smart_model
from langchain.agents.structured_output import ToolStrategy
from check_chance.data_models import FinalResults

@tool
def find_visa_details(query:str) -> list:
    """this tool query the vector database and find visa eligibility criteria for given visa name,their fees and processing time
    give query like this -> (visa_name) + (country) data
    available countries are these ("Canada","Spain","United Kingdom","Germany","United States","United Arab Emirates","France","Australia","Italy","Turkey","Netherlands","Argentina","New Zealand","Portugal","Saudi Arabia","Finland","Sweden","Singapore","Denmark","Oman","Luxembourg","Iceland","Switzerland","Norway",)
    """
    print(query)
    metadata = db.Collection.query(
        query_texts=query,
        n_results=1,
    )
    try:
        output_data = f"eligibilty:{metadata['metadatas'][0]['eligibility_criteria']},\n Fees:{metadata['metadatas'][0]['fees']}\n Processing time:{metadata['metadatas'][0]['processing_times']}\n target group:{metadata['metadatas'][0]['target_group']} \n required docs: {metadata['metadatas'][0]['required_documents']}"
        
    except:
        output_data = f"eligibilty:{metadata['metadatas'][0][0]['eligibility_criteria']},\n Fees:{metadata['metadatas'][0][0]['fees']}\n Processing time:{metadata['metadatas'][0][0]['processing_times']}\n target group:{metadata['metadatas'][0][0]['target_group']}\n required docs: {metadata['metadatas'][0][0]['required_documents']}"

    return output_data



calculate_chance_agent_prompt = """
you are visa admission, your task is to calculate user acceptance chance of getting visa,
You will get UserInfo data and  list of visas, then use find_visa_details tools for each visa for this tool 
query like this: [visa name , country]
from returned data from tool, calcuate user acceptance chance for that visa, according to UserInfo and Visa detail criterias,
for example compare documents and eligibilty with UserInfo and give him score between 1-100 , 
Usually users never get 100 percent score, so maxmimum score is between 80 to 90 because you cant be sure about it
Scoring system:
- factors like Age , Language Test Score and user nationality matters a lot
- if user had any (engingeering, programming or MBA history) always give him high score for Start-up Visa 
- for missing very importnant documents decrease chance of user
then return the results in asked format.
"""

calculate_chance_ai = create_agent(
    model = smart_model,
    tools= [find_visa_details],
    system_prompt= calculate_chance_agent_prompt,
    name="calculate_visa_chance",
    response_format= FinalResults,

)