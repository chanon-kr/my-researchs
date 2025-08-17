from graph.tools.math_tools import math_tools
from graph.state import GraphState
from graph.util.models import create_model
from langgraph.types import interrupt
import os

MODEL= os.getenv('COMMON_LLM_MODEL', "gemini-2.5-flash-lite")
PROVIDER= os.getenv('COMMON_LLM_PROVIDER', "google_genai")
SYSTEM_PROMPT= "You are a helpful assistant tasked with performing arithmetic on a set of inputs."

def hitl_node(state: GraphState):
    print('--Tool Calling Node--')
    tool_calls= state['messages'][-1].tool_calls
    confirm_message= ' \n'.join([f"{tool['name']}, {tool['args']}" for tool in tool_calls])
    answer = interrupt(f"About to run :\n{confirm_message}\n\nPress : [ok] to confirm")
    if answer.lower().strip() == 'ok' :
        return {'human_input' : 'ok'}
    else :
        return {'messages' : ('human', answer), 'human_input' : 'ng'}