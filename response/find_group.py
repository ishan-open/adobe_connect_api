from . import Base
from ..core.principal import GroupPrincipal
from ..exceptions.adobe_exceptions import NotFound


class FindGroupResponse(Base):
    @property
    def group(self) -> GroupPrincipal:
        """
        Returns
        -------
        GroupPrincipal : object
        """
        principal = self.response["results"]["principal-list"]
        if principal is None:
            raise NotFound
        elif principal is not None:
            principal = principal["principal"]
            if isinstance(principal, dict):
                return GroupPrincipal(principal)
