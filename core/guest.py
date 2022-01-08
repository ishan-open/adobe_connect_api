class Guest:
    """
    Attributes
    ----------
    principal_id : str

    type : str

    login : str

    name : str
    """
    def __init__(self, guest_dict):
        self.principal_id = guest_dict["@principal-id"]
        self.type = guest_dict["@type"]
        self.login = guest_dict["login"]
        self.name = guest_dict["name"]
        try:
            self.email = guest_dict["email"]
        except KeyError:
            self.email = "None"

    def __repr__(self):
        return f"Guest({self.principal_id})"
