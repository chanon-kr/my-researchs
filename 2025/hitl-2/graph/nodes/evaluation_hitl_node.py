from graph.tools.math_tools import math_tools
from graph.state import GraphState
from graph.util.models import create_model
from langgraph.types import interrupt
import os

def evaluation_hitl_node(state: GraphState):
    print('--EVA HITL Node--')
    answer = interrupt(f"{state['evaluation_reason']}\nPlease ask the related question :")
    return {'messages' : ('human', answer)}