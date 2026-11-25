---
title: "[Q6261] WSGI 响应头的多值语义：Set-Cookie 被 dict 吞掉的那一条"
date: 2026-11-25
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6261 · WSGI 响应头的多值语义：Set-Cookie 被 dict 吞掉的那一条

难度：P6 ｜ 标签：WSGI、PEP 3333、Set-Cookie、响应头、Headers、中间件

基线：CPython 3.12.2，纯标准库；用 `wsgiref.validate` 校验一个返回两个 `Set-Cookie` 的 WSGI app，再对比 `dict(headers)` 与 `Headers.get_all`。

**问**：登录接口同时下发 `sid`（会话）和 `theme`（主题）两个 Cookie。直连服务时一切正常；接了一个"统一响应头处理"的中间件后，用户登录成功却立刻掉线。抓包发现响应里只有一个 `Set-Cookie: theme=dark`，`sid` 不见了。中间件代码只有一行 `headers = dict(headers)`，它只是想"方便查找"。WSGI 的响应头为什么允许重复？为什么 `dict` 会吞掉一条？中间件应该怎么写？

**答**：

- **结论**：PEP 3333 规定 WSGI 响应头是**由 `(name, value)` 二元组组成的列表**，不是字典；同名头可以出现多次，`Set-Cookie` 是最典型的例子（每个 Cookie 一条）。`dict(headers)` 会把同名键覆盖，只保留最后一条，于是 `sid` 被 `theme` 覆盖。正确做法是用 `wsgiref.headers.Headers`：`get_all(name)` 返回所有同名值，`add_header(name, value)` 追加而不是覆盖；需要交给下游时保留 list，不要转 dict。WSGI 还有一个类型约束：header 的 name/value 必须是**原生 `str`**，值里只能放 latin-1 可编码的字符，非 ASCII 要用 RFC 5987/8187 编码，不能直接塞 UTF-8。
- **取舍**：有些框架/中间件 API 确实用 `Mapping[str, str]` 表示头，因为大多数头是单值的；但一旦涉及 `Set-Cookie`、`Warning`、`Link`、`Via` 这些可重复头，就必须用"多值容器"。设计中间件时，内部可以用 `list[tuple[str, str]]` 或 `Headers`，对外暴露 `get_all`；如果非要用 dict，值类型应该是 `list[str]`，并且明确哪些头允许合并（如 `Vary` 用逗号合并、`Set-Cookie` **不能**用逗号合并，因为 Expires 里本身有逗号）。另一个取舍是性能：`Headers` 每次查找是线性扫描，头数量通常 <30，可忽略；为了一点查找速度把语义丢掉不值得。
- **实战**：事故中间件在 `process_response` 里 `dict(response.headers)`，再统一 `response.headers = {...}`，所有多值头被压成一条。修复：① 中间件内部改用 `Headers(response.headers)`，只在需要判断时 `get_all`；② 透传时保留原始 list，不做 dict 转换；③ 加一条集成测试：登录响应必须包含两条 `Set-Cookie`，且 `sid` 的 `HttpOnly` 存在。上线后掉线投诉归零，后续接入的 `Warning` 头也不再丢。

下面用 `wsgiref.validate` 验证"两条 Set-Cookie 是合法的 PEP 3333 响应"，再对比 `dict` 与 `Headers` 的行为。

```python
# WSGI 响应头是 list[tuple], 同名头可重复; dict() 会覆盖
import warnings
from wsgiref.headers import Headers
from wsgiref.util import setup_testing_defaults
from wsgiref.validate import validator


def app(environ, start_response):
    headers = [
        ("Content-Type", "text/plain; charset=utf-8"),
        ("Set-Cookie", "sid=abc123; Path=/; HttpOnly; SameSite=Lax"),
        ("Set-Cookie", "theme=dark; Path=/; Max-Age=31536000"),
    ]
    start_response("200 OK", headers)
    return [b"ok"]


captured = {}


def start_response(status, headers, exc_info=None):
    captured["status"] = status
    captured["headers"] = headers


environ = {}
setup_testing_defaults(environ)
environ["QUERY_STRING"] = ""

# 1) wsgiref.validate 认可重复 Set-Cookie
with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always")
    iterator = validator(app)(environ, start_response)
    body = b"".join(iterator)
    iterator.close()

print("[1] 校验告警数:", len(caught), "| body:", body)
assert body == b"ok"
assert caught == [], "合法的重复 Set-Cookie 不应触发 PEP 3333 告警"
assert len(captured["headers"]) == 3

# 2) dict() 只保留最后一条
naive = dict(captured["headers"])
print("[2] dict 后的 Set-Cookie:", naive["Set-Cookie"])
assert naive["Set-Cookie"].startswith("theme="), "sid 被覆盖"
assert "sid" not in naive["Set-Cookie"]

# 3) Headers 保留全部
headers = Headers(captured["headers"])
cookies = headers.get_all("Set-Cookie")
print("[3] get_all:", cookies)
assert len(cookies) == 2
assert any(item.startswith("sid=") for item in cookies)
assert any(item.startswith("theme=") for item in cookies)

# 4) add_header 追加, 不是覆盖
headers.add_header("Set-Cookie", "locale=zh-CN; Path=/")
print("[4] add 后数量:", len(headers.get_all("Set-Cookie")))
assert len(headers.get_all("Set-Cookie")) == 3

print("[5] 结论: 透传用 list/Headers, 不要 dict(headers)")
```

**追问一**：`Set-Cookie` 能不能像 `Vary` 一样用逗号合并成一条？—— 不能。`Expires` 属性的日期本身包含逗号（`Wed, 21 Oct 2026 07:28:00 GMT`），合并后解析器无法区分"下一个 Cookie"和"日期里的逗号"；RFC 6265 明确要求每个 Cookie 一条 `Set-Cookie`。`Vary`、`Cache-Control` 这类头可以按规范合并，但也不要由中间件随意合并，最好保留原样，让客户端/缓存自己处理。

**追问二**：WSGI 头的值为什么必须是 latin-1 的 `str`，不能直接放中文？—— PEP 3333 为了兼容 Python 2 时代的字节语义，规定 value 是"可 latin-1 编码的 str"；服务器最终按 latin-1 转回字节写出。中文文件名、非 ASCII 的 `Location` 参数必须用百分号编码或 RFC 5987 的 `filename*=UTF-8''...`。直接放中文会在服务器编码阶段抛 `UnicodeEncodeError`，或者被截断成乱码；ASGI 没有这个限制（headers 是 bytes），但同样要遵守 HTTP 的字节语义。

## 背诵要点

- WSGI 响应头是 `list[tuple[str, str]]`，同名头可重复；`dict(headers)` 会覆盖，`Set-Cookie` 必须逐条保留。
- 用 `wsgiref.headers.Headers` 的 `get_all`/`add_header`；`Set-Cookie` 不能用逗号合并（Expires 含逗号）。
- WSGI header 值必须 latin-1 可编码，非 ASCII 用百分号编码或 RFC 5987/8187。

## 复盘追问

- 为什么 `dict(headers)` 在大多数接口上没出问题，登录接口却掉线？（只有多值头会丢，`Set-Cookie` 恰好是登录必需）
- 中间件要"查某个头是否存在"时，怎么在不破坏多值语义的前提下实现？（用 `Headers.get_all` 或 `any(name.lower()==...)`，不要转 dict）
