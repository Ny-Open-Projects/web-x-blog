"""Accept 内容协商: q 权重解析、特异度排序与 406 协商失败(纯标准库)。"""


def parse_accept(header):
    """解析 Accept 头, 返回按 q 降序、特异度降序的 [(type, subtype, q)]。

    特异度: type/subtype 高于 type/* 高于 */*; 同 q 下更特异者胜出。
    q=0 表示显式拒绝, 直接丢弃。
    """
    entries = []
    for part in header.split(","):
        part = part.strip()
        if not part:
            continue
        bits = [b.strip() for b in part.split(";")]
        media = bits[0]
        if "/" not in media:
            continue
        atype, asub = media.split("/", 1)
        q = 1.0
        for param in bits[1:]:
            if param.startswith("q="):
                try:
                    q = float(param[2:])
                except ValueError:
                    q = 1.0
        if q > 0:
            specificity = 2 if asub != "*" else (1 if atype != "*" else 0)
            entries.append((atype.lower(), asub.lower(), q, specificity))
    # q 降序, 再按特异度降序; 稳定排序保持原始顺序
    entries.sort(key=lambda e: (-e[2], -e[3]))
    return [(t, s, q) for t, s, q, _ in entries]


def negotiate(accept_header, available):
    """从可用表示中选出 Accept 最想要的; 全不匹配返回 None 由调用方转 406。"""
    prefs = parse_accept(accept_header)
    for atype, asub, q in prefs:
        for mime in available:
            mtype, msub = mime.lower().split("/", 1)
            type_ok = atype == "*" or atype == mtype
            sub_ok = asub == "*" or asub == msub
            if type_ok and sub_ok:
                return mime, q
    return None


AVAILABLE = ["application/json", "text/csv", "text/html"]

cases = [
    ("application/json", "application/json"),
    ("text/html;q=0.9, application/json;q=1.0", "application/json"),
    ("*/*", "application/json"),
    ("text/*", "text/csv"),
    ("application/xml;q=1.0", None),           # 无交集 -> 406
    ("text/html;q=0, application/json", "application/json"),  # q=0 显式拒绝
]
for header, expect in cases:
    result = negotiate(header, AVAILABLE)
    print("Accept: {:45s} -> {}".format(repr(header), result))
    assert (result is None) == (expect is None), header

print("协商失败时返回 406 Not Acceptable, 并在响应中给出可选表示清单")
