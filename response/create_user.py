from . import Base
from ..core.principal import CreatePrincipal
from ..exceptions.adobe_exceptions import SubCode, Duplicate


class CreateUserResponse(Base):
    @property
    def user(self) -> CreatePrincipal:
        """

        Returns
        -------
        CreatePrincipal : object
        """
        if self.status_code == SubCode.invalid and self.sub_code == SubCode.duplicate:
            raise Duplicate
        principal = self.response["results"]["principal"]
        if principal is not None:
            return CreatePrincipal(principal)
