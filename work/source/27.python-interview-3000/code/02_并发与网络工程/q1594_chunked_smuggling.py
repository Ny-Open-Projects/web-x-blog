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
