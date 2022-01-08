from . import Base
from ..core.poll import Poll
from typing import List


class PollResults(Base):
    @property
    def results(self) -> List[Poll]:
        """
        Returns
        -------
        results : list of Poll
        """
        final_results = []
        polls = self.response["results"]["report-quiz-interactions"]
        if polls is not None:
            polls = polls["row"]
            if isinstance(polls, dict):
                final_results.append(Poll(polls))
            elif isinstance(polls, list):
                for i in polls:
                    final_results.append(Poll(i))
        return final_results
