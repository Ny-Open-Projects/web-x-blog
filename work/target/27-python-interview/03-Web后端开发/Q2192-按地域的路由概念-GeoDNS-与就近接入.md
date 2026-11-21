---
title: [Q2192] 按地域的路由概念:GeoDNS 与就近接入
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2192 · 按地域的路由概念:GeoDNS 与就近接入

> 难度:★★☆☆ | 标签:部署, 架构

**问**:按地域路由是什么层的机制?它解决什么问题、兜底怎么设计?

**答**:地域路由发生在 DNS(GeoDNS/延迟路由策略)与网关层,不在业务代码里:解析时按客户端来源 IP 或 EDNS Client Subnet 把域名解析到最近的接入点,目标是缩短 RTT 与把流量分散到多区域。它解决的是延迟与区域隔离,不是容量问题——每个区域都要能独立承载全部流量,兜底才有意义:某区域健康检查失败,GeoDNS 把该区域从解析结果摘除,流量落到次近的健康区域。业务侧的配套是状态一致:跨区域的数据同步延迟决定了故障切换后的一致性表现,读多写少与最终一致的业务最容易受益。健康探测要用独立拨测点,只用区域内部自检会出现"区域挂了自己不知道"。

```python
# file: code/03_Web后端开发/q2192_geo_routing.py
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
```

**追问**:
- DNS 缓存会不会拖慢故障切换?——会,TTL 设短(如 60s)加客户端重解析,关键服务再加网关层重试跨区域。
- 同一区域内部还要负载均衡吗?——要,GeoDNS 只管区域间,区域内仍由 LB 与服务发现分担到实例。
