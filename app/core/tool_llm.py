from app.core.llm import get_llm

from app.tools.all_tools import TOOLS


def get_tool_llm():

    return get_llm().bind_tools(TOOLS)