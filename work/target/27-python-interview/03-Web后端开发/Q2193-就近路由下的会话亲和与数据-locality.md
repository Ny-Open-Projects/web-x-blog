---
title: [Q2193] 就近路由下的会话亲和与数据 locality
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2193 · 就近路由下的会话亲和与数据 locality

> 难度:★★★★ | 标签:部署, 架构

**问**:用户被路由到某个区域后,为什么要把他"粘"在那里?粘不住会付出什么代价?

**答**:亲和性的收益是数据 locality:用户的会话状态、热点缓存、读写的主库都在首选区域,粘住意味着缓存命中、低 RTT、写路径不跨区;粘不住(负载均衡不感知用户、区域抖动、解析漂移)时,每个请求都可能跨区回源取数据——多一次跨区 RTT、主区读压力集中、跨区流量费上涨。实现亲和的手段从外到内:GeoDNS 固定解析、网关按用户哈希选区域、应用层会话记录首选区域并在响应里携带建议。代价与判据:亲和会让区域间负载倾斜,当倾斜的容量代价高于跨区调用的延迟代价时(热点用户集中),要主动打散;判据用数据说话——跨区请求的占比与额外延迟,超过预算才值得放弃亲和。

```python
# file: code/03_Web后端开发/q2193_affinity_locality.py
"""就近路由下的会话亲和: 粘住区域复用缓存与数据 locality(纯标准库)。"""

USER_REGION = {"u1": "cn-east", "u2": "cn-north"}
CACHE_BY_REGION = {"cn-east": {"u1:cart": ["book"]}, "cn-north": {}}
CROSS_RTT_MS = 30                                     # 跨区回源一次的往返成本
counter = {"n": 0}


def get_cart(user, sticky=True):
    home = USER_REGION[user]
    if sticky:
        region = home
    else:
        regions = sorted(CACHE_BY_REGION)
        region = regions[counter["n"] % len(regions)]   # 不感知用户的轮转
        counter["n"] += 1
    key = user + ":cart"
    if key in CACHE_BY_REGION[region]:
        return CACHE_BY_REGION[region][key], region, 0
    return CACHE_BY_REGION[home].get(key), region, CROSS_RTT_MS


print("粘住主区      :", get_cart("u1", sticky=True))
print("不感知用户 1  :", get_cart("u1", sticky=False))
print("不感知用户 2  :", get_cart("u1", sticky=False))
cart, region, cost = get_cart("u1", sticky=False)
assert cost in (0, CROSS_RTT_MS)
print("要点: 亲和的收益是缓存命中与数据近距离, 判据是跨区请求占比与额外延迟是否超预算")
```

**追问**:
- 区域故障时亲和怎么解除?——健康检查摘除后亲和表失效,流量切到健康区域并重建缓存,期间接受跨区回源的高成本。
- 亲和与灰度发布冲突吗?——冲突,按用户亲和会阻碍均匀放量,灰度期间要按实例维度放量,发布完再恢复亲和。
