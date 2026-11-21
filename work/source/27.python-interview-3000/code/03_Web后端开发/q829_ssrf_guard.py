import ipaddress
from urllib.parse import urlparse

BLOCKED = [
    ipaddress.ip_network(n) for n in (
        "127.0.0.0/8", "10.0.0.0/8", "172.16.0.0/12",
        "192.168.0.0/16", "169.254.0.0/16", "0.0.0.0/8",
    )
]

def is_safe_url(raw: str, resolved_ips: list) -> bool:
    if urlparse(raw).scheme not in ("http", "https"):
        return False                     # 协议白名单
    for s in resolved_ips:               # 用解析后的 IP 判定
        ip = ipaddress.ip_address(s)
        if any(ip in net for net in BLOCKED):
            return False
    return True

print("公网 URL:", is_safe_url("https://api.example.com/x", ["93.184.216.34"]))
print("元数据服务:", is_safe_url("http://internal.local/x", ["169.254.169.254"]))
print("file 协议:", is_safe_url("file:///etc/passwd", []))
