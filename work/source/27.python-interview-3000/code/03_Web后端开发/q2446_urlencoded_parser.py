"""x-www-form-urlencoded 手写解析: 加号 百分号与重复键(纯标准库)。"""
from urllib.parse import unquote_plus


def parse_www_form(body):
    """按 HTML 规范解析: + 是空格, %XX 解码, 无 = 的键值为空串, 重复键成列表。"""
    result = {}
    for pair in body.split("&"):
        if pair == "":
            continue
        key, sep, value = pair.partition("=")
        key = unquote_plus(key)
        value = unquote_plus(value) if sep else ""
        result.setdefault(key, []).append(value)
    return result


def first(parsed, key, default=None):
    """多数业务只关心第一个值, 这里提供取值便捷函数。"""
    values = parsed.get(key)
    return values[0] if values else default


body = "q=1+2%203&kw=%E6%90%9C%E7%B4%A2&empty=&flag&dup=a&dup=b&plus=b%2Bc"
parsed = parse_www_form(body)
for key in parsed:
    print("{:5s} -> {}".format(key, parsed[key]))

assert first(parsed, "q") == "1 2 3"          # + 与 %20 都解码为空格
assert first(parsed, "kw") == "搜索"           # UTF-8 百分号解码
assert first(parsed, "empty") == ""           # k= 与 k 都得到空串
assert first(parsed, "flag") == ""            # 无等号的开关型字段
assert parsed["dup"] == ["a", "b"]            # 重复键保留全部
assert first(parsed, "plus") == "b+c"         # 字面加号必须编码为 %2B

# 陷阱演示: 裸 + 当成字面加号使用会得到空格
assert parse_www_form("email=a+b@x.com")["email"] == ["a b@x.com"]
print("陷阱: email=a+b@x.com 被解析为 a b@x.com, 字面加号必须写成 %2B")
print("要点: 该编码只有三条规则 + 即空格 %XX 解码 重复键成列表; "
      "k= 与 k 语义相同但都应保留键, 分号分隔是历史遗留不应再支持")
