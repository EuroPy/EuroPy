from datetime import datetime
from typing import List, Optional

class ModelDetails:
    def __init__(self, title: str,
            organization: Optional[str]=None,
            authors: List[str]=[],
            emails: List[str]=[],
            model_date: datetime=datetime.now(),
            model_version: str='--',
            citation_details: str='--',
            model_license: str='--',
            model_url: str='--',
            data_license: str='--',
            data_url: str='--',
            description: str='--'):
        """[summary]

        Args:
            title (str): Title of the model card
            organization (Optional[str], optional): Organization or company developing the model. Defaults to None.
            authors (List[str], optional): list of author names. Defaults to [].
            emails (List[str], optional): list of author email (mapped to authors). Defaults to [].
            model_date (datetime, optional): date of the model publication. Defaults to datetime.now().
            model_version (str, optional): version of the model. Defaults to '--'.
            citation_details (str, optional): how to cite the model (e.g. BibTex). Defaults to '--'.
            model_license (str, optional): license associated with the model code. Defaults to '--'.
            model_url (str, optional): url associated with the model code. Defaults to '--'.
            data_license (str, optional): license associated with the model's data: Defaults to '--'.
            data_url: (str, optional): url associated with the model's data. Defaults to '--'.
            description (str, optional): . Defaults to '--'.
        """

        self.title = title
        self.organization = organization
        self.authors = authors
        self.emails = emails
        self.model_date = model_date
        self.model_version = model_version
        self.citation_details = citation_details
        
        self.model_license = model_license
        self.model_url = model_url

        self.data_license = data_license
        self.data_url = data_url
        
        self.description = description