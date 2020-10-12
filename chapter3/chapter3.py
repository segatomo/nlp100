import json
import re


def no20():
    json_open = open('jawiki-country.json', 'r')
    for j in json_open:
        json_load = json.loads(j)
        if json_load['title'] == 'イギリス':
            return json_load['text']


def no21():
    text = no20()
    pat = r'^(.*\[\[Category:.*\]\].*)$'
    res = re.findall(pat, text, re.MULTILINE)
    return res


def no22():
    text = no21()
    res = []
    for t in text:
        res.append(t.replace('[[Category:', '').replace(']]', ''))
    return res


def no23():
    text = no20()
    pat = r'^(={2,})\s*(.+?)\s*\1.*$'
    res = re.findall(pat ,text, re.MULTILINE + re.VERBOSE)
    for r in res:
        if r[0] == '==':
            print(r[1], 1)
        elif r[0] == '===':
            print(' ' , r[1], 2)
        elif r[0] == '====':
            print('  ', r[1], 3)
    return res


if __name__ == "__main__":
    # print(no20())
    # print(no21())
    # print(no22())
    no23()