from . import Base
from ..core.custom_field import CustomField
from typing import List


class CustomFields(Base):
    @property
    def fields(self) -> List[CustomField]:
        """
        Returns
        -------
        fields : list of CustomField
        """
        final_fields = []
        fields = self.response["results"]["custom-fields"]
        if fields is not None:
            fields = self.response["results"]["custom-fields"]["field"]
            if isinstance(fields, dict):
                final_fields.append(CustomField(fields))

            elif isinstance(fields, list):
                for field in fields:
                    final_fields.append(CustomField(field))

        elif fields is None:
            pass

        return final_fields
