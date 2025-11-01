from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

def create_model(model:str, 
                 model_provider:str, 
                 system_prompt:str,
                 other_parameters:dict
                 ):

    llm = init_chat_model(model=model, model_provider= model_provider, **other_parameters)
    prompt= ChatPromptTemplate([('system', system_prompt), ('human', '{user_input}')])
    return llm, prompt