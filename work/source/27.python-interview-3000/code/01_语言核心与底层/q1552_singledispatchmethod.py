from functools import singledispatchmethod


class Renderer:
    @singledispatchmethod
    def render(self, value):
        return "fallback<" + type(value).__name__ + ">"     # object 兜底

    @render.register(int)
    def _(self, value):
        return "int:%+d" % value

    @render.register(list)
    def _(self, value):
        return "list[" + ", ".join(self.render(v) for v in value) + "]"


class FancyRenderer(Renderer):
    @Renderer.render.register(float)
    def _(self, value):              # 子类扩展:登记进父类的 dispatcher
        return "float:%.2f" % value


if __name__ == "__main__":
    r = Renderer()
    print(r.render(42))
    print(r.render(3.14159))
    print(r.render([1, -2, "hi"]))
    print(r.render({"plain": "dict"}))

    f = FancyRenderer()
    print("fancy float        :", f.render(2.71828))
    print("fancy int inherits :", f.render(7))
