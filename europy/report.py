class Report(object):
    def __init__(self):
        pass


class BasicReport(Report):
    def __init__(self, status):
        super(BasicReport).__init__()
        self.status = status
