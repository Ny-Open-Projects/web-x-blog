"""RFC 6902 JSON Patch 最小实现: test 断言与整体原子性(纯标准库)。"""
from copy import deepcopy


def resolve(doc, pointer):
    """返回 pointer 的父容器与末段 token; 根指针返回 (doc, None)。"""
    if pointer == "":
        return doc, None
    parts = [p.replace("~1", "/").replace("~0", "~") for p in pointer.lstrip("/").split("/")]
    parent = doc
    for token in parts[:-1]:
        parent = parent[int(token)] if isinstance(parent, list) else parent[token]
    return parent, parts[-1]


def get_by_pointer(doc, pointer):
    parent, last = resolve(doc, pointer)
    if last is None:
        return doc
    return parent[int(last)] if isinstance(parent, list) else parent[last]


def apply_json_patch(doc, ops):
    """按序应用操作; 任一步失败则整体拒绝, 不产生半成品文档。"""
    result = deepcopy(doc)
    for op in ops:
        action = op["op"]
        parent, last = resolve(result, op["path"])
        if action == "add":
            if isinstance(parent, list):
                parent.insert(min(int(last), len(parent)), op["value"])
            else:
                parent[last] = op["value"]
        elif action == "replace":
            if isinstance(parent, list):
                parent[int(last)] = op["value"]
            elif last not in parent:
                raise KeyError("replace 目标不存在: " + op["path"])
            else:
                parent[last] = op["value"]
        elif action == "remove":
            if isinstance(parent, list):
                parent.pop(int(last))
            else:
                del parent[last]
        elif action == "test":
            if get_by_pointer(result, op["path"]) != op["value"]:
                raise ValueError("test 断言失败: " + op["path"])
        else:
            raise ValueError("不支持的 op: " + action)
    return result


doc = {"user": {"name": "Ann", "age": 30}, "tags": ["x", "y"]}
ops = [
    {"op": "test", "path": "/user/name", "value": "Ann"},
    {"op": "replace", "path": "/user/age", "value": 31},
    {"op": "add", "path": "/user/city", "value": "SH"},
    {"op": "remove", "path": "/tags/0"},
]
print("JSON Patch 结果:", apply_json_patch(doc, ops))

bad = [{"op": "test", "path": "/user/name", "value": "Bob"},
       {"op": "replace", "path": "/user/age", "value": 99}]
try:
    apply_json_patch(doc, bad)
except ValueError as exc:
    print("test 失败整体拒绝:", exc, "| 原文档 age 未动:", doc["user"]["age"] == 30)
print("要点: Merge Patch 表达我要的样子, JSON Patch 表达请执行这些步骤; test 前置断言与操作级精确性是它的价值")
