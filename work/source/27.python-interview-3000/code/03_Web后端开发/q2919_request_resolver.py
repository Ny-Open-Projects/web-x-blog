"""统一的请求解析器: 头/查询串/请求体三源取值, 显式优先级与出处记录(纯标准库)。"""
from urllib.parse import parse_qs


class Unresolvable(Exception):
    """取值存在但无法转型, 在真实端点中应映射为 400。"""


class Request:
    """把三源收敛成一个取值入口: get 按显式顺序找第一个非空值并记录出处。"""

    def __init__(self, method="GET", path="/", headers=None, query="", body=None):
        self.method = method
        self.path = path
        self.headers = {k.lower(): v for k, v in (headers or {}).items()}
        self.query = parse_qs(query, keep_blank_values=True)
        self.body = body if isinstance(body, dict) else {}

    def get(self, name, default=None, sources=("body", "query", "header"), cast=None):
        """按 sources 顺序取第一个非空值, 返回 (值, 出处); 三源皆无给 default 与 None。"""
        for source in sources:
            raw, found = self._raw(name, source)
            if not found:
                continue
            return self._coerce(name, raw, cast, source), source
        return default, None

    def _raw(self, name, source):
        if source == "body":
            if name in self.body and self.body[name] not in (None, ""):
                return self.body[name], True
        elif source == "query":
            values = self.query.get(name)
            if values and values[0] != "":
                return values[0], True
        elif source == "header":
            raw = self.headers.get(name.lower())
            if raw not in (None, ""):
                return raw, True
        return None, False

    @staticmethod
    def _coerce(name, value, cast, source):
        if cast is None:
            return value
        try:
            return cast(value)
        except (TypeError, ValueError):
            raise Unresolvable("%r 在 %s 中无法转为 %s" % (name, source, cast.__name__))


req = Request(
    method="POST", path="/search",
    headers={"X-Trace-Id": "t-123", "Accept": "application/json"},
    query="page=2&page=3&q=web",
    body={"page": 9, "q": "python"},
)

page, src = req.get("page", cast=int)
print("page=%s 来自 %s, body 优先于 query" % (page, src))
assert (page, src) == (9, "body")

q, src = req.get("q")
print("q=%s 来自 %s" % (q, src))
assert (q, src) == ("python", "body")

trace, src = req.get("X-Trace-Id", sources=("header",))
print("trace=%s 只在头里, 显式声明单源" % trace)
assert (trace, src) == ("t-123", "header")

limit, src = req.get("limit", default=20, sources=("query", "body"))
print("limit 缺省 -> 默认值 %s, 出处 %s" % (limit, src))
assert (limit, src) == (20, None)

n1 = req.get("page", sources=("query",), cast=int)[0]
print("强制 query 源可拿到重复键首值:", n1)
assert n1 == 2

try:
    Request(query="page=abc").get("page", sources=("query",), cast=int)
except Unresolvable as e:
    print("转型失败 -> 400 语义:", e)

# 空串与缺失同权: keep_blank_values 解析出的空值不当作有值
empty, src = req.get("", sources=("header",))
print("空名取值 ->", empty, src)
assert empty is None and src is None
print("三源解析器演示通过")
