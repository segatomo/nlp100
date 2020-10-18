class Morph:
    """
    Morph represents a morpheme.
    
    Attributes
    ----------
    surface : str
        表層形
    base : str
        基本形
    pos : str
        品詞
    pos1 : str
        品詞再分類1
    """
    def __init__(self, line):
        self.surface = line.split('\t')[0]
        elem = line.split('\t')[1].split(',')
        self.base = elem[6]
        self.pos = elem[0]
        self.pos1 = elem[1]



if __name__ == "__main__":
    morphs = []
    sentences = []
    filename = 'ai.ja.txt.parsed'
    with open(filename) as f:
        for line in f:
            if line[0] == '*':
                continue
            if line != 'EOS\n':
                morphs.append(Morph(line))
            else:
                sentences.append(morphs)

    [print(vars(m)) for m in sentences[2]]