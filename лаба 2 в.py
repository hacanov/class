from b import B


class C(B):
    def __init__(self, teka="default_terka", zc="default_mc", pyt='default_pyt'):
        super().__init__(teka, zc, pyt)

    def oooo1(self):
        print("oooon in class C")

    def ooooo2(self):
        print("ooooon in class C")