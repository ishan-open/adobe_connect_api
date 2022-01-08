from . import Base
from ..core.permission import Permission


class Permissions(Base):
    @property
    def principals(self):
        final_principal = []
        principal = self.response["results"]["permissions"]
        if principal is None:
            pass
        else:
            principal = principal["principal"]
            if isinstance(principal, dict):
                final_principal.append(Permission(principal))

            elif isinstance(principal, list):
                for lst in principal:
                    final_principal.append(Permission(lst))

        return final_principal
