"""深嵌套响应的扁平化: 点路径展开与可逆重建(纯标准库)。"""


def flatten(obj, prefix="", sep=".", out=None):
    """嵌套 dict/list 展开成 'a.b.0.c' 形式的单层表, 供 CSV 导出与表格展示。

    空容器没有叶子, 在扁平结果里不可见, 这是往返不可逆的唯一来源。
    """
    if out is None:
        out = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            flatten(v, "%s%s%s" % (prefix, sep, k) if prefix else str(k), sep, out)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            flatten(v, "%s%s%d" % (prefix, sep, i) if prefix else str(i), sep, out)
    else:
        out[prefix] = obj
    return out


def unflatten(flat, sep="."):
    """逆操作: 每层用 __dict__/__list__ 双标记记容器种类, 最后统一剥壳。

    假定路径互不冲突(同一键既是数组又是对象视为脏数据);
    键名本身含 sep 时会歧义, 导出前必须校验键名。
    """
    root = {"__dict__": {}, "__list__": []}
    for path, value in flat.items():
        parts = path.split(sep)
        cur = root
        for i, p in enumerate(parts):
            kind = "__list__" if p.isdigit() else "__dict__"
            key = int(p) if p.isdigit() else p
            last = i == len(parts) - 1
            if kind == "__list__":
                lst = cur[kind]
                while len(lst) <= key:  # 数组按下标补位
                    lst.append(None)
            if last:
                cur[kind][key] = value
            else:
                if kind == "__list__":
                    nxt = cur[kind][key]
                else:
                    nxt = cur[kind].get(key)
                if not isinstance(nxt, dict):
                    nxt = {"__dict__": {}, "__list__": []}
                    cur[kind][key] = nxt
                cur = nxt
    return root


def rebuild(node):
    """剥壳: 非空 __list__ 优先判为数组, 非空 __dict__ 判为对象, 两者都空还原为 {}。"""
    if not isinstance(node, dict) or ("__dict__" not in node and "__list__" not in node):
        return node
    has_list, has_dict = bool(node["__list__"]), bool(node["__dict__"])
    if has_list and has_dict:
        raise ValueError("路径冲突: 同名键既是数组又是对象")
    if has_list:
        return [rebuild(x) for x in node["__list__"]]
    if has_dict:
        return {k: rebuild(v) for k, v in node["__dict__"].items()}
    return {}


src = {
    "order": {"id": "o1", "buyer": {"name": "Ann", "tags": ["vip", "new"]}},
    "items": [{"sku": "A", "qty": 2}, {"sku": "B", "qty": 1}],
    "total": 12.5,
}
flat = flatten(src)
assert flat["order.buyer.tags.1"] == "new" and flat["items.0.sku"] == "A"
assert len(flat) == 9, sorted(flat)
back = rebuild(unflatten(flat))
assert back == src, back
try:
    rebuild(unflatten({"a.0": 1, "a.b": 2}))
except ValueError as e:
    print("脏数据显式报错:", e)
print("展开键示例:", sorted(flat)[:3], "... 共 %d 个叶子, 重建与原结构逐值相等" % len(flat))
