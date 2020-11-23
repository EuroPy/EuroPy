class ReportFigure:
    def __init__(self, img_path=None, title=None, description=None, tag=None):
        self.img_path = img_path
        self.title = title
        self.description = description
        self.tag = tag

    def __str__(self):
        return f'ReportFigure(\n\ttitle: {self.title},\n\tdescription: {self.description},\n\ttag: {self.tag}\n)'
    
    def __repr__(self):
        return f'ReportFigure(title: {self.title}, description: {self.description}, tag: {self.tag})'
