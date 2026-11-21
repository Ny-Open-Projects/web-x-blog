from collections.abc import Sequence
from functools import singledispatch

@singledispatch
def render(arg):
    return f"fallback: {arg!r}"

@render.register
def _(arg: list):                 # 具体类型
    return f"list of {len(arg)}"

@render.register
def _(arg: Sequence):             # 更泛的 ABC,list 是其虚拟子类
    return "sequence-like"

print(render([1, 2]))             # list of 2 —— 最具体的赢,顺序无关
print(render((1, 2)))             # sequence-like
print(render("abc"))              # fallback? str 也是 Sequence!注意 str 命中 ABC 分支

# 同类型重复注册:后者静默覆盖
@render.register
def _(arg: list):
    return "second list impl"
print(render([1]))                # second list impl,无任何警告

print("registry keys:", sorted(k.__name__ for k in render.registry))
