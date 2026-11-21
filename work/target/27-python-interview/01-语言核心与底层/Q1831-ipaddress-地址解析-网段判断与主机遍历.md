---
title: [Q1831] ipaddress:地址解析、网段判断与主机遍历
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1831 · ipaddress:地址解析、网段判断与主机遍历

> 难度:★★★☆☆ | 标签:ipaddress, 网络, 运维

**问**:运维脚本里判断「这个 IP 在不在白名单网段」最稳的写法是什么?

**答**:ipaddress.ip_address(text) 解析并自动识别 v4/v6,非法输入抛 ValueError 而不是静默错判;ip_network(text) 表达网段,in 判成员——192.168.9.7 在 192.168.8.0/22 内为 True,192.168.12.1 已超出 /22 范围为 False,掩码边界计算不用自己写。三个易错点:① ip_network 默认 strict=True,10.0.0.1/24 这种「主机位非零」写法直接报错,容错解析用户输入时才用 strict=False 让它归一化成 10.0.0.0/24;② .hosts() 跳过网络地址与广播地址,遍历可用主机;③ is_private/is_loopback 把 IANA 保留段判定内置,白名单过滤一行搞定。IPv6 同一套 API;address 对象可哈希、可比较、可作集合元素。

```python
# file: code/01_语言核心与底层/q1831_ipaddress_net.py
"""ipaddress:地址解析、网段判断与主机遍历。"""
import ipaddress


def classify(text):
    addr = ipaddress.ip_address(text)     # 自动识别 v4/v6,非法则 ValueError
    return type(addr).__name__, addr.is_private, addr.is_loopback


def subnet_membership():
    net = ipaddress.ip_network("192.168.8.0/22")
    inside = ipaddress.ip_address("192.168.9.7") in net
    outside = ipaddress.ip_address("192.168.12.1") in net   # /22 到 11.255 为止
    return inside, outside


def iterate_hosts(net_text="10.0.0.0/30", n=4):
    return [str(h) for h in ipaddress.ip_network(net_text).hosts()][:n]


def strict_check():
    # 10.0.0.1/24 不是网络地址;strict=False 才会归一化成 10.0.0.0/24
    try:
        ipaddress.ip_network("10.0.0.1/24", strict=True)
        return "没报错?"
    except ValueError as e:
        return str(e)[:46]


if __name__ == "__main__":
    print("8.8.8.8:", classify("8.8.8.8"))
    print("127.0.0.1:", classify("127.0.0.1"))
    print("::1:", classify("::1"))
    print("网段成员判定:", subnet_membership())
    print("可用主机:", iterate_hosts())
    print("strict 校验:", strict_check())
```

**追问**:1) 录入 ACL 网段要不要 strict=False?——不要:管理面录入要严格校验,自动归一化会掩盖「主机位写错」;strict=False 只留给容错解析的读路径。2) 网段判断的完整工具箱?——addr in network 成员判断、network.subnets()/supernet、ip_interface 带主机位;v4/v6 统一抽象,IPv6Address 格式变体自动归一。3) 遍历语义?——network.hosts() 排除网络/广播地址(v4),v6 默认全量;遍历大段(如 /0)是天文数字,要分片或禁止。4) 生产陷阱?——对 /0 全网段 hosts() 遍历挂死;IPv6 zone id/压缩格式比较失误;字符串判断网段(应 in network);录入时 strict=False 吞错。
