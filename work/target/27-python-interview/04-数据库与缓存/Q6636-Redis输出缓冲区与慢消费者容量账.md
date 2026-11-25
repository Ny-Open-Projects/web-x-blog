---
title: [Q6636] Redis 客户端输出缓冲区（client-output-buffer-limit）与慢消费者容量账
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6636 · Redis 客户端输出缓冲区与慢消费者容量账

难度：P6 ｜ 标签：容量规划 / Redis / 可靠性

**问**：一次大 Key 导出（几十 MB 的 `GET`）加一个慢消费者（客户端假死但连接还在），把 Redis 内存顶到 maxmemory 触发淘汰甚至 OOM。输出缓冲区（client output buffer）是怎么撑爆内存的？容量账怎么算、参数怎么设？

**答**：
- **结论**：Redis 对每个客户端连接维护一个**输出缓冲区**：命令响应先写入这里，再逐步发往 socket。当客户端收得慢（网络慢、应用 GC 停顿、假死不读）而命令响应大（大 Key、`LRANGE 0 -1`、pubsub 广播、monitor），缓冲区持续堆积——这部分内存**不受 maxmemory 约束之外的保护**（实际上算在 used_memory 里却淘汰不了），堆积多了整机 OOM 或触发淘汰扰动。防线是 `client-output-buffer-limit <class> <hard> <soft> <soft-sec>`：hard = 缓冲区绝对上限立即断开；soft = 超过 soft 值持续 soft-sec 秒才断（容忍突发）。三类各配：normal（普通命令）、replica（主从同步，需大：一次全量 RDB 传输都走这里）、pubsub（订阅端慢是重灾区，Q6605）。容量账公式：峰值缓冲 = 单响应大小 × 未消费响应数，pubsub 场景 = 发布速率 × 慢订阅时长。
- **取舍**：limit 设太紧会把正常的大响应/主从全量同步掐断（复制反复重连，Q1422）；设太松在慢消费者出现时是定时炸弹。原则：normal 严格（64MB/16MB-60s 量级）、replica 宽松（按 RDB 大小算）、pubsub 按最慢订阅者容忍时长算。更根本的解法是**不产生大响应**：大 Key 拆桶（Q6643）、SCAN 替代 KEYS、`LRANGE` 分批。
- **实战**：① `CLIENT LIST` 的 `omem` 字段监控缓冲区堆积，对 omem > 阈值的连接告警；② `CLIENT KILL TYPE normal ADDR ...` 是应急处置（先摘掉慢消费者）；③ 应用侧设置 socket 读超时 + 健康检查，假死连接靠 TCP keepalive 不够快；④ pubsub 上线前算账：发布速率 × 最慢消费者容忍秒数必须 < soft 限制。

```python
# 输出缓冲区堆积模型: 慢消费者 + 大响应 -> omem 增长与 limit 断开判定
# 基线: Python 3.9+ 标准库; 线上核实用 CLIENT LIST 的 omem 字段
from dataclasses import dataclass


@dataclass
class OutputBuffer:
    hard_limit: int            # bytes, 超限立即断
    soft_limit: int
    soft_sec: int
    omem: int = 0              # 当前堆积
    above_soft_for: int = 0    # 持续超 soft 的秒数

    def on_response(self, resp_bytes: int, consumed_bytes: int) -> str:
        self.omem += resp_bytes - consumed_bytes
        if self.omem > self.hard_limit:
            return "KILL(hard)"
        if self.omem > self.soft_limit:
            self.above_soft_for += 1
            if self.above_soft_for >= self.soft_sec:
                return "KILL(soft)"
        else:
            self.above_soft_for = 0
        return "ok"


def main() -> None:
    # pubsub: 1KB/条 发布, 订阅端完全假死, soft=8MB/40s
    buf = OutputBuffer(hard_limit=64 << 20, soft_limit=8 << 20, soft_sec=40)
    pub_per_sec = 1000 * 1024                # 1MB/s
    for _ in range(47):                      # 47 秒: 尚未满 40 秒宽限
        assert buf.on_response(pub_per_sec, 0) == "ok"
    assert buf.above_soft_for == 39          # 第 9 秒起持续超 soft
    assert buf.on_response(pub_per_sec, 0) == "KILL(soft)"   # 第 40 秒断开
    assert buf.omem >= 47 * 1024 * 1000      # ~47MB 已堆积
    # 大 Key 单响应: 200MB GET 直接撞 hard
    buf2 = OutputBuffer(hard_limit=64 << 20, soft_limit=16 << 20, soft_sec=60)
    assert buf2.on_response(200 << 20, 0) == "KILL(hard)"
    print("OK: soft+soft_sec 容忍突发, hard 掐单响应; 大Key/慢消费者是两类源头")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么 replica 类的输出缓冲区要配得特别大？
→ 一句话提示：全量同步时主库要把整个 RDB 先写进该从库的输出缓冲区再传输，缓冲区上限小于 RDB 大小会导致同步反复失败重连，永远追不上。

**追问 2**：输出缓冲区内存和 maxmemory 淘汰是什么关系？
→ 一句话提示：缓冲区属于 used_memory 但不是"可淘汰的键空间"，淘汰只能赶数据赶不掉缓冲区；极端时缓冲区把内存顶到 OOM，淘汰策略根本救不了——所以必须用 limit 在连接层面断开。

## 背诵要点
- 输出缓冲区 = 每连接的响应暂存区；堆积源头两类 = 大响应（大 Key/monitor）+ 慢消费者（假死/pubsub 慢订阅）。
- 参数三段式：hard（立即断）/ soft+soft_sec（容忍突发）；normal 紧（64MB/16MB-60s 量级）、replica 宽（≥RDB 大小）、pubsub 按"发布速率 × 容忍秒数"算。
- 监控 `CLIENT LIST` 的 omem；应急 `CLIENT KILL`；根治 = 大 Key 拆桶 + 分批读。

## 复盘追问
- omem 告警触发后，如何区分是"大 Key 响应"还是"慢消费者"？提示：看该连接的 `cmd` 与输出堆积增速——单次跳变大是大响应，持续线性涨且 `tot-net` 低是消费慢。
- 为什么 TCP 层的背压（socket 发送缓冲满）不能替代这个机制？提示：内核 socket 缓冲满后 Redis 只能停写但连接占着，缓冲区仍在堆；必须应用层主动断开释放内存与连接槽。
