from typing import List
from . import Base
from ..core.sco import MeetingSco


class MeetingsListResponse(Base):
    @property
    def meetings(self) -> List[MeetingSco]:
        """
        Returns
        -------
        meetings : list of MeetingSco
        """
        final_scos = []
        scos = self.response["results"]["expanded-scos"]
        if scos is not None:
            scos = scos["sco"]
            if isinstance(scos, dict):
                if scos["@type"] == "meeting":
                    final_scos.append(MeetingSco(scos))
            elif isinstance(scos, list):
                for sco in scos:
                    if sco["@type"] == "meeting":
                        final_scos.append(MeetingSco(sco))
        elif scos is None:
            return final_scos

        return final_scos
