import os
import urllib.request


def matches_no_proxy(host: str, port: int, no_proxy: str,
                     port_sensitive: bool = True) -> bool:
    """复刻 http.client 的 NO_PROXY 语义 (含端口敏感行为)。"""
    host = (host or "").lower()
    for entry in no_proxy.split(","):
        entry = entry.strip().lower()
        if not entry:
            continue
        if ":" in entry:  # 带端口: 仅匹配该端口
            ehost, eport = entry.rsplit(":", 1)
            if port_sensitive and str(port) != eport:
                continue
            entry_host = ehost
        else:
            entry_host = entry
        entry_host = entry_host.lstrip(".")
        if host == entry_host or host.endswith("." + entry_host):
            return True
        if entry_host == "*":  # 全部直连
            return True
    return False


if __name__ == "__main__":
    os.environ.update({
        "HTTP_PROXY": "http://proxy:3128",
        "HTTPS_PROXY": "http://proxy:3128",
        "NO_PROXY": "localhost,127.0.0.1,.internal,repo.corp:8080",
    })
    print("getproxies():", urllib.request.getproxies())
    print("\nNO_PROXY 匹配判定:")
    cases = [
        ("localhost", 80, True),
        ("db.prod.internal", 5432, True),     # .internal 后缀
        ("notinternal.example", 80, False),   # 后缀陷阱: 须是 .internal 子域
        ("repo.corp", 8080, True),            # 带端口条目命中
        ("repo.corp", 443, False),            # 端口不符 → 走代理
        ("127.0.0.1", 80, True),
    ]
    for host, port, expect in cases:
        got = matches_no_proxy(host, port, os.environ["NO_PROXY"])
        mark = "OK " if got == expect else "FAIL"
        print(f"  [{mark}] {host}:{port} → direct={got}")
        assert got == expect

    print("\n端口条目注意: 'repo.corp:8080' 只影响 8080 端口, 443 仍走代理")
    print("建议: 内网域名一律用后缀形式 (.internal), 避免依赖端口语义")
