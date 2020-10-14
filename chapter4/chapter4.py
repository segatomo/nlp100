import MeCab
import pprint
import collections
import matplotlib.pyplot as plt
import itertools
import math
plt.rcParams['font.family'] = 'IPAexGothic'

def no30():
    res = []
    with open('neko.txt.mecab') as f:
        sentence = []
        for line in f:
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
    print(res[:10])
    return res


def no32():
    res = []
    morph = no30()
    for sent in morph:
        for token in sent:
            if token['pos'] == '動詞':
                res.append(token['base'])
    print(res[:10])
    return res


def no33():
    res = []
    morph = no30()
    for sent in morph:
        for i, token in enumerate(sent[:len(sent)-2]):
            if (token['pos'] == '名詞') and (sent[i+1]['surface'] == 'の') and (sent[i+2]['pos'] == '名詞'):
                res.append(''.join([s['surface'] for s in sent[i:i+3]]))
    print(res[:10])
    return res


def no34():
    morph = no30()
    res = []
    for sent in morph:
        i = 0
        tmp = []
        while i < len(sent):
            if sent[i]['pos'] == '名詞':
                tmp.append(sent[i]['surface'])
            elif len(tmp) > 1:
                res.append(tmp)
                tmp = []
            else:
                tmp = []
            i += 1
    return max((r for r in res), key=len)


def no35():
    morph = no30()
    words = []
    for sent in morph:
        words.extend([s['base'] for s in sent if (s['pos'] != '記号' and s['surface'] != '')])
    c = collections.Counter(words)
    return c.most_common()


def no36():
    data = no35()[:10]
    plt.figure()
    plt.title('頻度上位10語')
    plt.bar([d[0] for d in data], [d[1] for d in data])
    plt.show()


def no37():
    morph = no30()
    words = [[s['surface'] for s in sent if (s['pos'] != '記号' and s['surface'] != '')] for sent in morph if len(sent) > 1]
    word_combinations = [list(itertools.combinations(word, 2)) for word in words]
    word_combinations = [[tuple(sorted(c)) for c in combi if '猫' in c] for combi in word_combinations]
    cat_list = list(itertools.chain.from_iterable(word_combinations))
    c = collections.Counter(cat_list)
    data = c.most_common(10)
    plt.figure()
    plt.title('「猫」と共起頻度の高い上位10語')
    plt.bar([d[0][0] for d in data], [d[1] for d in data])
    plt.show()


def no38():
    data = [d[1] for d in no35()]
    plt.figure()
    plt.hist(data, bins=100)
    plt.show()


def no39():
    data = no35()
    plt.figure()
    plt.scatter(list(range(1,len(data)+1)) ,[d[1] for d in data])
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('単語の出現頻度順位')
    plt.ylabel('単語の出現頻度')
    plt.show()


if __name__ == "__main__":
    no39()