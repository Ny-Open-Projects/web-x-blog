class Base:
    def __init__(self):
        print("Base.__init__")

class A(Base):
    def __init__(self):
        print("A.__init__")
        super().__init__()

class B(Base):
    def __init__(self):
        print("B.__init__")
        super().__init__()

class C(A, B):        # 菱形:A、B 都继承 Base
    def __init__(self):
        print("C.__init__")
        super().__init__()

if __name__ == "__main__":
    C()
    # C -> A -> B -> Base,Base 只初始化一次
    print([c.__name__ for c in C.__mro__])
