from typing import List
from . import Base
from ..core.principal import Principal


class PrincipalsList(Base):
    @property
    def principals(self) -> List[Principal]:
        """
        Returns
        -------
        principals : list of Principal
        """
        final_principal = []
        principal = self.response["results"]["principal-list"]
        if principal is None:
            pass
        else:
            principal = principal["principal"]
            if isinstance(principal, dict):
                final_principal.append(Principal(principal))

            elif isinstance(principal, list):
                for lst in principal:
                    final_principal.append(Principal(lst))

        return final_principal
