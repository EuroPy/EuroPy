import os, yaml
from europy.lifecycle import reporting

def load_global_params(path, report=True):
    
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
