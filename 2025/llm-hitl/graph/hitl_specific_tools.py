from langgraph.graph import StateGraph, END
from langgraph.prebuilt import tools_condition, ToolNode

from graph.state import GraphState
from graph.nodes.tools_calling import tool_calling_node
from graph.nodes.hitl import hitl_node
from graph.tools.math_tools_specific_hitl import math_tools
from graph.tools.custom_tools_condition import custom_tools_condition, tools_router
from langgraph.checkpoint.memory import MemorySaver

# Graph
builder = StateGraph(GraphState)

# Define nodes: these do the work
builder.add_node("assistant", tool_calling_node)
builder.add_node("tools", ToolNode(math_tools))

# Define edges: these determine the control flow
builder.set_entry_point("assistant")
builder.add_conditional_edges(
    "assistant",
    # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
    # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
    tools_condition,
)
builder.add_edge("tools", "assistant")

memory = MemorySaver()
graph = builder.compile(checkpointer=memory)