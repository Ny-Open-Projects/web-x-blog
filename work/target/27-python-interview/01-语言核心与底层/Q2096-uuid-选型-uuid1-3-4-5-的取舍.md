---
title: [Q2096] uuid 选型:uuid1/3/4/5 的取舍
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2096 · uuid 选型:uuid1/3/4/5 的取舍

> 难度:★★★☆☆ | 标签:uuid, ID 设计, 标准库

**问**:uuid1、uuid4、uuid5 各适合什么场景?怎么给业务表选主键 ID?

**答**:默认答案是 uuid4:122 位随机,碰撞概率工程上可忽略,无隐私泄露,适合绝大多数「只要唯一」的场景。uuid1 是「时间戳 + 时钟序列 + 节点 MAC」,优点是生成端近似有序、可按时间粗排,代价是 .node 字段暴露生成机器的 MAC 地址——日志与对外接口里用它可被关联定位设备,隐私敏感场景禁用。uuid5 是命名空间 + 名字的 SHA1 确定性散列:同一命名空间同一名字永远得到同一 UUID,适合「同名同 ID」的场景,比如按域名生成稳定标识、跨系统对齐资源 ID(demo 验证了确定性);uuid3 同思路但用 MD5,新代码一律选 uuid5。选型口诀:要唯一用 uuid4,要时间序用 uuid1 级别的时间有序方案,要确定性用 uuid5。

```python
# file: code/01_语言核心与底层/q2096_uuid_choice.py
"""uuid 选型:uuid1、uuid4 与 uuid5 的取舍。"""
import uuid


if __name__ == "__main__":
    u4a, u4b = uuid.uuid4(), uuid.uuid4()
    print("uuid4 随机:", str(u4a)[:18], "两次不同:", u4a != u4b)

    u1 = uuid.uuid1()
    print("uuid1 带时间戳与节点:", u1.fields[0] > 0, "| MAC 来自 node 字段:", hex(u1.node)[:10], "...")
    print("uuid1 生成端时间可比较:", uuid.uuid1().time >= u1.time)

    n1 = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")
    n2 = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")
    print("uuid5 确定性:同输入同输出:", n1 == n2, "|", n1)
    print("换命名空间结果改变:", uuid.uuid5(uuid.NAMESPACE_URL, "example.com") != n1)

    print("选型:常规唯一用 uuid4;确定性标识用 uuid5;uuid1 注意 MAC 隐私")
```

**追问**:1) uuid1 的隐私风险具体在哪?——node 字段携带网卡 MAC,跨数据源关联可定位设备;需要时间有序的公开 ID 怎么办?——用时间戳前缀的自实现方案或新版 uuid7 思路,uuid1 因为 MAC 问题只限内网受控场景。2) 选型矩阵?——v4 随机默认;v3/v5 按命名空间+名字确定性(v5 SHA1 优先);uuid1 时间有序但泄 MAC;3.14+ 标准库加入 uuid6/uuid7(时间有序、无 MAC)。3) 工程属性?——v4 无序导致数据库索引随机写放大,热点主键常改用「时间前缀 + 随机尾」;字符串比较统一小写;存储用 16 字节二进制而不是 36 字符。4) 生产陷阱?——uuid1 进对外 API 泄 MAC;把 uuid 字符串截断存库;拿 uuid 前几位当时间排序(v4 不行)。
