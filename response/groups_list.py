from typing import List
from . import Base
from ..core.principal import GroupPrincipal


class GroupsListResponse(Base):
    @property
    def groups(self) -> List[GroupPrincipal]:
        """
        Returns
        -------
        groups : list of GroupPrincipal
        """
        final_principal = []
        principal = self.response["results"]["principal-list"]
        if principal is None:
            pass
        else:
            principal = principal["principal"]
            if isinstance(principal, dict):
                final_principal.append(GroupPrincipal(principal))

            elif isinstance(principal, list):
                for lst in principal:
                    final_principal.append(GroupPrincipal(lst))

        return final_principal
