"""按地域的路由概念: 就近解析与故障兜底(纯标准库)。"""

REGIONS = {
    "cn-east": {"endpoint": "sh.example.com", "covers": ("116.", "117."), "alive": True},
    "cn-north": {"endpoint": "bj.example.com", "covers": ("111.", "112."), "alive": True},
    "cn-south": {"endpoint": "gz.example.com", "covers": ("113.", "119."), "alive": False},
}
FALLBACK_ORDER = ["cn-east", "cn-north", "cn-south"]


def resolve(client_ip):
    """先按来源前缀就近, 区域故障或无匹配时按顺序兜底到健康区域。"""
    for region, conf in REGIONS.items():
        if conf["alive"] and client_ip.startswith(conf["covers"]):
            return conf["endpoint"], region
    for region in FALLBACK_ORDER:
        conf = REGIONS[region]
        if conf["alive"]:
            return conf["endpoint"], region + " 兜底"
    raise RuntimeError("无可用区域")


for ip in ["116.24.1.2", "111.199.1.2", "113.5.5.5", "8.8.8.8"]:
    print("{:12s} -> {}".format(ip, resolve(ip)))
print("要点: 地域路由在 DNS 与网关层完成, 每个区域都要能独立承载全量流量, 兜底才有意义")
