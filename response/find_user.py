from . import Base
from ..core.principal import UserPrincipal
from ..exceptions.adobe_exceptions import NotFound


class FindUserResponse(Base):
    @property
    def user(self) -> UserPrincipal:
        """
        Returns
        -------
        UserPrincipal : object
        """
        principal = self.response["results"]["principal-list"]
        if principal is None:
            raise NotFound
        elif principal is not None:
            principal = principal["principal"]
            if isinstance(principal, dict):
                return UserPrincipal(principal)

