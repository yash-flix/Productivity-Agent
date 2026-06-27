from langchain_core.messages import SystemMessage

from app.core.llm import get_llm
from app.tools.all_tools import TOOLS
from app.utils.prompt_loader import load_prompt


system_prompt = load_prompt("system.txt")


def assistant(state):

    llm = get_llm().bind_tools(TOOLS)

    messages = [

        SystemMessage(content=system_prompt)

    ] + state["messages"]

    response = llm.invoke(messages)

    return {

        "messages": [

            response

        ]

    }