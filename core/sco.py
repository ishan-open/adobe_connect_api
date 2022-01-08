class Sco:
    """
    Attributes
    ----------
    depth : str

    sco_id : str

    folder_id : str

    type : str

    icon : str

    lang : str

    source_sco_id : str

    display_seq : str

    source_sco_type : str

    source_sco_icon : str

    content_source_sco_icon : str

    duration : str

    name : str

    url_path : str

    date_created : str

    date_modified : str
    """
    def __init__(self, sco_dict):
        self.depth = sco_dict["@depth"]
        self.sco_id = sco_dict["@sco-id"]
        self.folder_id = sco_dict["@folder-id"]
        self.type = sco_dict["@type"]
        self.icon = sco_dict["@icon"]
        self.lang = sco_dict["@lang"]
        self.source_sco_id = sco_dict["@source-sco-id"]
        self.display_seq = sco_dict["@display-seq"]
        self.source_sco_type = sco_dict["@source-sco-type"]
        self.source_sco_icon = sco_dict["@source-sco-icon"]
        self.content_source_sco_icon = sco_dict["@content-source-sco-icon"]
        self.duration = sco_dict["@duration"]
        self.name = sco_dict["name"]
        self.url_path = sco_dict["url-path"].replace("/", "")
        self.date_created = sco_dict["date-created"]
        self.date_modified = sco_dict["date-modified"]

    def __repr__(self):
        return f"Sco({self.sco_id})"


class MeetingSco(Sco):
    """
    Attributes
    ----------
    meeting_id : str

    """
    def __init__(self, sco_dict):
        super(MeetingSco, self).__init__(sco_dict)
        self.meeting_id = sco_dict["@sco-id"]


class ScoChanged:
    """
    Attributes
    ----------
    depth : str

    sco_id : str

    folder_id : str

    type : str

    icon : str

    lang : str

    source_sco_id : str

    display_seq : str

    source_sco_type : str

    source_sco_icon : str

    content_source_sco_icon : str

    duration : str

    name : str

    url_path : str

    date_created : str

    date_modified : str
    """
    def __init__(self, sco_dict):
        self.depth = sco_dict["depth"]
        self.sco_id = sco_dict["sco_id"]
        self.folder_id = sco_dict["folder_id"]
        self.type = sco_dict["type"]
        self.icon = sco_dict["icon"]
        self.lang = sco_dict["lang"]
        self.source_sco_id = sco_dict["source_sco_id"]
        self.display_seq = sco_dict["display_seq"]
        self.source_sco_type = sco_dict["source_sco_type"]
        self.source_sco_icon = sco_dict["source_sco_icon"]
        self.content_source_sco_icon = sco_dict["content_source_sco_icon"]
        self.duration = sco_dict["duration"]
        self.name = sco_dict["name"]
        self.url_path = sco_dict["url_path"].replace("/", "")
        self.date_created = sco_dict["date_created"]
        self.date_modified = sco_dict["date_modified"]

    def __repr__(self):
        return f"Sco({self.sco_id})"


class MeetingScoChanged(ScoChanged):
    """
    Attributes
    ----------
    meeting_id : str

    """
    def __init__(self, sco_dict):
        super(MeetingScoChanged, self).__init__(sco_dict)
        self.meeting_id = sco_dict["sco_id"]
