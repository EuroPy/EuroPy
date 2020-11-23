# This file can be used to write markdown
import sys
import json

markdown = ""
tab = "  "
list_tag = '* '
htag = '#'
root_report_directory = '.europy/reports'  # this directory location is only temporary - we will discuss and choose the right logic for this
report_directory = ""


def parseDict(d, depth):
    for k in d:
        if isinstance(d[k], (dict, list)):
            addHeader(k, depth)
            parseJSON(d[k], depth + 1)
        else:
            addValue(k, d[k], depth)


def addHeader(value, depth):
    chain = buildHeaderChain(depth)
    global markdown
    markdown += chain.replace('value', value.title())


def addValue(key, value, depth):
    chain = buildValueChain(key, value, depth)
    global markdown
    markdown += chain


def parseJSON(json_block, depth):
    if isinstance(json_block, dict):
        parseDict(json_block, depth)
    if isinstance(json_block, list):
        parseList(json_block, depth)


def parseList(l, depth):
    for value in l:
        if not isinstance(value, (dict, list)):
            index = l.index(value)
            addValue(index, value, depth)
        else:
            parseDict(value, depth)


def buildHeaderChain(depth):
    chain = list_tag * (bool(depth)) + htag * (depth + 1) + \
            ' value ' + (htag * (depth + 1) + '\n')
    return chain


def buildValueChain(key, value, depth):
    chain = tab * (bool(depth - 1)) + list_tag + \
            str(key) + ": " + str(value) + "\n"
    return chain


def writeOut(markdown, output_file):
    file_path = os.path.join(report_directory, output_file)
    with open(file_path, 'w+') as f:
        f.write(markdown)


def writeMD(input_data, output_file):
    depth = 0
    parseJSON(input_data, depth)
    global markdown
    markdown = markdown.replace('#######', '######')
    writeOut(markdown, output_file)


def main():
    if len(sys.argv) > 1:
        input_data = sys.argv[1]
        output_file = output_file + 'markdown'
        writeMD(input_data, output_file)
    else:
        print('\n' + "you must specify an input stream.")
