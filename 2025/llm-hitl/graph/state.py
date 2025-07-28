from langgraph.graph import MessagesState

class GraphState(MessagesState):
    human_input : str
    feedback : str