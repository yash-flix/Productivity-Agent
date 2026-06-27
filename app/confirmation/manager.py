from app.confirmation.state import PendingAction


class ConfirmationManager:

    def __init__(self):

        self.pending = None


    def has_pending(self):

        return self.pending is not None


    def create(

        self,

        tool_name,

        arguments,

        message,

    ):

        self.pending = PendingAction(

            tool_name=tool_name,

            arguments=arguments,

            message=message,

        )


    def confirm(self):

        action = self.pending

        self.pending = None

        return action


    def cancel(self):

        self.pending = None