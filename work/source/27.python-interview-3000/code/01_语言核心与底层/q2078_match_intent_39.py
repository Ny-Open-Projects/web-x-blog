"""match 意图的 3.9 等价实现:按形状分发、解包绑定与哨兵。"""
import sys

MISSING = object()                 # 哨兵:区分「没有这个分支」与 None


def dispatch_v39(event):
    """isinstance 判形 + 解包绑定 + 守卫,等价 match/case 意图。"""
    if isinstance(event, dict) and "click" in event:
        x, y = event["click"]      # 对应 case {"click": [x, y]}
        return f"click at {x},{y}"
    if isinstance(event, dict) and "key" in event:
        (key,) = event["key"]      # 对应 case {"key": [key]}
        if key in ("quit", "exit"):    # 对应带 guard 的 case
            return "退出程序"
        return f"key {key}"
    if isinstance(event, list) and event:
        verb, *rest = event        # 对应 case [verb, *rest]
        return f"批量命令 {verb} 参数 {len(rest)} 个"
    return "未识别的事件形状"


if __name__ == "__main__":
    print(dispatch_v39({"click": [3, 4]}))
    print(dispatch_v39({"key": ["quit"]}))
    print(dispatch_v39({"key": ["a"]}))
    print(dispatch_v39(["sync", 1, 2, 3]))
    print(dispatch_v39(123))
    if sys.version_info >= (3, 10):
        print("3.10+ 可直接写 match event: case {...}")
    else:
        print("本机 3.9:上面的 isinstance 加解包就是 match 的等价骨架")
