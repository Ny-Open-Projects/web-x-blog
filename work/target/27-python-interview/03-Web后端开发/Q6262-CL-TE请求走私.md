---
title: "[Q6262] CL.TE 与 TE.CL：前后端解析器不一致如何制造请求走私"
date: 2026-11-25
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6262 · CL.TE 与 TE.CL：前后端解析器不一致如何制造请求走私

难度：P7 ｜ 标签：HTTP、请求走私、CL.TE、Transfer-Encoding、Content-Length、代理

基线：CPython 3.12.2，纯标准库；手写两个最小解析器（按 Content-Length / 按 chunked），对同一段原始请求演示解析结果分叉。

**问**：CDN 在前面做 HTTP/1.1 接入，源站是自研 Python 网关。安全团队用一个同时带 `Content-Length: 6` 和 `Transfer-Encoding: chunked` 的请求打过来，源站把 chunked 的结束符 `0\r\n\r\n` 当成请求体结束，剩下的一段 `GET /admin` 被当成"同一连接上的下一个请求"；CDN 却按 Content-Length 只转了 6 字节。结果一个匿名用户"替"下一个用户发了一个管理员请求，缓存也被污染。为什么两个都"合规"的解析器会分叉？CL.TE 和 TE.CL 分别怎么利用？工程上怎么彻底堵住？

**答**：

- **结论**：HTTP/1.1 的消息边界由 `Content-Length` 或 `Transfer-Encoding: chunked` 决定。如果一条请求同时带这两个头，RFC 9112 要求 **Transfer-Encoding 优先**，并且服务器应当拒绝这种歧义消息（或至少按同一规则归一化）；但很多代理只认 CL、很多源站只认 TE，两边各读各的，就会对"请求在哪里结束"产生不同答案。**CL.TE**：前端按 CL 截断并转发 6 字节，后端按 chunked 解析，`0\r\n\r\n` 之后剩下的字节被后端当作下一个请求（走私）；**TE.CL**：前端按 chunked 解析、后端按 CL 读取，前端认为请求已结束、后端还在等更多 body，下一请求的头部被拼进 body，同样造成错位。利用链通常需要 keep-alive 复用连接，攻击者把"毒请求"留在连接上，让下一个用户的请求接在它后面。
- **取舍**：最稳的修复是**在边缘拒绝歧义**：同时出现 CL 与 TE → 400；多个 CL 且值不同 → 400；TE 的值最终不是 `chunked` → 400/501；不认识的 transfer coding → 拒绝。代价是可能误伤一些老客户端/中间件（它们会同时带两个头但值一致），所以要先统计流量再灰度。另一个方向是"端到端统一"：边缘把 HTTP/1.1 归一化成 HTTP/2 或固定一种 framing，源站只信任边缘注入的内部头；但边缘本身必须正确解析，否则只是把问题前移。不要试图"两个都支持、谁先到用谁"——那正是漏洞。
- **实战**：事故根因是 CDN 配置了"保留客户端 CL"，源站网关在检测到 TE 时优先 chunked，且没有拒绝双头。修复：① 边缘 WAF 增加规则：CL+TE 同时存在直接 400，并记录 `smuggling_attempt`；② 源站入口做同样的校验（纵深防御），不依赖边缘；③ 关闭源站对外的 keep-alive 复用（或限制每连接请求数），降低走私命中下一用户的概率；④ 灰度一周，误伤 0.003%（都是老旧 SDK），加白名单后归零。上线后走私探测请求全部 400。

下面用两个最小解析器对同一段原始请求求解，验证 CL 与 TE 对"请求结束位置"的判断不同，以及"双头即拒绝"的闸门。

```python
# CL.TE: 前端按 Content-Length, 后端按 chunked, 同一请求解析出不同的"剩余字节"
import re


def parse_by_content_length(raw: bytes):
    head, body = raw.split(b"\r\n\r\n", 1)
    match = re.search(rb"Content-Length:\s*(\d+)", head, re.I)
    if not match:
        raise ValueError("missing Content-Length")
    length = int(match.group(1))
    return body[:length], body[length:]


def parse_by_chunked(raw: bytes):
    head, body = raw.split(b"\r\n\r\n", 1)
    if b"transfer-encoding" not in head.lower():
        raise ValueError("missing Transfer-Encoding")
    out = bytearray()
    pos = 0
    while True:
        line_end = body.index(b"\r\n", pos)
        size = int(body[pos:line_end].split(b";")[0], 16)
        pos = line_end + 2
        if size == 0:
            pos += 2                       # 跳过结尾的 CRLF
            break
        out += body[pos:pos + size]
        pos += size + 2                    # 跳过 chunk 数据后的 CRLF
    return bytes(out), body[pos:]


# 毒请求: 声明 CL=6, 同时声明 chunked; body 是 "0\r\n\r\n" + 走私的 GET
smuggled = b"GET /admin HTTP/1.1\r\nHost: internal\r\n\r\n"
body = b"0\r\n\r\n" + smuggled
raw = (
    b"POST /upload HTTP/1.1\r\n"
    b"Host: victim.example\r\n"
    b"Content-Length: 6\r\n"
    b"Transfer-Encoding: chunked\r\n"
    b"\r\n" + body
)

front_body, front_rest = parse_by_content_length(raw)
back_body, back_rest = parse_by_chunked(raw)

print("[1] 前端(CL) body:", front_body, "| 剩余:", front_rest[:20])
print("[2] 后端(TE) body:", back_body, "| 剩余:", back_rest[:20])
assert front_body == b"0\r\n\r\nG"
assert back_body == b""
assert front_rest.startswith(b"ET /admin"), "前端把 G 吃掉了, 剩余从 ET 开始"
assert back_rest.startswith(b"GET /admin"), "后端把整段 GET 留作下一个请求"
assert front_rest != back_rest, "两个解析器对消息边界的判断分叉"


def validate_framing(headers: dict) -> None:
    """RFC 9112 的保守实现: 歧义即拒绝."""
    has_cl = "content-length" in headers
    has_te = "transfer-encoding" in headers
    if has_cl and has_te:
        raise ValueError("400 ambiguous: both Content-Length and Transfer-Encoding")
    if has_te and not headers["transfer-encoding"].lower().endswith("chunked"):
        raise ValueError("400 unsupported transfer coding")
    if has_cl:
        values = {v.strip() for v in headers["content-length"].split(",")}
        if len(values) != 1:
            raise ValueError("400 conflicting Content-Length")


for headers, label in [
    ({"content-length": "6", "transfer-encoding": "chunked"}, "CL+TE"),
    ({"content-length": "6, 7"}, "多个不同 CL"),
    ({"transfer-encoding": "gzip"}, "TE 不是 chunked"),
]:
    try:
        validate_framing(headers)
        raise AssertionError(f"{label} 本应被拒绝")
    except ValueError as exc:
        print(f"[3] {label} ->", exc)

validate_framing({"content-length": "6"})
validate_framing({"transfer-encoding": "chunked"})
print("[4] 单一 framing 通过; 结论: 边缘与源站都要拒绝双头")
```

**追问一**：为什么只在边缘修不够？—— 因为边缘和源站可能对"边缘注入的头"信任不同：如果源站还接受来自内网/其他路径的直连，或者有第二个代理链，边缘的校验就被绕过。纵深防御要求**每个解析 HTTP 的组件**都拒绝歧义 framing，至少源站入口要再校验一次；同时内网服务不应直接暴露。另一个盲点是 HTTP/2 降级到 HTTP/1.1 的网关：降级时重新生成 CL/TE，若实现不严谨也会引入同样的歧义。

**追问二**：`Transfer-Encoding: chunked, gzip` 这种顺序有什么讲究？—— TE 是**按应用顺序**解码的：`chunked, gzip` 表示先 chunked 分帧、再 gzip 解压；`gzip, chunked` 表示先 gzip、再 chunked。服务器如果不支持前面的 coding，应返回 501；如果最后一个 coding 不是 `chunked`，消息边界就不是 chunked，不能用 chunked 解析。很多走私漏洞来自"只看 TE 里有没有 chunked 子串"的实现——必须按逗号拆分、按顺序处理、并拒绝未知 coding。

## 背诵要点

- 同一请求同时带 CL 与 TE 时，RFC 9112 要求 TE 优先且应拒绝歧义；前后端各认一个就会 CL.TE/TE.CL 走私。
- CL.TE：前端按 CL 截断，后端按 chunked 把剩余字节当下一个请求；TE.CL 反之。
- 修复：边缘 + 源站双重拒绝双头/多值 CL/未知 TE，限制 keep-alive 复用，尽量端到端 HTTP/2。

## 复盘追问

- 为什么走私通常要配合 keep-alive？（毒请求的剩余字节要留在连接上，等下一个用户的请求拼上来）
- 只检查 `b"chunked" in transfer_encoding` 有什么问题？（`gzip, chunked` 与 `chunked, gzip` 顺序不同；未知 coding 应拒绝而不是猜）
