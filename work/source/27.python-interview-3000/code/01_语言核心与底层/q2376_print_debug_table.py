"""print 调试的表格化:对齐输出让多轮状态一目了然。"""
import os


def dump_vars(stage, **vars):
    """统一的调试快照:一行一个变量,定宽对齐。"""
    print(f"--- {stage} ---")
    for name, value in vars.items():
        print(f"  {name:<10} = {value!r:>28}")


def run_pipeline(nums):
    acc = 0
    out = []
    for i, v in enumerate(nums):
        acc += v
        out.append(acc * 2)
        if i % 2 == 0:            # 节流:只看偶数轮
            dump_vars(f"step{i}", i=i, v=v, acc=acc, out=out)
    return out


if __name__ == "__main__":
    result = run_pipeline([1, 2, 3, 4])
    print("最终:", result)

    DEBUG = os.environ.get("DEBUG")
    x = 42
    if DEBUG:
        print(f"[debug] x={x}")
    print("DEBUG 未设置时 [debug] 行不出现:", DEBUG is None)

    s = "a\tb"
    print("str :", s)
    print("repr:", repr(s))
