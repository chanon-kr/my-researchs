
from typing import (
    Any,
    Literal,
    Union,
)

from langchain_core.messages import AnyMessage
from pydantic import BaseModel

from graph.state import GraphState


def custom_tools_condition(
    state: Union[list[AnyMessage], dict[str, Any], BaseModel],
    messages_key: str = "messages",
) -> Literal["hitl", "__end__"]:
    if isinstance(state, list):
        ai_message = state[-1]
    elif isinstance(state, dict) and (messages := state.get(messages_key, [])):
        ai_message = messages[-1]
    elif messages := getattr(state, messages_key, []):
        ai_message = messages[-1]
    else:
        raise ValueError(f"No messages found in input state to tool_edge: {state}")
    if hasattr(ai_message, "tool_calls") and len(ai_message.tool_calls) > 0:
        return "hitl"
    return "__end__"

def tools_router(
    state: GraphState
) -> Literal["tools", "assistant"]:
    if state['human_input'] == 'ok' :
        return 'tools'
    else :
        return 'assistant'