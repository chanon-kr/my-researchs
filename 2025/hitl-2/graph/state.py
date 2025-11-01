from langgraph.graph import MessagesState

class GraphState(MessagesState):
    human_input : str
    feedback : str
    evaluation_result : bool
    evaluation_reason : str