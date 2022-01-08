class Usage:
    """
    Attributes
    ----------
    transaction_id : str

    sco_id : str

    principal_id : str

    score : str

    url : str

    login : str

    user_name : str

    status : str

    date_closed : str
    """
    def __init__(self, parsed_meeting):
        self.transaction_id = parsed_meeting["@transaction-id"]
        self.sco_id = parsed_meeting["@sco-id"]
        self.principal_id = parsed_meeting["@principal-id"]
        self.score = parsed_meeting["@score"]
        self.url = parsed_meeting["url"]
        self.login = parsed_meeting["login"]
        self.user_name = parsed_meeting["user-name"]
        self.status = parsed_meeting["status"]
        self.date_closed = parsed_meeting["date-closed"]

    def __repr__(self):
        return f"Usage({self.transaction_id})"
