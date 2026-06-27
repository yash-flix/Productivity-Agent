from dataclasses import dataclass


@dataclass
class PendingAction:

    tool_name: str

    arguments: dict

    message: str