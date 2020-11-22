import os, yaml, json
from typing import Dict, Any
from europy.lifecycle import reporting

def load_global_params(path: str, report=True) -> Dict[str:Any]:
    """Load and return global paramss

    Args:
        path (str): path to param file
        report (bool, optional): Add params to EuroPy report. Defaults to True.

    Returns:
        Dict[str:Any]: global params
    """
    
    params = {}
    with open(path, 'r') as f:
        if os.path.split(path)[-1].split('.')[-1] in ['yml', 'yaml']:
            params = yaml.load(f, Loader=yaml.FullLoader)
        else: 
            params = json.load(f)

    
    global_params = params.get('global', {})
    
    if report:
        reporting.capture_parameters('global', global_params)
    
    return global_params
