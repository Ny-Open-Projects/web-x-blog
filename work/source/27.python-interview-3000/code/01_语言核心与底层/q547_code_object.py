import types

def greet(name):
    return f"hello {name}"

def other(name):
    return f"hi {name}"

if __name__ == "__main__":
    code = greet.__code__
    print(type(code).__name__)
    print("varnames:", code.co_varnames)
    print("consts:", code.co_consts)
    print("argcount:", code.co_argcount)

    rebound = types.FunctionType(code, other.__globals__, "greet2")
    print("rebuilt function:", rebound("CPython"))
    print("same code object:", rebound.__code__ is code)
