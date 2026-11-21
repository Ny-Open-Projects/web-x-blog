class MetaA(type): pass
class MetaB(type): pass

class A(metaclass=MetaA): pass
class B(metaclass=MetaB): pass

try:
    class C(A, B): pass            # 两个不相干的 metaclass
except TypeError as e:
    print("conflict:", e)

# 仅有公共基类不够:MetaA2 与 MetaB2 是兄弟,组合 A2、B2 依然冲突
class MetaCommon(type):
    def __new__(mcls, name, bases, ns):
        cls = super().__new__(mcls, name, bases, ns)
        print("built by MetaCommon:", name)
        return cls

class MetaA2(MetaCommon): pass
class MetaB2(MetaCommon): pass
class A2(metaclass=MetaA2): pass
class B2(metaclass=MetaB2): pass

try:
    class C2(A2, B2): pass        # 兄弟 metaclass 不会自动合并
except TypeError as e:
    print("conflict again:", e)

# 真正的解法:显式给出同时继承两者的组合 metaclass,成为唯一 most derived
class MetaCombined(MetaA2, MetaB2): pass
class C3(A2, B2, metaclass=MetaCombined): pass

print("type(C3):", type(C3).__name__)              # MetaCombined
print("issubclass check:", issubclass(C3, A2) and issubclass(C3, B2))
