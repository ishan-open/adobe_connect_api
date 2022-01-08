from . import Base
from ..core.feature import Feature


class CheckAccountPasscode(Base):
    @property
    def passcodes(self):
        final_passcode = []
        passcodes = self.response["results"]["disabled-features"]
        if passcodes is not None:
            passcodes = passcodes["feature"]
            if isinstance(passcodes, dict):
                final_passcode.append(Feature(passcodes))
            elif isinstance(passcodes, list):
                for passcode in passcodes:
                    final_passcode.append(Feature(passcode))
        elif passcodes is None:
            pass

        return final_passcode
