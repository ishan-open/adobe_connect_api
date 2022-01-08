class Feature:
    """
    Attributes
    ----------
    account_id : str

    feature_id : str

    date_begin : str

    date_end : str

    record_created : str
    """
    def __init__(self, parsed_feature_xml):
        self.account_id = parsed_feature_xml["@account-id"]
        self.feature_id = parsed_feature_xml["@feature-id"]
        self.date_begin = parsed_feature_xml["date-begin"]
        self.date_end = parsed_feature_xml["date-end"]
        self.record_created = parsed_feature_xml["recordcreated"]
