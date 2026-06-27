import json

from app.core.llm import get_llm


llm = get_llm()


def supervisor_node(state):

    user_message = state["messages"][-1]["content"]

    prompt = f"""
You are a routing agent.

Choose ONE tool.

Available:

slides

todo

excel

calendar

meetings

User:

{user_message}

Return ONLY valid JSON.

Example

{{
"tool":"todo",
"args":{{}},
"confirmation_required":true
}}
"""

    response = llm.invoke(prompt)

    decision = json.loads(response.content)

    return {

        "tool_name": decision["tool"],

        "tool_args": decision["args"],

        "confirmation_required": decision["confirmation_required"]

    }