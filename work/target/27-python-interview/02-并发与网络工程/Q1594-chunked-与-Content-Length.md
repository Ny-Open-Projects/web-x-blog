---
title: [Q1594] chunked 与 Content-Length 歧义:走私风险
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1594 · chunked 与 Content-Length 歧义:走私风险

> 难度:★★★★ | 标签:HTTP, 请求走私, 解析器

**问**:一个请求同时带 Content-Length 和 Transfer-Encoding: chunked 会发生什么?为什么这是安全漏洞?

**答**:HTTP 规范说 TE 优先,且二者并存本身就该 400 拒绝。漏洞出在多级解析:前端网关按 CL 认为体只有前 8 字节,后端按 TE 把同样的字节流解析成块 abc 加终止块加下一个请求——被 CL 当作体的字节,在 TE 眼里是一个全新的走私请求(比如 GET /admin)。攻击者把恶意请求夹在 body 里,绕过前端的 ACL、WAF 与日志。防线:网关对 CL 与 TE 并存、重复 CL、非 chunked 的 TE 一律拒绝;规范化后只转发一种解释;内部各组件的解析器语义必须对齐。

```python
# file: code/02_并发与网络工程/q1594_chunked_smuggling.py
"""chunked 与 Content-Length 的歧义: 解析优先级与走私风险。

HTTP 规范说: TE 与 CL 并存时以 TE 为准, 且二者并存本身就该拒绝。
若前端网关信 CL、后端信 TE, 两边对"报文体到哪结束"理解不同,
夹带在 body 里的字节就会被后端当成一个全新请求 —— 请求走私。
本演示在同一报文上跑三种解析器, 只做字节级分析, 不发真实攻击。
"""
RAW = (b"POST /checkout HTTP/1.1\r\n"
       b"Host: shop.local\r\n"
       b"Content-Length: 8\r\n"
       b"Transfer-Encoding: chunked\r\n"
       b"\r\n"
       b"3\r\nabc\r\n0\r\n\r\n"
       b"GET /admin HTTP/1.1\r\nHost: shop.local\r\n\r\n")

NORMAL = (b"POST /save HTTP/1.1\r\n"
          b"Host: shop.local\r\n"
          b"Transfer-Encoding: chunked\r\n"
          b"\r\n"
          b"4\r\nWiki\r\n5\r\npedia\r\n0\r\nX-Check: 1\r\n\r\n")


def split_head(raw):
    head, _, rest = raw.partition(b"\r\n\r\n")
    lines = head.split(b"\r\n")
    headers = {}
    for ln in lines[1:]:
        k, _, v = ln.partition(b":")
        headers[k.strip().lower().decode()] = v.strip().decode()
    return headers, rest


def parse_by_content_length(headers, rest):
    n = int(headers["content-length"])
    return rest[:n], rest[n:]


def parse_by_chunked(rest, allow_trailer=False):
    body = bytearray()
    i = 0
    trailer = b""
    while True:
        j = rest.index(b"\r\n", i)
        size = int(rest[i:j].split(b";")[0], 16)
        i = j + 2
        if size == 0:
            if allow_trailer and rest[i:i + 2] != b"\r\n":
                end = rest.index(b"\r\n\r\n", i)
                trailer = rest[i:end]
                i = end + 4
            else:
                i += 2                      # 终止块的收尾 CRLF
            break
        body += rest[i:i + size]
        i += size + 2
    return bytes(body), rest[i:], trailer


def strict_gate(headers):
    """现代网关的正确姿势: 歧义一律 400。"""
    if "content-length" in headers and "transfer-encoding" in headers:
        raise ValueError("CL 与 TE 并存 -> 400 拒绝")
    te = headers.get("transfer-encoding", "")
    if te and te.lower() != "chunked":
        raise ValueError("未知 TE 编码 -> 400 拒绝")


def main():
    # 1) 歧义报文: 两种解析器看到两个世界
    headers, rest = split_head(RAW)
    cl_body, cl_rest = parse_by_content_length(headers, rest)
    te_body, te_rest, _ = parse_by_chunked(rest)
    print("CL 视角 body:", cl_body)
    print("CL 视角剩余流开头:", cl_rest[:16])
    print("TE 视角 body:", te_body)
    print("TE 视角剩余流:", te_rest)
    assert cl_body == b"3\r\nabc\r\n", "前端按 CL 认为体只有 8 字节"
    assert te_body == b"abc", "后端按 TE 认为体是 abc"
    assert te_rest.startswith(b"GET /admin"), "后端把剩余字节解析成新请求 -> 走私"

    # 2) 严格网关: 直接拒绝歧义
    try:
        strict_gate(headers)
        raise AssertionError("歧义报文必须被拒")
    except ValueError as e:
        print("严格网关:", e)

    # 3) 正常 chunked + trailer 应解析正确
    headers_n, rest_n = split_head(NORMAL)
    strict_gate(headers_n)
    body_n, tail_n, trailer_n = parse_by_chunked(rest_n, allow_trailer=True)
    print("正常报文 body:", body_n, "| trailer:", trailer_n, "| 剩余:", tail_n)
    assert body_n == b"Wikipedia" and trailer_n == b"X-Check: 1" and tail_n == b""

    print("结论: 解析器对'体到哪结束'的分歧就是走私的裂缝, 歧义必须在网关拒绝")


if __name__ == "__main__":
    main()
```

**追问**:1) TE.TE 变体是什么?——头混淆技巧:TE 头写两次或加混淆,让前端忽略 TE、后端识别 TE——本质还是两边解释不一致。2) 走私的两种基本形态怎么记?——CL.TE(前端按 CL、后端按 TE)与 TE.CL(反向),变体都是让两级解析器「选择不同的体界定」;判断防线只有一条:全链路只允许一种解释,歧义请求 400 拒绝。3) 网关侧的规范化怎么做?——并存即拒、重复 CL 不一致即拒、TE 非 chunked 即拒;规范化后按唯一解释转发,内部组件(Haproxy/Nginx/应用框架)版本要统一升级(老版本解析器差异是走私温床);WAF 不能替代「源头拒绝」。4) 生产陷阱?——自研代理直接转发原字节流(歧义透传);中间件按「最后出现的 CL」处理(各实现不一致);测试只测正常请求,走私用例(双 CL、TE.TE)没进回归;内网服务假定「前面有人把关」而自己不校验。

---
