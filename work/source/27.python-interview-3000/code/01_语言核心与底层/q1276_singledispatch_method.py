from functools import singledispatchmethod


class Renderer:
    @singledispatchmethod
    def render(self, value):
        raise NotImplementedError("no renderer for %r" % (value,))

    @render.register(int)
    def _(self, value):
        return "int:%d" % value

    @render.register(str)
    def _(self, value):
        return "str:%s" % value


if __name__ == "__main__":
    r = Renderer()
    print(r.render(42), "|", r.render("hi"))
    try:
        r.render(1.5)
    except NotImplementedError as e:
        print("fallback:", e)
