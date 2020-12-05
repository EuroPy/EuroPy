import os, yaml, json
from datetime import datetime
from typing import List, Optional
from europy.lifecycle.markdowner import Markdown
from europy.lifecycle.model_details import ModelDetails


class ModelCard:
    def __init__(self, model_details: ModelDetails=ModelDetails(title="--"), parameters={}):
        self.model_details = model_details
        self.parameters = parameters

    def to_markdown(self, level=2):
        md = Markdown()
        md.add_header('Model Card', level)

        md += self.model_details.to_markdown(level=level+1)
        
        md.add_header('Parameters', level+1)
        md.add_dict_content(self.parameters, depth=level+1)

        return md
        