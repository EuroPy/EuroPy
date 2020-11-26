import os
from datetime import datetime

root_report_directory = '.europy/reports'
report_directory = os.path.join(root_report_directory, f'{datetime.now().strftime("%d%m%Y_%H%M%S")}')