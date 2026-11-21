import dis
import types

SRC = """
def hello(name):
    return "hello " + name
"""

if __name__ == "__main__":
    module_code = compile(SRC, "<demo>", "exec")
    print("module co_names:", module_code.co_names)
    nested = [c for c in module_code.co_consts if isinstance(c, types.CodeType)]
    fn_code = nested[0]
    print("nested:", fn_code.co_name, "varnames:", fn_code.co_varnames)

    # eval 模式:表达式编译后可直接求值
    expr = compile("1 + 1", "<expr>", "eval")
    print("eval code result:", eval(expr))

    # 不可变派生:改名换文件名,字节码不动
    renamed = fn_code.replace(co_name="hello2", co_filename="<renamed>")
    ns = {}
    exec(module_code, ns)
    hello = ns["hello"]
    print("before swap:", hello("CPython"))
    hello.__code__ = renamed          # 槽位兼容,可以直接换
    print("after swap :", hello("CPython"), "| co_name:", hello.__code__.co_name)
    print("instruction count:", len(list(dis.get_instructions(renamed))))
