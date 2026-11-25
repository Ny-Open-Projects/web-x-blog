---
title: [Q6654] 短连接 TIME_WAIT 容量账
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6654 · 短连接风暴 TIME_WAIT 与端口容量账

难度：P6-P7 | 标签：MySQL、TCP、容量规划

**问**：某定时任务每秒建几百个 MySQL 短连接，运维发现机器上数万条 `TIME_WAIT`。TIME_WAIT 的账怎么算？什么时候会真正"打满端口"，怎么治？

**答**：结论：TIME_WAIT 是**主动关闭方**停留 2*MSL（Linux 固定 60s）的 TCP 状态，不是应用泄漏，而是"谁主动断"的账。客户端每秒 C 个短连接，稳态就积压约 `C × 60` 条 TIME_WAIT。真正的风险不是端口数本身，而是四元组耗尽：客户端连**同一个目标 IP:port** 时可用源端口约 3 万个（28232-61000 可配），`QPS × 60 > 可用源端口` 才会 `Cannot assign requested address`。治本靠连接池复用；治标才用 `tcp_tw_reuse=1`（仅出站方向有效，需时间戳支持）。

实战要点：
1. 账目示例：500 连接/秒 × 60s = 3 万条 TIME_WAIT，恰好逼近同一目标四元组上限，周期性报错。
2. 客户端建连失败特征：connect 阶段 `EADDRNOTAVAIL`，与 MySQL 层 `too many connections` 是两回事，先分清是 OS 账还是 DB 账。
3. 容器环境再乘一层：每 Pod 独立 netns，账按 Pod 算；serverless 短任务最容易踩（参见 Q6536）。

```python
"""TIME_WAIT 稳态与四元组安全水位估算（标准库，可运行）"""
from dataclasses import dataclass

TW_SECONDS = 60.0
EPHEMERAL_LO, EPHEMERAL_HI = 32768, 60999  # ip_local_port_range 常见默认
SAFE_RESERVE = 0.10  # 预留 10% 给其他出站目标


@dataclass
class TwBudget:
    target_ip: str
    target_port: int
    other_conn_per_target: int = 200  # 池内长连接等占用

    @property
    def usable_ports(self) -> int:
        span = EPHEMERAL_HI - EPHEMERAL_LO + 1
        return int(span * (1 - SAFE_RESERVE)) - self.other_conn_per_target

    def safe_short_conn_qps(self) -> int:
        return int(self.usable_ports / TW_SECONDS)


b = TwBudget("10.0.0.8", 3306)
print("可用源端口:", b.usable_ports)
print("安全短连接建连速率:", b.safe_short_conn_qps(), "/s")

planned = 500  # 每秒新建短连接
verdict = "OK" if planned <= b.safe_short_conn_qps() else "必须上连接池"
print(f"计划 {planned}/s ->", verdict)

# 治本估算：池大小 N、每连接平均持有 0.2s，可支撑 QPS ≈ N / 0.2
pool_size = 32
print(f"池大小 {pool_size} 理论支撑:", int(pool_size / 0.2), "QPS")
```

**追问 1**：为什么 `tcp_tw_reuse` 对服务端（被动关闭方）无效？
**提示**：TIME_WAIT 在主动关闭方；服务端大量 TIME_WAIT 说明是服务端先断（如 keepalive 超时配置不当），reuse 帮不上，要靠 keepalive 与长连接。

**追问 2**：把 `ip_local_port_range` 扩到 1024-65535 是不是好方案？
**提示**：只把上限提高约一倍且挤占低位端口；而且只是延后打满，连接数持续增长仍会撞，账还是要算。

**追问 3**：TIME_WAIT 会计入 MySQL `max_connections` 吗？
**提示**：不会，TIME_WAIT 连接已关闭；但建连/断连风暴本身消耗 DB 的线程创建与 TLS 握手成本，DB 侧 CPU 会先报警。

## 背诵要点
- 稳态 TIME_WAIT ≈ 建连 QPS × 60s；同一目标四元组可用源端口约 2.6 万，除以 60 得安全建连速率。
- 客户端 `EADDRNOTAVAIL` 是 OS 四元组账，与 `too many connections`（DB 账）要分清。
- 治本=连接池复用；`tcp_tw_reuse=1` 只对出站短连接有效，是缓兵之计。

## 复盘追问
- 当时如果把任务改成 5 个常驻连接复用，DB 侧哪些指标会同步改善？
- 如何在告警里区分"TIME_WAIT 增长是正常流量放大"与"某处忘了关连接"？
