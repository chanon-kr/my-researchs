from graph.state import GraphState
from langgraph.types import interrupt
import os

def tools_hitl_node(state: GraphState):
    print('--Tool HITL Node--')
    tool_calls= state['messages'][-1].tool_calls
    confirm_message= ' \n'.join([f"{tool['name']}, {tool['args']}" for tool in tool_calls])
    answer = interrupt(f"About to run :\n{confirm_message}\n\nPress : [ok] to confirm")
    if answer.lower().strip() == 'ok' :
        return {'human_input' : 'ok'}
    else :
        return {'messages' : ('human', answer), 'human_input' : 'ng'}