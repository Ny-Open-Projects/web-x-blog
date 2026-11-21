import os

try:                                   # 顶层检测一次:标准库 json 一定在
    import json as _fast_json
    HAS_FAST = True
    FAST_REASON = ""
except ImportError as err:             # 实际不会走到:演示结构
    HAS_FAST = False
    FAST_REASON = str(err)

try:                                   # 第三方包:本机大概率没有
    import uvloop as _loop_impl
    HAS_UVLOOP = True
    LOOP_REASON = ""
except ImportError as err:
    HAS_UVLOOP = False
    LOOP_REASON = "%s 未安装: pip install uvloop" % err.name


def pick_loop(force=None):
    """env 可覆盖自动检测:FORCE_UVLOOP=1 或 0。"""
    if force is None:
        force = os.environ.get("FORCE_UVLOOP")
    if force == "1":
        if not HAS_UVLOOP:
            raise RuntimeError("FORCE_UVLOOP=1 但依赖缺失: " + LOOP_REASON)
        return "uvloop"
    if force == "0":
        return "asyncio 默认循环"
    return "uvloop" if HAS_UVLOOP else "asyncio 默认循环"


if __name__ == "__main__":
    print("HAS_FAST:", HAS_FAST, "| HAS_UVLOOP:", HAS_UVLOOP)
    print("auto      :", pick_loop())
    print("forced off:", pick_loop(force="0"))
    try:
        pick_loop(force="1")
    except RuntimeError as err:
        print("forced on :", err)
    print("reason kept:", LOOP_REASON)
