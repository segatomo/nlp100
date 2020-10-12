import MeCab
import pprint


def no30():
    res = []
    with open('neko.txt.mecab') as f:
        sentence = []
        for i, line in enumerate(f):
            out = line.rstrip('\n').split('\t')
            if out[0] == 'EOS':
                res.append(sentence)
                sentence = []
                continue
            if len(out) > 1:
                surface = out[0]   # 表層形
                elem = out[1].split(',')
                base = elem[6]   # 基本形
                pos = elem[0]   # 品詞
                pos1 = elem[1]   # 品詞細分類1
                sentence.append({
                    'surface': surface,
                    'base': base,
                    'pos': pos,
                    'pos1': pos1,
                })
    # pprint.pprint(res[:10])
    return res


def no31():
    res = []
    for sent in no30():
        for token in sent:
            if token['pos'] == '動詞':
                res.append(token['surface'])
    # print(res)
    return res


def no32():
    res = []
    for sent in no30():
        for token in sent:
            if token['pos'] == '動詞':
                res.append(token['base'])
    # print(res)
    return res

if __name__ == "__main__":
    no32()