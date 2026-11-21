"""数组式查询键的解析约定: ids[] 追加式与 ids[0] 下标式(纯标准库)。"""
import re
from urllib.parse import parse_qs

INDEXED = re.compile(r"^(?P<base>[^\[\]]+)\[(?P<idx>\d*)\]$")


def parse_array_keys(qs):
    """把多种数组写法解析成统一视图。

    每个键基名对应一个槽位: plain 收裸键, list 收 ids[] 追加式,
    indexed 收 ids[0] 下标式(稀疏下标原样保留, 填充策略交给调用方)。
    filters[status] 这类字母下标不做嵌套展开, 深嵌套应该改用 JSON 请求体。
    """
    flat = parse_qs(qs, keep_blank_values=True)
    view = {}
    for key, values in flat.items():
        m = INDEXED.match(key)
        if m:
            base, idx = m.group("base"), m.group("idx")
            slot = view.setdefault(base, {"plain": [], "list": [], "indexed": {}})
            if idx == "":
                slot["list"].extend(values)
            else:
                slot["indexed"][int(idx)] = values[0]
        else:
            slot = view.setdefault(key, {"plain": [], "list": [], "indexed": {}})
            slot["plain"].extend(values)
    return view


def contract_check(view):
    """同一个基名混用多种写法视为客户端违约, 服务端应回 400 而不是猜。"""
    return [
        base
        for base, slot in view.items()
        if sum(bool(slot[k]) for k in ("plain", "list", "indexed")) > 1
    ]


v1 = parse_array_keys("ids[]=1&ids[]=2&active=1")
assert v1["ids"]["list"] == ["1", "2"], v1
assert v1["active"]["plain"] == ["1"]
v2 = parse_array_keys("ids[0]=1&ids[2]=3")
assert v2["ids"]["indexed"] == {0: "1", 2: "3"}, v2
v3 = parse_array_keys("ids=1&ids[]=2&ids[5]=9")
assert contract_check(v3) == ["ids"], v3
v4 = parse_array_keys("ids[]=&ids[]=x")
assert v4["ids"]["list"] == ["", "x"], v4  # keep_blank_values 保住空值
print("追加式   ", v1["ids"])
print("下标稀疏 ", v2["ids"]["indexed"])
print("混用违约 ", contract_check(v3))
print("空串保留 ", v4["ids"]["list"])
