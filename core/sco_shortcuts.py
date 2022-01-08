class ShortCuts:
    """
    Attributes
    ----------
    tree_id : str

    sco_id : str

    type : str

    domain_name : str
    """
    def __init__(self, parsed_sco_shortcuts):
        self.tree_id = parsed_sco_shortcuts["@tree-id"]
        self.sco_id = parsed_sco_shortcuts["@sco-id"]
        self.type = parsed_sco_shortcuts["@type"]
        self.domain_name = parsed_sco_shortcuts["domain-name"]

    def __repr__(self):
        return f"ShortCuts({self.sco_id})"
