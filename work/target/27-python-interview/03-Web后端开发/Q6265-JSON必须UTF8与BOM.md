---
title: "[Q6265] JSON 必须是 UTF-8：BOM、UTF-16 自动探测与 415 闸门"
date: 2026-11-25
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6265 · JSON 必须是 UTF-8：BOM、UTF-16 自动探测与 415 闸门

难度：P6 ｜ 标签：JSON、UTF-8、charset、BOM、415、surrogate、WAF

基线：CPython 3.12.2，纯标准库；用 `json.loads` 的 bytes/str 两种入口、BOM 与 UTF-16 编码实测自动探测行为。

**问**：WAF 规则按 UTF-8 解析请求体，看到的是正常的 `{"action":"query"}`；源站把 body 直接交给 `json.loads(bytes)`，Python 自动探测出 UTF-16 并解出一个完全不同的对象，攻击者用 UTF-16 绕过了关键词检测。另一个客户端在 JSON 前加了 UTF-8 BOM，服务端先 `body.decode("utf-8")` 再 `json.loads`，直接 500（`Unexpected UTF-8 BOM`）。还有一条请求带 `Content-Type: application/json; charset=utf-16`，服务端照单全收。JSON 到底允许哪些编码？`json.loads` 为什么会"猜"编码？严格入口应该怎么卡？

**答**：

- **结论**：RFC 8259 规定：交换中的 JSON 文本**必须用 UTF-8 编码**，`application/json` 没有定义 `charset` 参数；实现可以忽略 BOM，但不能把 BOM 当成内容。Python 的 `json.loads(bytes)` 会调用 `detect_encoding`：先看 UTF-8/16/32 BOM，再看前 4 字节的 NUL 分布，自动选择 UTF-8/16/32——这是为了兼容本地文件，**不适合不可信网络输入**，因为 WAF 和源站可能对同一段字节得出不同解码结果（解析器差异就是绕过面）。`body.decode("utf-8")` 不会去掉 BOM，BOM 变成 `\ufeff`，`json.loads` 会报 `Unexpected UTF-8 BOM`。正确入口是：校验媒体类型（`application/json` 或以 `+json` 结尾）→ `charset` 只接受 UTF-8（缺省也按 UTF-8）→ 去掉 UTF-8 BOM → 拒绝前 4 字节含 NUL 的 UTF-16/32 启发式 → 严格 UTF-8 解码 → 再 `json.loads(str)`。
- **取舍**：严格 415 会误伤少量老客户端（它们发 `charset=utf-8`，这个应放行；发 UTF-16 的极罕见），但能保证"WAF 与应用看到同一份字节"。另一个取舍是 BOM：RFC 允许忽略，浏览器 `fetch` 不会加 BOM，但某些 Windows 工具会；建议**剥掉 UTF-8 BOM 后接受**，而不是 400，减少无谓故障。JSON 里的孤立代理对（`"\ud800"`）语法上能被 Python 接受，但编码成 UTF-8 会抛 `UnicodeEncodeError`；如果不校验，错误会延迟到写数据库/序列化响应时变成 500，应该在入口就转 400。
- **实战**：事故是 WAF 与源站解码不一致：攻击者把 `"select"` 写成 UTF-16，WAF 按 UTF-8 看不到关键词，源站 `json.loads(bytes)` 正确解出并执行。修复：① 入口强制 `Content-Type` 为 JSON、`charset` 只允许 utf-8；② 拒绝 UTF-16/32（BOM 或 NUL 启发式）；③ 剥离 UTF-8 BOM；④ 递归检查字符串里没有孤立代理对；⑤ WAF 与源站共用同一个规范化函数（同一份代码/规则）。上线后 UTF-16 绕过尝试全部 415，BOM 导致的 500 归零。

下面验证 `json.loads(bytes)` 的自动探测、`decode("utf-8")` 对 BOM 的失败、严格入口对 UTF-16/非法 UTF-8/孤立代理对的 415/400。

```python
# JSON 入口: 只接受 UTF-8, 剥 BOM, 拒绝 UTF-16/32 与孤立代理对
import codecs
import json


class HTTPError(Exception):
    def __init__(self, status, message):
        super().__init__(message)
        self.status = status


def parse_content_type(value):
    parts = [p.strip() for p in value.split(";")]
    media = parts[0].lower()
    params = {}
    for part in parts[1:]:
        key, _, val = part.partition("=")
        params[key.strip().lower()] = val.strip().strip('"')
    return media, params


def check_strings(obj):
    if isinstance(obj, str):
        try:
            obj.encode("utf-8")
        except UnicodeEncodeError as exc:
            raise HTTPError(400, f"invalid unicode: {exc.reason}") from exc
    elif isinstance(obj, dict):
        for key, value in obj.items():
            check_strings(key)
            check_strings(value)
    elif isinstance(obj, list):
        for item in obj:
            check_strings(item)


def parse_json(content_type, body):
    media, params = parse_content_type(content_type)
    if media != "application/json" and not media.endswith("+json"):
        raise HTTPError(415, f"unsupported media type: {media}")
    charset = params.get("charset", "utf-8").lower()
    if charset not in ("utf-8", "utf8"):
        raise HTTPError(415, f"unsupported charset: {charset}")

    if body.startswith(codecs.BOM_UTF8):
        body = body[len(codecs.BOM_UTF8):]
    if b"\x00" in body[:4]:
        raise HTTPError(415, "UTF-16/32 JSON is not allowed")

    try:
        text = body.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise HTTPError(400, f"invalid utf-8: {exc.reason}") from exc

    try:
        obj = json.loads(text)
    except json.JSONDecodeError as exc:
        raise HTTPError(400, f"invalid json: {exc.msg}") from exc

    check_strings(obj)
    return obj


# 1) 正常 UTF-8
print("[1]", parse_json("application/json", '{"a":1}'.encode("utf-8")))
assert parse_json("application/json", '{"a":1}'.encode()) == {"a": 1}

# 2) charset=utf-8 放行, 其他 415
assert parse_json('application/json; charset="UTF-8"', b'{"a":1}') == {"a": 1}
for ct in ("application/json; charset=utf-16", "text/plain"):
    try:
        parse_json(ct, b'{"a":1}')
        raise AssertionError(f"{ct} 应被拒绝")
    except HTTPError as exc:
        print(f"[2] {ct} -> {exc.status}")

# 3) json.loads(bytes) 会自动识别 UTF-16; 严格入口拒绝
utf16 = '{"a":1}'.encode("utf-16")
print("[3] json.loads(bytes) 自动探测:", json.loads(utf16))
assert json.loads(utf16) == {"a": 1}
try:
    parse_json("application/json", utf16)
    raise AssertionError("UTF-16 应被 415")
except HTTPError as exc:
    print("[4] 入口拒绝 UTF-16 ->", exc.status, exc)

# 4) UTF-8 BOM: bytes 入口能接受, 但先 decode('utf-8') 会失败
bom_body = codecs.BOM_UTF8 + b'{"a":1}'
assert json.loads(bom_body) == {"a": 1}
try:
    json.loads(bom_body.decode("utf-8"))
    raise AssertionError("带 BOM 的 str 不应被接受")
except json.JSONDecodeError as exc:
    print("[5] decode 后再 loads ->", exc.msg)
assert parse_json("application/json", bom_body) == {"a": 1}
print("[6] 严格入口剥离 BOM 后接受")

# 5) 非法 UTF-8 -> 400
try:
    parse_json("application/json", b'{"a":"\xff"}')
    raise AssertionError("非法 UTF-8 应 400")
except HTTPError as exc:
    print("[7] 非法 UTF-8 ->", exc.status)

# 6) 孤立代理对: 语法能过, 编码 UTF-8 失败, 入口转 400
lone = json.loads('"\\ud800"')
print("[8] 孤立代理对:", repr(lone))
try:
    lone.encode("utf-8")
except UnicodeEncodeError:
    print("    编码 UTF-8 -> UnicodeEncodeError")
try:
    parse_json("application/json", b'"\\ud800"')
    raise AssertionError("孤立代理对应 400")
except HTTPError as exc:
    print("[9] 入口拒绝孤立代理对 ->", exc.status)

# 7) +json 后缀放行
assert parse_json("application/vnd.api+json", b'{"data":[]}') == {"data": []}
print("[10] application/*+json 放行")
```

**追问一**：为什么不能直接依赖 `json.loads(bytes)` 的 BOM 探测？—— 因为它的探测规则（BOM + NUL 分布）是"尽力猜"，同一段字节在不同实现（WAF、网关、其他语言）里可能被解成不同结果；安全边界上，"两个组件看到不同内容"就是绕过。网络入口应该只允许一种编码（UTF-8），把多编码兼容留给离线文件导入；如果必须支持 UTF-16，要在最外层统一转码，并让所有下游只看到 UTF-8。

**追问二**：`Content-Type: application/json; charset=utf-8` 到底合不合法？—— RFC 8259 没有为 `application/json` 定义 `charset` 参数，严格说带了也无意义；但现实中大量客户端会带，服务端应当**接受 utf-8/utf8（大小写不敏感）**，拒绝其他值。不要因为"规范没定义"就 415 掉 `charset=utf-8`，那会制造无谓的兼容问题；真正的闸门是"实际字节必须是 UTF-8"。

## 背诵要点

- RFC 8259 要求 JSON 用 UTF-8；`application/json` 没有 charset 参数，但应放行 `charset=utf-8`。
- `json.loads(bytes)` 会按 BOM/NUL 自动探测 UTF-8/16/32，不适合不可信输入；`decode("utf-8")` 不去 BOM，会报 `Unexpected UTF-8 BOM`。
- 入口顺序：媒体类型 → charset → 剥 UTF-8 BOM → 拒绝 NUL/UTF-16 → 严格 UTF-8 → 拒绝孤立代理对（400 而非 500）。

## 复盘追问

- 为什么 UTF-16 请求能绕过只按 UTF-8 做关键词匹配的 WAF？（WAF 与源站对同一字节串解码结果不同，属于解析器差异）
- 孤立代理对应该在入口拦还是等落库报错？（入口 400 可控；落库/序列化时才炸会变 500，且可能污染数据）
