class Meeting:
    """
    Attributes
    ----------
    account_id : str

    disabled : str

    display_seq : str

    folder_id : str

    icon : str

    lang : str

    max_retries : str

    sco_id : str

    source_sco_id : str

    date_begin : str

    date_begin : str

    date_modified : str

    description : str

    name : str

    meeting_id : str

    url_path : str

    date_end : str
    """
    def __init__(self, parsed_meeting):
        self.account_id = parsed_meeting["@account-id"]
        self.disabled = parsed_meeting["@disabled"]
        self.display_seq = parsed_meeting["@display-seq"]
        self.folder_id = parsed_meeting["@folder-id"]
        self.icon = parsed_meeting["@icon"]
        self.lang = parsed_meeting["@lang"]
        self.max_retries = parsed_meeting["@max-retries"]
        self.sco_id = parsed_meeting["@sco-id"]
        self.source_sco_id = parsed_meeting["@source-sco-id"]
        self.date_begin = parsed_meeting["date-begin"]
        self.date_created = parsed_meeting["date-created"]
        self.date_modified = parsed_meeting["date-modified"]
        self.description = parsed_meeting["description"]
        self.name = parsed_meeting["name"]
        self.meeting_id = parsed_meeting["@sco-id"]
        self.url_path = parsed_meeting["url-path"].replace("/", "")
        try:
            self.date_end = parsed_meeting["date-end"]
        except KeyError:
            self.date_end = "For Ever!"

    def __repr__(self):
        return f"Meeting({self.meeting_id})"
