
from langchain.agents import create_agent
from check_chance.ai import model
from langchain.agents.structured_output import ToolStrategy
from langchain_core.tools import tool
from check_chance.data_models import UserInfo,FinalResults
from check_chance.agent_calculate_chance import calculate_chance_ai
from check_chance.agent_find_visa import find_visa_ai

@tool
def find_visa_event(userinfo:UserInfo) ->str:
    """its find_visa_event tool, query UserInfo"""
    model_input = {"role":"ai",'content':str(userinfo)}
    result = find_visa_ai.invoke({'messages':[model_input]})
    return result['messages'][-1].text


@tool 
def calculate_chance_event(userinfo:UserInfo, visa_name_list:list[str]):
    """its calculate_chance_event tool, query userinfo, visa_name_list """
    model_input = [{"role":"ai",'content':str(userinfo)},{"role":"ai",'content':str(visa_name_list)}]
    
    results = calculate_chance_ai.invoke({'messages':model_input})
    return results['structured_response']


super_prompt= """
you are supervisor first use find_visa_event
and then use its returned data and use calculate_chance_event
to get final results
"""

super_agent = create_agent(
    model = model,
    tools = [find_visa_event,calculate_chance_event],
    system_prompt= super_prompt,

    response_format= FinalResults
)





