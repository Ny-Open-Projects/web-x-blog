import json
from typing import Dict, List, Union

JSON = Union[None, bool, int, float, str,
             List["JSON"], Dict[str, "JSON"]]     # 字符串前向引用,3.9 可用


def validate(obj) -> bool:
    if obj is None or isinstance(obj, (bool, int, float, str)):
        return True
    if isinstance(obj, list):
        return all(validate(x) for x in obj)
    if isinstance(obj, dict):
        return all(isinstance(k, str) and validate(v) for k, v in obj.items())
    return False


if __name__ == "__main__":
    doc = json.loads('{"a": [1, 2.5, null, true], "b": {"c": "text"}}')
    print("valid doc  :", validate(doc))
    print("invalid doc:", validate({1: "x"}))
    print("alias type :", type(JSON).__name__, "| 递归成员可解开")
    if __import__("sys").version_info >= (3, 12):
        print("3.12+: type JSON = ... 一等递归别名语法")
