from . import Base
from ..core.custom_field import CustomField


class CreateCustomField(Base):
    @property
    def field(self) -> CustomField:
        """
        Returns
        -------
        CustomField : object
        """
        return CustomField(self.response["results"]["field"])
