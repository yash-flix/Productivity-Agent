from langchain_core.tools import tool

from app.services.presentation_service import PresentationService

presentation_service = PresentationService()


@tool
def create_presentation(topic: str) -> str:
    """
    Create a PowerPoint presentation on a topic.
    """

    slides = [

        {
            "title": "Introduction",
            "bullets": [
                f"What is {topic}",
                "Why it matters",
                "Key concepts"
            ]
        },

        {
            "title": "Architecture",
            "bullets": [
                "Components",
                "Workflow",
                "Implementation"
            ]
        },

        {
            "title": "Applications",
            "bullets": [
                "Real-world use cases",
                "Benefits",
                "Industry adoption"
            ]
        },

        {
            "title": "Advantages",
            "bullets": [
                "Automation",
                "Productivity",
                "Scalability"
            ]
        },

        {
            "title": "Challenges",
            "bullets": [
                "Cost",
                "Security",
                "Maintenance"
            ]
        },

        {
            "title": "Conclusion",
            "bullets": [
                "Summary",
                "Future",
                "Next Steps"
            ]
        }

    ]

    filepath = presentation_service.create_presentation(
        title=topic,
        slides=slides
    )

    return f"Presentation saved to {filepath}"