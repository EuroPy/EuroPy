import os
import errno
from typing import Any, List
from europy import report_directory


class Markdown:

    cls_dict_markdown = ""
    tab = "  "
    list_tag = '* '
    htag = '#'

    def __init__(self):
        self.content = ""

    def saveToFile(self, file_name: str):
        file_path = os.path.join(report_directory, file_name)
        if not os.path.exists(file_path):
            try:
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
        file = open(file_path, "w")
        file.write(self.content)
        file.close()

    def add_linebreak(self):
        self.content += self.create_block("", 1)
        return self

    def add_list_item(self, text: str, depth: int = 0):
        intent = ""
        if depth > 0:
            intent = "".join([" " * 2] * depth)

        self.content += self.create_block(intent + "- {}".format(text))
        return self

    def add_header(self, text: str, htype: int = 1):
        string = "".join(["#"] * htype) + " {t}".format(t=text)
        self.content += self.create_block(string, 2)
        return self

    def add_text(self, text: str):
        self.content += self.create_block(text, 2)
        return self

    def add_horizontal_line(self):
        self.content += self.create_block("___")
        return self

    def add_block_content(self, *lines: Any):
        _lines: List[str] = list(lines)
        self.content += self.create_block("> " + "  \n".join(_lines), 2)
        return self

    def add_image(self, url: str, alt_text: str):
        self.content += self.create_block("![{}]({})".format(alt_text, url), 2)
        return self

    @classmethod
    def create_block(cls, text: str = '', lbcount: int = 1):
        return text + "".join(['\n'] * lbcount)

    def add_table(self, *rows: Any):
        contents: List[List[str]] = list(rows)
        for i, items in enumerate(contents):
            self.content += "| " + "| ".join(items) + "\n"
            if i == 0:
                for item in items:
                    self.content += "| "
                    self.content += "".join(["-"] * len(item))
                self.content += "\n"
        self.content += "\n"
        return self

    def add_dict_content(self, data):
        depth = 0
        self.content += "\n"
        self.parseInputData(data, depth)
        self.content += self.getClassMarkdownData()
        self.content += "\n"
        return self

    @classmethod
    def getClassMarkdownData(cls):
        return cls.cls_dict_markdown

    @classmethod
    def parseInputData(cls, data, depth):
        if isinstance(data, dict):
            cls.parseDict(data, depth)
        if isinstance(data, list):
            cls.parseList(data, depth)

    @classmethod
    def parseDict(cls, d, depth):
        for k in d:
            if isinstance(d[k], (dict, list)):
                cls.addHeader(k, depth)
                cls.parseInputData(d[k], depth + 1)
            else:
                cls.addValue(k, d[k], depth)

    @classmethod
    def parseList(cls, lis, depth):
        for value in lis:
            if not isinstance(value, (dict, list)):
                index = lis.index(value)
                cls.addValue(index, value, depth)
            else:
                cls.parseDict(value, depth)

    @classmethod
    def addHeader(cls, value, depth):
        chain = cls.buildHeaderChain(depth)
        cls.cls_dict_markdown += chain.replace('value', value.title())

    @classmethod
    def addValue(cls, key, value, depth):
        chain = cls.buildValueChain(key, value, depth)
        cls.cls_dict_markdown += chain

    @classmethod
    def buildHeaderChain(cls, depth):
        chain = cls.list_tag * (bool(depth)) + cls.htag * (depth + 1) + \
                ' value ' + (cls.htag * (depth + 1) + '\n')
        return chain

    @classmethod
    def buildValueChain(cls, key, value, depth):
        chain = cls.tab * (bool(depth - 1)) + cls.list_tag + \
                str(key) + ": " + str(value) + "\n"
        return chain

