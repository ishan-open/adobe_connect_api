class Permission:
    """
    Attributes
    ----------
    principal_id : str

    is_primary : str

    type : str

    has_children : str

    name : str

    display_uid : str
    """
    def __init__(self, principal_dict):
        self.principal_id = principal_dict["@principal-id"]
        self.is_primary = principal_dict["@is-primary"]
        self.type = principal_dict["@type"]
        self.has_children = principal_dict["@has-children"]
        self.permission_id = principal_dict["@permission-id"]
        self.name = principal_dict["name"]
        self.display_uid = principal_dict["display-uid"]

    def __repr__(self):
        return f"Permission({self.principal_id})"
