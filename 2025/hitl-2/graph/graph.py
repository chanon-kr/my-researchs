from langgraph.graph import StateGraph, END, START
from langgraph.prebuilt import tools_condition, ToolNode
from graph.tools.math_tools import math_tools

from graph.state import GraphState
from graph.nodes.evaluation_node import evaluation_node
from graph.nodes.evaluation_hitl_node import evaluation_hitl_node
from graph.nodes.tools_calling_node import tool_calling_node
from graph.nodes.tools_hitl_node import tools_hitl_node
from graph.tools.custom_tools_condition import custom_tools_condition, tools_router
from langgraph.checkpoint.memory import MemorySaver

# Graph
builder = StateGraph(GraphState)

# Define nodes: these do the work
builder.add_node("evaluation_node", evaluation_node)
builder.add_node("evaluation_hitl_node", evaluation_hitl_node)


builder.add_edge(START, 'evaluation_node')

evaluation_condition= lambda x : 'GO' if x['evaluation_result'] else 'ASK'
builder.add_edge("evaluation_hitl_node", 'evaluation_node')
builder.add_conditional_edges(
    "evaluation_node",
    evaluation_condition,
    {
        'ASK' : 'evaluation_hitl_node',
        'GO' : END,
        # 'GO' : 'react',
    }
)


# ## STEP 2
# builder.add_node("react", tool_calling_node)
# builder.add_node("tool_hitl_node", tools_hitl_node)
# builder.add_node("tools", ToolNode(math_tools))
# builder.add_conditional_edges(
#     "react",
#     # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
#     # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
#     custom_tools_condition,
# )
# builder.add_conditional_edges(
#     "tool_hitl_node",
#     tools_router,
# )
# builder.add_edge("tools", "react")


memory = MemorySaver()
graph = builder.compile(checkpointer=memory)