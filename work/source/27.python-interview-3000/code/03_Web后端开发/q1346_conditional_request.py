"""条件请求:If-None-Match 的解析与 304 判定(纯标准库)。"""


def parse_if_none_match(value):
    """解析 If-None-Match,返回 [(weak: bool, tag: str)];* 表示任意实体。"""
    if not value:
        return []
    value = value.strip()
    if value == "*":
        return [(False, "*")]
    tags = []
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        weak = part.startswith("W/")
        if weak:
            part = part[2:]
        tags.append((weak, part.strip()))
    return tags


def not_modified(etag, if_none_match):
    """按 RFC 7232 的弱比较判定:命中返回 True,服务端应回 304。"""
    tags = parse_if_none_match(if_none_match)
    if not tags:
        return False
    if any(tag == "*" for _, tag in tags):
        return True
    ours = etag[2:] if etag.startswith("W/") else etag
    return any(tag == ours for _, tag in tags)


resource_etag = '"v7"'
print("单标签命中:", not_modified(resource_etag, '"v7"'))
print("多标签命中:", not_modified(resource_etag, '"v6", "v7"'))
print("星号命中:", not_modified(resource_etag, "*"))
print("弱标签命中:", not_modified(resource_etag, 'W/"v7"'))
print("不命中:", not_modified(resource_etag, '"v8"'))
print("空头不命中:", not_modified(resource_etag, None))
