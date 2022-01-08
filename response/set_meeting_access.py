from . import Base
from ..exceptions.adobe_exceptions import SubCode, InvalidMeetingId, InvalidPrincipalId, InvalidPermissionID


class SetMeetingAccess(Base):
    @property
    def return_code(self):
        if self.status_code == SubCode.no_data:
            raise InvalidPrincipalId
        elif self.sub_code == SubCode.denied and self.status_code == SubCode.no_access:
            raise InvalidMeetingId
        elif self.status_code == SubCode.invalid and self.sub_code == SubCode.format:
            raise InvalidPermissionID
        return self.status_code
