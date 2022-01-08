class Base:
    """
    Base Reponse object

    Parameters
    ----------
    parsed_xml : dict

    Attributes
    ----------
    response : dict
    """
    def __init__(self, parsed_xml):
        """
        Parameters
        ----------
        parsed_xml : dict
        """
        self.response = parsed_xml

    @property
    def status_code(self):
        """
        returns status code.

        Returns
        -------
        status : str
        """
        return self.response["results"]["status"]["@code"]

    @property
    def sub_code(self):
        """
        returns sub code.

        Returns
        -------
        status : str
        """
        try:
            return self.response["results"]["status"]["invalid"]["@subcode"]
        except KeyError:
            try:
                return self.response["results"]["status"]["@subcode"]
            except KeyError:
                pass
