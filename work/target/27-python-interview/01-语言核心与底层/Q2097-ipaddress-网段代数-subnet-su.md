---
title: [Q2097] ipaddress 网段代数:subnet、supernet 与排除
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2097 · ipaddress 网段代数:subnet、supernet 与排除

> 难度:★★★☆☆ | 标签:ipaddress, 网段运算, 运维

**问**:ipaddress 模块怎么做网段切分、上卷合并和「挖洞排除」?主机位被置位的网段怎么处理?

**答**:网段当作代数对象运算:network.subnets(new_prefix=26) 把 /24 均匀切成 4 个 /26,返回惰性迭代器;subnet.supernet(prefixlen_diff=2) 按前缀长度上卷,兄弟子网并回父网;address_exclude(other) 从父网里挖掉一块,因为剩余区域不连续,返回若干 CIDR 的列表恰好拼回原网。散 IP 区间用 summarize_address_range(first, last) 归并成最小 CIDR 列表——IP 白名单合并的标配。构造时的 strict 校验是个高频坑:ip_network("10.0.0.1/24") 默认拒绝主机位被置位的写法,报 ValueError;配置文件里的「脏网段」用 strict=False 让解释器自动掩掉主机位,demo 两条路径都演示。

```python
# file: code/01_语言核心与底层/q2097_ipaddress_algebra.py
"""ipaddress 网段代数:切分、上卷合并与挖洞排除。"""
import ipaddress

block = ipaddress.ip_network("10.0.0.0/24")


if __name__ == "__main__":
    subs = sorted(block.subnets(new_prefix=26))
    print("/24 切成 4 个 /26:", [str(s) for s in subs])

    merged = subs[0].supernet(prefixlen_diff=2)
    print("上卷两个前缀级回到 /24:", merged == block)

    pieces = block.address_exclude(ipaddress.ip_network("10.0.0.64/26"))
    print("挖掉 10.0.0.64/26 后剩余:", [str(p) for p in pieces])

    rng = ipaddress.summarize_address_range(
        ipaddress.ip_address("192.168.0.8"), ipaddress.ip_address("192.168.0.15"))
    print("散 IP 区间归并为 CIDR:", [str(n) for n in rng])

    print("strict=False 自动掩掉主机位:", ipaddress.ip_network("10.0.0.1/24", strict=False))
    try:
        ipaddress.ip_network("10.0.0.1/24")
    except ValueError as e:
        print("默认 strict 校验:", e)
```

**追问**:1) address_exclude 为什么返回列表?——挖掉中间一块后剩余区域不连续,只能用多个 CIDR 拼回;supernet 有什么前提?——只按前缀长度上卷,子网得真实存在于该父网内,否则结果与预期拓扑不符。2) 网段代数的运算集?——address_exclude 挖洞、supernet/subnets 缩放、overlaps 判断、比较运算符判定包含;全部基于 CIDR 数学,无 DNS/路由语义。3) 与 Q1831 的配合?——录入严格(strict=True)、代数运算后结果可能含主机位变化的网段,要重新校验;大段遍历(如 /0)是天文数字必须禁止。4) 生产陷阱?——exclude 后没重新汇总导致 ACL 漏洞;supernet 跨父网想当然;把「重叠网段」当错误(先 overlaps 判断)。
