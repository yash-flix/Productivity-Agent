from langgraph.graph import StateGraph

from langgraph.graph import START

from langgraph.graph import END

from langgraph.prebuilt import ToolNode

from langgraph.prebuilt import tools_condition

from app.graph.state import AgentState

from app.agents.agent import assistant

from app.tools.all_tools import TOOLS


builder = StateGraph(AgentState)

builder.add_node(

    "assistant",

    assistant

)

builder.add_node(

    "tools",

    ToolNode(TOOLS)

)

builder.add_edge(

    START,

    "assistant"

)

builder.add_conditional_edges(

    "assistant",

    tools_condition

)

builder.add_edge(

    "tools",

    "assistant"

)

graph = builder.compile()