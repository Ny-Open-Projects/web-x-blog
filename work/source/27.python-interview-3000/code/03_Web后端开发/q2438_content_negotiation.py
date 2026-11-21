"""Accept 内容协商与多渲染器: HTML 与 JSON 双出口(纯标准库)。"""
import json


def parse_accept(header):
    """解析 Accept 头为 (mime, q) 列表, q 降序稳定排序, 通配在同级靠后。"""
    entries = []
    for part in header.split(","):
        tokens = part.strip().split(";")
        mime = tokens[0].strip().lower()
        if not mime:
            continue
        q = 1.0
        for param in tokens[1:]:
            key, _, value = param.strip().partition("=")
            if key == "q":
                q = float(value)
        entries.append((mime, q))
    entries.sort(key=lambda e: (-e[1], e[0] == "*/*"))
    return entries


def negotiate(accept_header, renderers, default):
    """返回选中的渲染器名; 无可接受类型返回 None, 对应 406。"""
    for mime, q in parse_accept(accept_header):
        if q <= 0:
            continue                                  # q=0 表示明确拒绝
        if mime in renderers:
            return mime
        if mime == "*/*":
            return default
    return None


RENDERERS = {
    "application/json": lambda data: json.dumps(data, ensure_ascii=False).encode(),
    "text/html": lambda data: "<h1>{}</h1><p>{}</p>".format(
        data["title"], data["summary"]).encode(),
}

item = {"title": "周报", "summary": "本周完成了限流中间件"}

for accept in ["text/html", "application/json", "text/html;q=0.8, application/json;q=0.9",
               "*/*", "text/csv", "text/csv;q=0, application/json"]:
    chosen = negotiate(accept, RENDERERS, default="application/json")
    if chosen is None:
        print("{:48s} -> 406 Not Acceptable".format(accept))
        continue
    body = RENDERERS[chosen](item)
    print("{:48s} -> {} | {}".format(accept, chosen, body[:28]))

assert negotiate("text/html", RENDERERS, "application/json") == "text/html"
assert negotiate("application/json", RENDERERS, "text/html") == "application/json"
assert negotiate("*/*", RENDERERS, "application/json") == "application/json"
assert negotiate("text/csv", RENDERERS, "application/json") is None
assert negotiate("text/csv;q=0, application/json", RENDERERS, "application/json") == "application/json"
print("要点: 协商按 q 值降序匹配, q=0 是明确拒绝, 通配符是兜底; "
      "匹配失败回 406 并附 Accept-Post 之类的可用类型提示")
