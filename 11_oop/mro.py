class A:
    # def test(self):
    print('from A')
    # pass
class B(A):
    # def test(self):
    print('from B')
    # pass
class C(A):
    # def test(self):
    print('from C')
    # pass

class D(B):
    # def test(self):
    print('from D')
    # pass

class E(C):
    # def test(self):
    print('from E')
    # pass

class H(A):
    # def test(self):
    print('from H')
    # pass
class F(D,E,H):
    # def test(self):
    print('from F')
    # pass
if __name__ == "__main__":
    f=F()
    # f.test()
    print(F.mro())