class CustomField:
    """
    Attributes
    ----------
    object_type : str
    permission_id : str
    permission_id : str

    """
    def __init__(self, parsed_customfield_xml):
        self.object_type = parsed_customfield_xml["@object-type"]
        self.permission_id = parsed_customfield_xml["@permission-id"]
        self.field_type = parsed_customfield_xml["@field-type"]
        self.is_required = parsed_customfield_xml["@is-required"]
        self.is_primary = parsed_customfield_xml["@is-primary"]
        self.display_seq = parsed_customfield_xml["@display-seq"]
        self.account_id = parsed_customfield_xml["@account-id"]
        self.field_id = parsed_customfield_xml["@field-id"]
        self.name = parsed_customfield_xml["name"]
        try:
            self.comments = parsed_customfield_xml["comments"]
        except KeyError:
            pass
