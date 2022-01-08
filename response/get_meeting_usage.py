from typing import List
from . import Base
from ..core.meeting_usage import Usage


class MeetingUsage(Base):
    @property
    def usages(self) -> List[Usage]:
        """
        Returns
        -------
        usages : list of Usage
        """
        final_usages = []
        usage_dict = self.response["results"]["report-bulk-consolidated-transactions"]["row"]
        if usage_dict is not None:
            if isinstance(usage_dict, dict):
                final_usages.append(Usage(usage_dict))
            elif isinstance(usage_dict, list):
                for i in  usage_dict:
                    final_usages.append(Usage(i))

        return final_usages
