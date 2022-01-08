from typing import List
from . import Base
from ..core.guest import Guest


class GuestListResponse(Base):
    @property
    def guests(self) -> List[Guest]:
        """
        Returns
        -------
        guests : list of Guest
        """
        final_principal = []
        principal = self.response["results"]["report-bulk-users"]["row"]
        if isinstance(principal, dict):
            final_principal.append(Guest(principal))

        elif isinstance(principal, list):
            for lst in principal:
                final_principal.append(Guest(lst))

        elif principal is None:
            pass

        return final_principal
