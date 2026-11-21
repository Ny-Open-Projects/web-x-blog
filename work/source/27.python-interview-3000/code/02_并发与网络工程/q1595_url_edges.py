"""URL 解析的边界: urlsplit 坑位清单。

- .port 是惰性属性: 访问非法端口才抛 ValueError, 存一步、炸一步;
- IPv6 主机带方括号, .hostname 返回去括号的地址;
- urlparse 会把分号段拆成 params, urlsplit 不会 —— 两者选型要看场景;
- 反斜杠不是分隔符: https:\\host 会被整个塞进 path, netloc 为空;
- 默认端口(443/80)时 .port 返回 None;
- %2F 解码后变成 /, 路径语义在"解码前后"是两回事。
"""
from urllib.parse import urlsplit, urlparse, unquote

CASES = [
    "https://user:pass@127.0.0.1:8443/a/b?k=v#frag",
    "http://[::1]:8080/ipv6",
    "https://example.com//double//slash",
    "https://example.com/path/index;jessionid",
    "https://EXAMPLE.com/UPPER",
    "example.com/no-scheme",
    "https://example.com:99999/bad-port",
    "https://example.com/a%2Fb",
    "https:\\\\example.com\\path",
]


def main():
    findings = []

    s = urlsplit(CASES[0])
    print("userinfo 场景:", s.netloc, "| hostname:", s.hostname, "| port:", s.port)
    assert s.hostname == "127.0.0.1" and s.port == 8443
    assert s.username == "user" and s.password == "pass"

    s = urlsplit(CASES[1])
    print("IPv6 场景: netloc=%s hostname=%s port=%s" % (s.netloc, s.hostname, s.port))
    assert s.hostname == "::1" and s.port == 8080
    findings.append("ipv6")

    s = urlsplit(CASES[2])
    print("双斜杠场景: path=%s (不合并, 语义交给服务端)" % s.path)
    assert s.path == "//double//slash"

    u = urlparse(CASES[3])
    s = urlsplit(CASES[3])
    print("分号场景: urlparse path=%r params=%r | urlsplit path=%r"
          % (u.path, u.params, s.path))
    assert u.params == "jessionid" and u.path == "/path/index"
    assert s.path == "/path/index;jessionid"
    findings.append("urlsplit-vs-urlparse")

    s = urlsplit(CASES[4])
    print("大写+省略端口: scheme=%s hostname=%s port=%s (省略才返回 None, 显式 :443 会返回 443)"
          % (s.scheme, s.hostname, s.port))
    assert s.scheme == "https" and s.hostname == "example.com" and s.port is None
    findings.append("default-port-none")

    s = urlsplit(CASES[5])
    print("无 scheme: netloc=%r path=%r" % (s.netloc, s.path))
    assert s.netloc == "" and s.path == "example.com/no-scheme"

    s = urlsplit(CASES[6])
    try:
        s.port
        raise AssertionError("非法端口应在访问时抛错")
    except ValueError as e:
        print("非法端口访问才抛 ValueError:", e)
        findings.append("lazy-port-error")

    s = urlsplit(CASES[7])
    print("%%2F 场景: 原始 path=%r unquote 后=%r" % (s.path, unquote(s.path)))
    assert s.path == "/a%2Fb" and unquote(s.path) == "/a/b"
    findings.append("percent-encoding")

    s = urlsplit(CASES[8])
    print("反斜杠场景: netloc=%r path=%r (主机丢了)" % (s.netloc, s.path))
    assert s.netloc == "" and "example.com" in s.path
    findings.append("backslash-trap")

    assert len(findings) == 6, "六类边界结论都应验证到"
    print("结论: urlsplit 是'字面拆解', 安全语义要自己补——尤其反斜杠与解码顺序")


if __name__ == "__main__":
    main()
