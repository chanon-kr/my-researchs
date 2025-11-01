from graph.tools.math_tools import math_tools
from graph.state import GraphState
from graph.util.models import create_model
import os

MODEL= os.getenv('COMMON_LLM_MODEL', "gemini-2.5-flash-lite")
PROVIDER= os.getenv('COMMON_LLM_PROVIDER', "google_genai")
SYSTEM_PROMPT= "You are a helpful assistant tasked with performing arithmetic on a set of inputs."
TEMPERATURE= 0

def tool_calling_node(state: GraphState) :
    print('--Tool Calling Node--')
    llm, prompt= create_model(model= MODEL, 
                              model_provider= PROVIDER, 
                              system_prompt= SYSTEM_PROMPT,
                              other_parameters= {'temperature' : TEMPERATURE},
                              )
    llm_with_tools = llm.bind_tools(math_tools)
    chain= prompt|llm_with_tools
    return {'messages' : chain.invoke(state['messages'])}