from langchain_core.messages import HumanMessage

from app.graph.workflow import graph


while True:

    user = input("\nYou : ")

    if user.lower() == "exit":

        break

    response = graph.invoke(

        {

            "messages": [

                HumanMessage(content=user)

            ]

        }

    )

    print()

    print(

        "Assistant:",

        response["messages"][-1].content

    )