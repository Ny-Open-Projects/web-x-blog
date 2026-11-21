"""CRLF 头注入: 响应头的消毒。

攻击者把 \\r\\n 塞进会回显进响应头的输入(如昵称、搜索词):
  X-User: attacker\\r\\nSet-Cookie: session=pwned
响应头被拆成两条, 攻击者凭空注入了 Set-Cookie 甚至整个响应体。
防线: 头值消毒(剥 CR/LF/NUL)+ 头名白名单, 双保险。
"""
def build_response(status, headers):
    lines = ["HTTP/1.1 %s" % status]
    for k, v in headers:
        lines.append("%s: %s" % (k, v))
    return ("\r\n".join(lines) + "\r\n\r\n").encode() + b"ok"


def sanitize(value):
    """剥掉 CR/LF/NUL: 头值只能是单行文本。"""
    for ch in ("\r", "\n", "\x00"):
        value = value.replace(ch, "")
    return value


ALLOWED = {"X-User", "Content-Type", "Cache-Control"}


def build_response_safe(status, headers):
    lines = ["HTTP/1.1 %s" % status]
    for k, v in headers:
        if k not in ALLOWED:            # 头名白名单
            continue
        lines.append("%s: %s" % (sanitize(k), sanitize(v)))
    return ("\r\n".join(lines) + "\r\n\r\n").encode() + b"ok"


def head_lines(resp):
    return resp.split(b"\r\n\r\n")[0].split(b"\r\n")


def main():
    attacker = "alice\r\nSet-Cookie: session=pwned\r\n\r\nHTTP/1.1 200 OK"

    vulnerable = build_response("200 OK", [("X-User", attacker)])
    lines = head_lines(vulnerable)
    print("易感实现的响应头:")
    for ln in lines:
        print("   %s" % ln.decode(errors="replace"))
    injected = any(b"Set-Cookie" in ln for ln in lines)
    print("注入成功:", injected)
    assert injected, "不做消毒时, 攻击者应能注入 Set-Cookie 头"

    safe = build_response_safe("200 OK",
                               [("X-User", attacker),
                                ("X-Evil", "should-be-dropped"),
                                ("Content-Type", "text/plain")])
    lines = head_lines(safe)
    print("消毒后的响应头:")
    for ln in lines:
        print("   %s" % ln.decode(errors="replace"))
    assert not any(ln.startswith(b"Set-Cookie") for ln in lines), \
        "CR/LF 已剥除, 不再拆出独立头行"
    assert not any(b"X-Evil" in ln for ln in lines), "白名单外的头应被丢弃"
    assert any(b"alice" in ln for ln in lines), "合法内容保留(压平成单行)"
    print("注意: 残留的 Set-Cookie 字样只是被压平的头值文本, 已无头语义")

    print("结论: CRLF 是头与体的分界符, 进头之前必须消毒——白名单是第二道锁")


if __name__ == "__main__":
    main()
