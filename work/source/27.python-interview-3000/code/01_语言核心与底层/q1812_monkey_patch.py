"""猴子补丁的边界:何时替换、如何留存原实现。"""
import json

_original = json.dumps


def patched_dumps(obj, **kw):
    # 补丁版:补默认参数,其余透传;必须保留原实现的引用以便还原
    kw.setdefault("ensure_ascii", False)
    kw.setdefault("sort_keys", True)
    return _original(obj, **kw)


def apply_patch():
    json.dumps = patched_dumps


def revert_patch():
    json.dumps = _original


if __name__ == "__main__":
    data = {"名字": "服务", "port": 8080}
    print("原版输出:", json.dumps(data)[:26])
    apply_patch()
    print("补丁输出:", json.dumps(data))
    print("补丁仍透传参数:", json.dumps(data, indent=None)[:30])
    revert_patch()
    print("还原后:", json.dumps(data)[:26])
    print("约定:测试 fixture 内打补丁,生产库代码禁止全局替换")
