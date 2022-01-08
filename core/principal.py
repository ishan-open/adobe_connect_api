class BasePrincipal:
    """
    Attributes
    ----------
    principal_id : str
        Each Adobe Connect user and group has a principal-id.
        Unique ID used for any call.

    type : str
        Shows the principal type.

    has_children : str
        Shows the principal how many children have.

    account_id : str

    name : str
        Shows name of principal.

    login : str
        username of principal for login to adobe connect.

    """
    def __init__(self, principal_dict):
        self.principal_id = principal_dict["@principal-id"]
        self.type = principal_dict["@type"]
        self.has_children = principal_dict["@has-children"]
        self.account_id = principal_dict["@account-id"]
        self.name = principal_dict["name"]
        self.login = principal_dict["login"]


class Principal(BasePrincipal):
    """
        Attributes
        ----------
        is_primary : str

        is_hidden : str

        is_ecommerce : str

        training_group_id : str

        display_uid : str
        """
    def __init__(self, principal_dict):
        super().__init__(principal_dict)
        try:
            self.email = principal_dict["email"]
        except KeyError:
            pass
        self.is_primary = principal_dict["@is-primary"]
        self.is_hidden = principal_dict["@is-hidden"]
        self.is_ecommerce = principal_dict["@is-ecommerce"]
        self.training_group_id = principal_dict["@training-group-id"]
        self.display_uid = principal_dict["display-uid"]

    def __repr__(self):
        return f"Principal({self.principal_id})"


class UserPrincipal(Principal):
    """
    Attributes
    ----------
    user_id : str

    """
    def __init__(self, principal_dict):
        super(UserPrincipal, self).__init__(principal_dict)
        self.user_id = principal_dict["@principal-id"]


class GroupPrincipal(Principal):
    """
    Attributes
    ----------
    group_id : str
    """
    def __init__(self, principal_dict):
        super(GroupPrincipal, self).__init__(principal_dict)
        self.group_id = principal_dict["@principal-id"]


class CreatePrincipal(BasePrincipal):
    """
    Attributes
    ----------
    ext_login : str

    """
    def __init__(self, principal_dict):
        super().__init__(principal_dict)
        self.ext_login = principal_dict["ext-login"]

    def __repr__(self):
        return f"CreatePrincipal({self.principal_id})"


class CurrentUser:
    """
    Attributes
    ----------

    user_id : str

    user_type : str

    name : str

    login : str
    """
    def __init__(self, parsed_current_xml):
        self.user_id = parsed_current_xml["@user-id"]
        self.user_type = parsed_current_xml["results"]["common"]["user"]["@type"]
        self.name = parsed_current_xml["results"]["common"]["user"]["name"]
        self.login = parsed_current_xml["results"]["common"]["user"]["login"]
