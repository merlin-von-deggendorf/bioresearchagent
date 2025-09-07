import requests

class Gwasapi:
    def __init__(self):
        pass

    def get_metadata(self):
        """
        Fetch metadata from the GWAS Catalog API.
        Returns the JSON response as a Python dict.
        """
        url = "https://www.ebi.ac.uk/gwas/rest/api/v2/metadata"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()