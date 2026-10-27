#Defines the state that all agents will use
from langchain.messages import AnyMessage
from typing_extensions import TypedDict, Annotated
import operator

class ResearchState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    llm_calls: int
