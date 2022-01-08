from typing import List
from . import Base
from ..core.sco_shortcuts import ShortCuts


class ScoShortcuts(Base):
    @property
    def shortcuts(self) -> List[ShortCuts]:
        """
        Returns
        -------
        shortcuts : list of ShortCuts
        """
        final_scos = []
        scos = self.response["results"]["shortcuts"]
        if scos is not None:
            scos = scos["sco"]
            if isinstance(scos, dict):
                final_scos.append(ShortCuts(scos))
            elif isinstance(scos, list):
                for sco in scos:
                    final_scos.append(ShortCuts(sco))
        elif scos is None:
            pass

        return final_scos
