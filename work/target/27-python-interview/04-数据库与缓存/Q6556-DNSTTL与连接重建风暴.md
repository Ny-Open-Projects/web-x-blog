---
title: [Q6556] DNS TTL 与故障切换后的连接重建风暴
date: 2026-11-20
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6556 · DNS TTL 与故障切换后的连接重建风暴

难度：P6 | 标签：DNS TTL、故障切换、重连风暴、容量规划

**问**：主库故障切换到新主后，500 个应用实例几乎同时开始重连，新主还没恢复流量就先被建连请求压死了。DNS TTL 在这场事故里扮演什么角色？重连风暴怎么摊平？

**答**：
- **结论**：应用通过域名连数据库，本地解析缓存 TTL 到期才重新解析——TTL 为 0 或所有实例缓存同时过期时，故障切换（域名指向新 IP）的瞬间全体实例在同一秒发起建连，新主每秒建连能力（TLS 握手 + 认证 + 恢复检查）只有几十个，超出的连接被拒，客户端再重试，形成"拒绝-重试"的次生风暴。摊平三板斧：TTL 5-30 秒、重连时刻叠加随机抖动（jitter）、应用侧对新主库的建连限速（令牌桶）。
- **取舍**：TTL 太长，切换后流量迁移慢（客户端拿着旧 IP 继续撞死主库）；TTL 太短，DNS 解析本身变成新风暴源。折中是 5-30 秒 + 抖动——抖动是免费的，TTL 是延迟与风暴的旋钮。有的驱动支持 connect retry with backoff，必须带随机化，否则所有实例的重试序列整齐划一。
- **实战**：演练才是验收：定期做切换演练，看"新主建连峰值曲线"是否超出容量预算（TLS 握手的 CPU 成本按每秒几百次算）；连接串里显式配置 connect timeout / retry backoff；数据库中间层（ProxySQL）常自带连接复用，能显著降低新建数。

```python
"""DNS TTL 与故障切换后的连接重建风暴：抖动重连把尖峰摊平。"""
import random
from collections import Counter

random.seed(7)

INSTANCES = 500
NEW_PRIMARY_CAP = 50    # 新主库每秒能接受的新建连接数（TLS 握手 + 认证成本高）

def failover_storm(ttl_s: float, jitter_s: float) -> tuple[int, int]:
    """返回 (每秒新建连接峰值, 被拒连接数)。TTL 过期 + 抖动决定重连时刻。"""
    times = []
    for _ in range(INSTANCES):
        # 本地缓存 TTL 过期后才重新解析；重连时刻叠加人为抖动
        t = ttl_s + random.uniform(0, jitter_s)
        times.append(int(t))
    per_sec = Counter(times)
    peak = max(per_sec.values())
    rejected = sum(max(0, c - NEW_PRIMARY_CAP) for c in per_sec.values())
    return peak, rejected

for ttl, jitter in ((0.0, 0.0), (5.0, 0.0), (5.0, 30.0)):
    peak, rej = failover_storm(ttl, jitter)
    extra = f"，被拒 {rej} 个（触发下一轮重试风暴）" if rej else "，无拒绝"
    print(f"TTL={ttl}s 抖动={jitter}s -> 新建连接峰值 {peak}/s{extra}")

print("治理组合：TTL 5-30s（别用 0，否则 DNS 解析本身也成风暴）+ 重连抖动 + "
      "应用侧对新主库的建连限速")
```

**追问链**：
1. 追问一层：为什么 TTL=5s 且不加抖动时风暴照样发生？——所有实例缓存过期时刻相同（都在切换后第 5 秒），TTL 只决定了风暴发生在哪一秒，不决定有没有风暴；抖动（随机化重连时刻）才是摊平手段，TTL 与抖动缺一不可。
2. 追问二层：TLS 握手为什么放大了建连成本？——每次新建连接要做 TCP 三次握手 + TLS 握手（RSA/ECDHE 运算）+ 认证往返，单次 CPU 成本是普通内网握手的一个数量级以上；新主恢复初期 CPU 本来就紧，建连限速实际是在保护它的 CPU 水位。

**背诵要点**：
1. TTL 决定风暴时刻、不决定有无风暴：全员同时过期 = 全员同一秒重连。
2. 摊平三板斧：TTL 5-30s + 重连抖动 + 对新主建连限速。
3. 验收靠切换演练：看新主建连峰值是否超容量预算，超了就拒绝-重试循环。

**复盘追问**：
1. 切换后新主 CPU 100% 但 QPS 为零，查什么？（建连风暴：netstat 看 SYN 队列与 TLS 握手速率，应用侧上抖动与建连限速）
2. 为什么"把 TTL 调成 0"是反向操作？（解析本身成为热点且切换瞬间所有实例同步解析+重连，风暴更大；TTL 的价值是给迁移一个可控的收敛窗口）
