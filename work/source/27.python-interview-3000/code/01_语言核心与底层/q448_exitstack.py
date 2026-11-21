import contextlib
import os
import tempfile

def open_many(paths):
    """打开任意数量文件,把清理权打包移交"""
    stack = contextlib.ExitStack()
    handles = [stack.enter_context(open(p, encoding="utf-8")) for p in paths]
    return stack, handles                 # 所有权随 stack 一起移交

def rollback_demo(paths):
    with contextlib.ExitStack() as stack:
        stack.callback(print, "cleanup 1 runs last")
        stack.callback(print, "cleanup 2 runs first")
        raise RuntimeError("boom")        # 异常时 callback 逆序执行

if __name__ == "__main__":
    tmpdir = tempfile.mkdtemp()
    paths = []
    for i in range(3):
        p = os.path.join(tmpdir, f"f{i}.txt")
        with open(p, "w", encoding="utf-8") as w:
            w.write("line\n" * (i + 1))
        paths.append(p)

    stack, handles = open_many(paths)
    print("total lines:", sum(1 for h in handles for _ in h))
    stack.close()                         # 逆序统一关闭

    try:
        rollback_demo(paths)
    except RuntimeError as e:
        print("caught:", e)
