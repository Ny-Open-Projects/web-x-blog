"""多列排序参数的语法解析: 白名单校验加方向与上限(纯标准库)。"""

WHITELIST = {"name", "created_at", "price"}
MAX_COLUMNS = 3


class SortParamError(Exception):
    pass


def parse_sort(param):
    """解析 'name,-created_at' 形态; 返回 [(列, 方向)]。"""
    if param is None or param == "":
        return [("created_at", "desc")]
    if len(param) > 128:
        raise SortParamError("排序参数过长")
    seen = []
    for token in param.split(","):
        token = token.strip()
        if not token:
            raise SortParamError("空排序段")
        direction = "asc"
        if token[0] in "+-":
            direction = "desc" if token[0] == "-" else "asc"
            token = token[1:]
        if not token:
            raise SortParamError("纯符号的排序段")
        if token not in WHITELIST:
            raise SortParamError("未知排序字段: " + token)
        if any(t[0] == token for t in seen):
            raise SortParamError("重复排序字段: " + token)
        seen.append((token, direction))
        if len(seen) > MAX_COLUMNS:
            raise SortParamError("最多允许 {} 列".format(MAX_COLUMNS))
    return seen


def to_order_by(parsed):
    return ", ".join("{} {}".format(col, d.upper()) for col, d in parsed)


for raw in [None, "name", "-price", "name,-created_at,price", "name,-created_at,price,rating"]:
    try:
        print("{!r:34s} -> ORDER BY {}".format(raw, to_order_by(parse_sort(raw))))
    except SortParamError as exc:
        print("{!r:34s} -> 400: {}".format(raw, exc))
for bad in ["name,-name", "name;DROP TABLE x", "-", "name,,"]:
    try:
        parse_sort(bad)
        print("漏网!", bad)
    except SortParamError as exc:
        print("{!r:22s} -> 400: {}".format(bad, exc))
print("要点: 语法层管形状, 白名单管合法性, 重复列与列数上限都要显式拒绝")
