from . import Base
from ..core.meeting import Meeting
from ..exceptions.adobe_exceptions import SubCode, Duplicate


class CreateMeeting(Base):
    @property
    def meeting(self) -> Meeting:
        """
        Returns
        -------
        Meeting : object
        """
        if self.status_code == SubCode.invalid and self.sub_code == SubCode.duplicate:
            raise Duplicate
        meeting = self.response["results"]["sco"]
        if meeting is not None:
            return Meeting(meeting)
