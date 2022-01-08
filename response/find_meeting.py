from . import Base
from ..core.sco import MeetingScoChanged


class FindMeetingResponse(Base):
    @property
    def meeting(self) -> MeetingScoChanged:
        """
        Returns
        -------
        MeetingScoChanged : object
        """
        return MeetingScoChanged(self.response)
