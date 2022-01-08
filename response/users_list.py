from typing import List
from . import Base
from ..core.principal import UserPrincipal


class UsersListResponse(Base):
    @property
    def users(self) -> List[UserPrincipal]:
        """
        Returns
        -------
        users : list of UserPrincipal
        """
        final_principal = []
        principal = self.response["results"]["principal-list"]
        if principal is None:
            pass
        else:
            principal = principal["principal"]
            if isinstance(principal, dict):
                final_principal.append(UserPrincipal(principal))

            elif isinstance(principal, list):
                for lst in principal:
                    final_principal.append(UserPrincipal(lst))

        return final_principal
