"""X-Forwarded-For 的信任链: 从右往左跳过可信代理数(纯标准库)。"""

TRUSTED_PROXIES = 2                                    # 边缘 LB + 内部网关


def client_ip(xff_header, remote_addr):
    """remote_addr 是 TCP 对端, 是唯一无条件可信的地址。"""
    if not xff_header:
        return remote_addr, "无 XFF, 直接取对端"
    hops = [h.strip() for h in xff_header.split(",")]
    if len(hops) < TRUSTED_PROXIES:
        return remote_addr, "跳数不足, 疑似绕过代理, 保守取对端"
    return hops[-TRUSTED_PROXIES], "取倒数第 {} 跳".format(TRUSTED_PROXIES)


cases = [
    ("9.9.9.9, 10.0.0.3", "10.0.0.3", "正常两级代理"),
    ("6.6.6.6, 9.9.9.9, 10.0.0.3", "10.0.0.3", "客户端自带伪造头"),
    ("6.6.6.6", "10.0.0.9", "直连伪造跳数不足"),
    (None, "10.0.0.9", "直连无 XFF"),
]
for xff, remote, label in cases:
    ip, why = client_ip(xff, remote)
    print("{:12s} XFF={!r:30s} -> {} ({})".format(label, xff, ip, why))
assert client_ip("6.6.6.6, 9.9.9.9, 10.0.0.3", "10.0.0.3")[0] == "9.9.9.9"
print("要点: 每个可信代理追加一跳, 真实 IP 在倒数第 N 跳; 取第一跳等于信任攻击者的输入")
