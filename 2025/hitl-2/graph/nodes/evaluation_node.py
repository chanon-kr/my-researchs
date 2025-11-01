from graph.tools.math_tools import math_tools
from graph.state import GraphState
from graph.util.models import create_model
import os
# Import Structure Output related
from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser

MODEL= os.getenv('COMMON_LLM_MODEL', "gemini-2.5-flash-lite")
PROVIDER= os.getenv('COMMON_LLM_PROVIDER', "google_genai")
# Create Structure Output
class EvaluationResult(BaseModel):
    evaluation_result: bool = Field(..., description="Question related to provided tools or not")
    evaluation_reason : str = Field(..., description="Reason why the question related or not related to the tools")

parser= JsonOutputParser(pydantic_object= EvaluationResult)

SYSTEM_PROMPT= """
You are a helpful assistant tasked to evaluated if user's input related to the tools or not.

Your output should be in this format.
{format_instructions}
"""

TEMPERATURE= 0

def evaluation_node(state: GraphState) :
    print('--Evaluate Node--')
    llm, prompt= create_model(model= MODEL, 
                              model_provider= PROVIDER, 
                              system_prompt= SYSTEM_PROMPT,
                              other_parameters= {'temperature' : TEMPERATURE},
                              )
    llm_with_tools = llm.bind_tools(math_tools)
    json_prompt= prompt.partial(format_instructions=parser.get_format_instructions())

    chain= json_prompt|llm_with_tools|parser
    return chain.invoke(state['messages'])