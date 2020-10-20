from chapter5_40 import Morph

class Chunk:
    """
    Chunk represents a phase.

    Attributes
    ----------
    morphs : list
        形態素(Morph)オブジェクトのリスト
    dst : int
        係り先文節インデックス番号
    srcs : list
        係り元文節インデックス番号のリスト
    """
    def __init__(self, morphs, dst):
        self.morphs = []
        self.dst = dst
        self.srcs = []


def process_chunk(filename):
    chunks = []
    sentence = []
    with open(filename) as f:
        for line in f:
            if line[0] == '*':
                chunk = Chunk(line, int(line.split(' ')[2].rstrip('D')))
                sentence.append(chunk)
            elif line != 'EOS\n':
                chunk.morphs.append(Morph(line))
            else:
                for i, chunk in enumerate(sentence):
                    if chunk.dst != -1:
                        sentence[chunk.dst].srcs.append(i)
                chunks.append(sentence)
                sentence = []

    return chunks


if __name__ == "__main__":
    filename = 'ai.ja.txt.parsed'
    chunks = process_chunk(filename)
    for c in chunks[2]:
        [print(m.surface) for m in c.morphs]
        print(c.dst)
        print(c.srcs)