class mymy:
    def __init__(self):
        self.seq = ""
        self.gc = 0.0
        print("class mymy created!")

    def calcGC(self, seq):
        c = self.seq.count("C")
        g = self.seq.count("G")
        self.gc =float(c+g) / len(self.seq)
