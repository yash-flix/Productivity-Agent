from langchain_core.messages import (
    HumanMessage,
    SystemMessage
)

from app.core.llm import get_llm

from app.utils.prompt_loader import load_prompt


class MeetingService:

    def __init__(self):

        self.llm = get_llm()

        self.prompt = load_prompt(

            "meeting_summary.txt"

        )

    def summarize(

        self,

        transcript: str

    ):

        response = self.llm.invoke(

            [

                SystemMessage(

                    content=self.prompt

                ),

                HumanMessage(

                    content=transcript

                )

            ]

        )

        return response.content