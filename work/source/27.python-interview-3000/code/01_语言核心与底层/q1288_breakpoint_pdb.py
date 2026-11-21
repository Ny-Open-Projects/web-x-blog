import bdb
import os


def divide(a, b):
    result = a / b
    return result


if __name__ == "__main__":
    os.environ["PYTHONBREAKPOINT"] = "0"
    print("PYTHONBREAKPOINT =", os.environ["PYTHONBREAKPOINT"])
    breakpoint()                        # 已被环境变量禁用,不会进 pdb
    print("breakpoint() disabled, continuing")

    lines_hit = []

    class Tracer(bdb.Bdb):
        def user_line(self, frame):
            lines_hit.append((frame.f_code.co_name, frame.f_lineno))
            self.set_continue()         # 收集一行即放行到底

    tr = Tracer()
    tr.set_break(divide.__code__.co_filename,
                 divide.__code__.co_firstlineno + 1)
    tr.runcall(divide, 6, 3)
    print("bdb hit lines:", lines_hit)
