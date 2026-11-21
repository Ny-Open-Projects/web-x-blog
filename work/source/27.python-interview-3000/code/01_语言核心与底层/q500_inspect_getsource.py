import inspect

def important_algorithm(x):
    """文档字符串也会被读取"""
    y = x * 2
    return y + 1

class Widget:
    def render(self):
        return "rendered"

if __name__ == "__main__":
    print(inspect.getsource(important_algorithm))
    print("doc:", inspect.getdoc(important_algorithm))
    print("render starts at line:", inspect.getsourcelines(Widget.render)[1])
    print("module:", inspect.getmodule(Widget).__name__)
    print("len source lines:", len(inspect.getsourcelines(Widget)[0]))
