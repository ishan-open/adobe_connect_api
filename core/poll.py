class Poll:
    """
    Attributes
    ----------
    display_seq : str

    transcript_id : str

    interaction_id : str

    sco_id : str

    score : str

    name : str

    sco_name : str

    date_created : str

    description : str

    response : str
    """
    def __init__(self, parsed_poll_results):
        self.display_seq = parsed_poll_results["@display-seq"]
        self.transcript_id = parsed_poll_results["@transcript-id"]
        self.interaction_id = parsed_poll_results["@interaction-id"]
        self.sco_id = parsed_poll_results["@sco-id"]
        self.score = parsed_poll_results["@score"]
        self.name = parsed_poll_results["name"]
        self.sco_name = parsed_poll_results["sco-name"]
        self.date_created = parsed_poll_results["date-created"]
        self.description = parsed_poll_results["description"]
        self.response = parsed_poll_results["response"]

    def __repr__(self):
        return f"Poll({self.transcript_id})"
