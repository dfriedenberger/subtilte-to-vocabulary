
class LevelDetector:

    def __init__(self,filename):

        self.word_map = {}
        with open(filename,'r',encoding="UTF-8") as f:

            for line in f.readlines():
                p = line.strip().split(";")
                if len(p) != 2:
                    raise ValueError(f"Cannot read line:{line}")

                self.word_map[p[0]] = p[1]

    def get_level(self,word):
        k = word.lower()
        if k not in self.word_map:
            return "XX"
        return self.word_map[k]
