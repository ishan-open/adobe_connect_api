from . import Base
from ..core.sco import Sco
from typing import List


class FindSco(Base):
    @property
    def sco(self) -> List[Sco]:
        """
        Returns
        -------
        sco : list of Sco
        """
        final_scos = []
        scos = self.response["results"]["expanded-scos"]
        if scos is not None:
            scos = scos["sco"]
            if isinstance(scos, dict):
                final_scos.append(Sco(scos))
            elif isinstance(scos, list):
                for sco in scos:
                    final_scos.append(Sco(sco))
            return final_scos
