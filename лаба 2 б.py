from а import A


class B(A):
    def __init__(self, teka, zc, pyt):
        super().__init__(teka, zc)
        self.pyt = pyt

    def ooo(self):
        print("ooon in class B")
