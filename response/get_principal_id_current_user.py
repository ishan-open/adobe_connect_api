from . import Base
from ..core.principal import CurrentUser


class GetPrincipalIdCurrentUser(Base):
    @property
    def user(self) -> CurrentUser:
        """
        Returns
        -------
        CurrentUser : object
        """
        principal = self.response["results"]["common"]["user"]
        if principal is not None:
            return CurrentUser(principal)
