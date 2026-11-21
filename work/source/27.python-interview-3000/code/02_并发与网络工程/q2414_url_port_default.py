# -*- coding: utf-8 -*-
"""URL 端口默认值补全: urlsplit 不替你补端口, 规范化要自己做。

- urlsplit 只做切分, https://a.example 的 port 是 None, 不是 443;
- 监控去重、缓存键、限流桶都按 origin 归组, 不补默认端口就会一分为二;
- 显式写 :443 与不写是同一个服务, 规范化后必须合并。
"""
from urllib.parse import urlsplit

DEFAULT_PORTS = {"http": 80, "https": 443, "ws": 80, "wss": 443, "ftp": 21}


def canonical_origin(url):
    """补全默认端口, 剥掉 userinfo, 产出规范化 origin。"""
    parts = urlsplit(url)
    scheme = parts.scheme.lower()
    if not parts.hostname:
        raise ValueError("无法解析主机: %r" % url)
    host = parts.hostname.lower()                # 已解包 userinfo 与方括号 IPv6
    if ":" in host:
        host = "[%s]" % host                     # IPv6 字面量要重新带方括号
    port = parts.port
    if port is None:
        if scheme not in DEFAULT_PORTS:
            raise ValueError("scheme %r 没有已知默认端口" % scheme)
        port = DEFAULT_PORTS[scheme]
    elif DEFAULT_PORTS.get(scheme) == port:
        port = DEFAULT_PORTS[scheme]             # 显式默认端口归一化
    return "%s://%s:%d" % (scheme, host, port)


def main():
    cases = [
        ("https://api.Example.com/v1", "https://api.example.com:443"),
        ("https://api.example.com:443/v1", "https://api.example.com:443"),
        ("http://api.example.com", "http://api.example.com:80"),
        ("https://u:pass@api.example.com:8443/x", "https://api.example.com:8443"),
        ("http://[::1]:8080/m", "http://[::1]:8080"),
        ("http://[::1]/m", "http://[::1]:80"),
    ]
    for raw, want in cases:
        got = canonical_origin(raw)
        print("%-42s -> %s" % (raw, got))
        assert got == want, "规范化结果不符"

    # 监控归组的实际收益: 四种写法本是同一服务
    aliases = {"https://a.io", "https://a.io:443", "https://A.io/",
               "https://u@a.io"}
    grouped = {canonical_origin(u) for u in aliases}
    print("四种别名归一后只剩:", grouped)
    assert len(grouped) == 1, "默认端口补全让监控分组不再裂开"

    # 无端口默认值的 scheme: 明确报错而不是猜
    try:
        canonical_origin("ftp-x://host/path")
        raise AssertionError("未知 scheme 应当报错")
    except ValueError as e:
        print("未知 scheme 正确报错:", e)
    # ftp 在表里, 直接给默认
    print("ftp 默认端口:", canonical_origin("ftp://files.example"))


if __name__ == "__main__":
    main()
