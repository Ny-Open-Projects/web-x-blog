---
title: [Q2446] x-www-form-urlencoded 手写解析的三个陷阱
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2446 · x-www-form-urlencoded 手写解析的三个陷阱

> 难度:★★☆☆ | 标签:表单, URL 编码, 解析

**问**:手写一个 urlencoded 解析器,加号、无等号的键、重复键分别怎么处理?

**答**:这个编码只有三条规则,但每条都有陷阱。第一,加号即空格:这是 HTML 表单语境的约定,字面加号必须写成 %2B,所以 email=a+b@x.com 解出来是 "a b@x.com",解码要用 unquote_plus 而不是普通 unquote。第二,键可能没有等号(开关型字段),值为空串,但键必须保留;k= 与 k 语义相同,都产出空串值。第三,重复键成列表:同名字段(多选框、多次提交)全部保留在列表里,只取第一个值的业务要显式选择,默默覆盖会丢数据。分隔只用 & 不用分号,分号分隔是历史遗留且已被废弃,解析器支持它反而制造歧义。UTF-8 百分号序列按字节解码,unquote_plus 默认就是 UTF-8。

```python
# file: code/03_Web后端开发/q2446_urlencoded_parser.py
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
```

**追问**:
- 查询串里的加号也是空格吗?——HTML 表单与多数框架的 query 解析沿用同一约定,但 RFC 3986 通用语法里加号是合法字面字符,跨系统传参要显式编码。
- 为什么解析器要保留空值键?——前端用"键存在与否"表达开关,丢掉空值键会把用户的选择变成默认值。
