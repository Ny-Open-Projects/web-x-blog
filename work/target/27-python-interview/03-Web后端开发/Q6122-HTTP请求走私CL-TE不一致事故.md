---
title: [Q6122] HTTP 请求走私（CL-TE 不一致）事故复盘
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6122 · HTTP 请求走私：CL 与 TE 不一致的解析分歧事故

> 难度:★★★★★ | 标签:事故复盘, HTTP, 安全

**问**:前端代理和后端 Python 应用对"一个请求体有多长"判断不一致会怎样？CL-TE 与 TE-CL 走私分别怎么构造？为什么说根因是"边界解析没有唯一事实源"？Python 侧能做什么防线？

**答**:结论：请求走私的本质是**前后两级解析器对 body 边界各执一词**。规范（RFC 9110）说：同时有 `Content-Length` 与 `Transfer-Encoding: chunked` 时 TE 优先、且两者矛盾要拒绝（或至少 CL 与多个 CL 头不一致必须拒绝）。走私两类：a) **CL-TE**（前端信 CL、后端信 TE）：攻击者发 `Content-Length: 13` + chunked body，前端认为"13 字节完事"，把后续字节留在管道里；后端按 chunk 解析，把残留字节拼成**第二个请求**——恰好是攻击者的私货（如 `/admin` 删除请求），借他人连接绕过前端 ACL；b) **TE-CL** 反向同理。事故形态通常是：偶发的 400、"别人的身份出现在我的请求里"、ACL 后的接口被未知来源调用。Python 侧防线：a) 应用前**只留一级可信解析器**——uvicorn/gunicorn 直收或代理做"规范化转发"（重写请求头消除歧义）；b) 中间件对同时出现 CL+TE 或重复 CL 的请求直接 400（示例代码）；c) 升级代理与 ASGI 服务器以获得最新的解析加固（如 h11 对重复/矛盾头的严格校验）。

```python
# 基线: 纯标准库模拟两级解析器的边界分歧（无网络，纯逻辑演示）

def frontend_parse(headers, body):
    """前端代理: CL 优先（旧版 nginx 行为, 用于演示分歧）。"""
    cl = int(headers.get("content-length", 0))
    return body[:cl], body[cl:]           # (本次请求体, 管道残留)

def backend_parse(headers, body):
    """后端应用: TE 优先（RFC 9110 要求）。"""
    if "chunked" in headers.get("transfer-encoding", ""):
        out, rest = b"", b""
        buf = body
        while True:
            line, _, buf = buf.partition(b"\r\n")
            size = int(line.split(b";")[0], 16)
            if size == 0:
                rest = buf                # 0-chunk 之后仍有数据 -> 后端视为'下一个请求'
                break
            out += buf[:size]; buf = buf[size + 2:]   # 跳过 chunk 的 \r\n
        return out, rest
    cl = int(headers.get("content-length", 0))
    return body[:cl], body[cl:]

# ---- 攻击请求: 前端信 CL=13, 后端信 TE -> 第二个请求被走私 ----
headers = {"content-length": "13", "transfer-encoding": "chunked"}
body = (b"1\r\n"                       # chunk 大小 1
        b"G\r\n"                       # 1 字节: 'G'
        b"0\r\n"                       # 终止块
        b"POST /admin/delete HTTP/1.1\r\n"   # <- 走私载荷, 前端认为这是残留字节
        b"Host: intra\r\n\r\n")

front_body, residue = frontend_parse(headers, body)
back_body, rest = backend_parse(headers, body)
print("前端认为的请求体:", front_body, "| 残留:", residue)
print("后端认为的请求体:", back_body, "| 剩余:", rest[:40], "... -> 被解析为第二个请求")

# ---- 防线: 应用层中间件对矛盾头直接 400 ----
def smuggling_guard(headers) -> str | None:
    if "transfer-encoding" in headers and "content-length" in headers:
        return "CL+TE 同时出现: 拒绝"
    if headers.get("content-length", "").count(",") or \
       isinstance(headers.get("content-length"), list):
        return "重复/歧义 CL: 拒绝"
    return None

for h in (headers, {"content-length": "10"},
          {"content-length": ["10", "20"]},          # 某些 ASGI 层重复头会变 list
          {"content-length": "10, 20"}):
    verdict = smuggling_guard(h)
    print(f"{str(h)[:45]:47s} -> {verdict or '放行'}")
```

**追问一层**:为什么 HTTP/2 前端会"消除"这类走私？（h2 有帧化的真实长度，代理把 h2 转成 h1 时若**原样透传**攻击者的 CL/TE 头会复活走私——所以必须由代理重建头，即 h2.descync 防线）。
**追问二层**:走私怎么被用于绕过鉴权而不被日志发现？（走私请求寄生在受害者连接上，前端访问日志只记"一个正常请求"；需要后端连接级日志 + 前后端请求数对账才能发现）。
**追问三层**:给出可上线的检测组合拳。（定时探测：自造歧义请求看是否 400；指标：前后端请求计数差；加固：代理规范化转发 + 应用 400 门禁 + 服务器升级）。

## 背诵要点
- 走私根因 = 前后端对 body 边界解析不一致；RFC 9110：CL+TE 并存 TE 优先、矛盾即拒绝。
- CL-TE/TE-CL 两类：残留字节被后端拼成第二个请求，绕过前端 ACL 与日志。
- 防线三层：代理规范化转发、应用对 CL+TE/歧义 CL 直接 400、升级 h11/uvicorn 解析加固。

## 复盘追问
- 生产出现"后端收到未知来源的管理请求"，请设计前后端请求对账与歧义头探测方案。
- 为什么"信任前端已经做了 WAF"不构成防线？从解析分歧的层位角度说明。
