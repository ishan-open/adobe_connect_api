from . import Base
from ..core.principal import Principal
from ..exceptions.adobe_exceptions import NotFound


class FindPrincipalId(Base):
    @property
    def principal(self) -> Principal:
        """
        Returns
        -------
        Principal : object
        """
        principal = self.response["results"]["principal-list"]
        if principal is None:
            raise NotFound
        elif principal is not None:
            principal = principal["principal"]
            if isinstance(principal, dict):
                return Principal(principal)
