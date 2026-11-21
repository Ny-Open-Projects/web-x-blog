"""RFC 8288 Link 头分页: 头部的生成与解析(纯标准库)。"""
import re

LINK_ITEM = re.compile(r'<([^>]*)>\s*(?:;\s*([^,]+))?')


def build_link(base, page, per_page, total):
    """生成翻页 Link 头: next prev first last 四个 rel, 视页位决定是否出现。"""
    pages = max(1, (total + per_page - 1) // per_page)
    url = lambda p: "{}/items?page={}&per_page={}".format(base, p, per_page)
    rels = []
    if page < pages:
        rels.append('<{}>; rel="next"'.format(url(page + 1)))
    if page > 1:
        rels.append('<{}>; rel="prev"'.format(url(page - 1)))
    rels.append('<{}>; rel="first"'.format(url(1)))
    if pages > 1:
        rels.append('<{}>; rel="last"'.format(url(pages)))
    return ", ".join(rels)


def parse_link(header):
    """解析 Link 头为 [(url, rel)], 参数按分号切分, rel 去引号转小写。"""
    out = []
    for m in LINK_ITEM.finditer(header):
        url, params = m.group(1), m.group(2) or ""
        for kv in params.split(";"):
            kv = kv.strip()
            if kv.lower().startswith("rel="):
                rel = kv[4:].strip().strip('"').lower()
                out.append((url, rel))
    return out


header = build_link("/api/v1", 3, 20, 95)
print("第 3 页的 Link 头:")
print("Link: " + header)
rels = dict((r, u) for u, r in parse_link(header))   # rel -> url
assert rels["next"].endswith("page=4&per_page=20") and rels["prev"].endswith("page=2&per_page=20")
assert rels["first"].endswith("page=1&per_page=20")
if rels.get("last"):
    assert rels["last"].endswith("page=5&per_page=20")
print("解析结果:", {r: u.split("?")[1] for r, u in rels.items()})

last_header = build_link("/api/v1", 5, 20, 95)
print("末页 Link(无 next):", last_header)
assert "next" not in [r for _, r in parse_link(last_header)]

print("对比响应体内嵌翻页元数据: Link 头不占体, 客户端按 rel 取址, 与表示解耦")
