---
title: [Q6585] Redis maxclients 与连接池容量账
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6585 · Redis maxclients 与连接池容量账

难度：P6 ｜ 标签：Redis / maxclients / 连接池 / 容量规划

**问**：微服务扩容后 Redis 开始报 `ERR max number of clients reached`，运维把 maxclients 从 10000 调到 50000，问题"解决"了。这个做法藏了什么坑？Redis 的连接数容量到底怎么算？

**答**：
- **结论**：Redis 连接是每连接一个文件描述符 + 一块客户端缓冲内存（约几 KB 到几十 KB，输出缓冲区可以随慢客户端膨胀），50000 连接除了 FD 上限（还要看 `ulimit -n` 与 fs.file-max），更怕的是内存：连接层内存 ≈ 连接数 × 单连接缓冲，且慢客户端/大结果集会让输出缓冲冲到 `client-output-buffer-limit`。调大 maxclients 只是把"立即报错"改成"缓慢内存膨胀后 OOM"——错误可见性换成了隐患延迟。正确算法：`所需连接数 = Σ(每服务实例 × 池上限) + 发布期抖动（滚动重启瞬时翻倍）+ 监控/运维连接`，并把结果与实例内存账一起验算。
- **取舍**：客户端连接池要设硬上限（redis-py `ConnectionPool(max_connections=...)`），超限行为选 `BlockingConnectionPool`（排队等待）而不是默认池（直接抛错）或无上限（连接泄漏）。分片/多实例时账要分开算：Cluster 里每个客户端会对每个主节点都建池，连接数是"服务实例 × 节点数 × 池大小"的乘积——扩容节点数时连接数也跟着乘上去，这是容量账里最常漏乘的一项。
- **实战**：步骤：① 盘点所有客户端池上限，算乘积账；② maxclients 设为账面值 × 1.3（发布抖动），同时检查 `ulimit -n` ≥ maxclients + 1024；③ `info clients` 的 connected_clients 建立水位告警（70%/90%）；④ 用 `client list` 定期巡检空闲连接（idle 时间长的）找泄漏源——连接泄漏（只建不还）是池无上限部署的常见后果。

```python
# Redis 连接数容量账计算器（纯标准库）
# 基线：Python 3.9+

def redis_conn_budget(
    services: list[dict],       # [{"instances": n, "pool_size": p, "nodes": k}]
    burst_factor: float = 1.3,
    mem_per_conn_kb: int = 16,
) -> dict:
    """Cluster 模式下连接数 = 实例 × 节点数 × 池大小（最常漏乘项）"""
    total = sum(s["instances"] * s.get("nodes", 1) * s["pool_size"]
                for s in services)
    limit = int(total * burst_factor)
    conn_mem_mb = limit * mem_per_conn_kb / 1024
    return {"expected_conns": total, "maxclients": limit,
            "conn_mem_mb": round(conn_mem_mb, 1)}


def main() -> None:
    services = [
        {"instances": 20, "pool_size": 32, "nodes": 3},   # web 服务
        {"instances": 5,  "pool_size": 10, "nodes": 3},   # 后台任务
    ]
    b = redis_conn_budget(services)
    print(b)
    # 20*32*3 + 5*10*3 = 1920 + 150 = 2070
    assert b["expected_conns"] == 2070
    assert b["maxclients"] == 2691
    # 节点从 3 扩到 6：连接数翻倍 —— 漏乘节点数会算错一半
    b2 = redis_conn_budget([dict(s, nodes=6) for s in services])
    assert b2["expected_conns"] == 4140
    print("OK: 节点扩容时连接账按乘积翻倍")


if __name__ == "__main__":
    main()
```

**追问 1**：`client-output-buffer-limit` 和 maxclients 有什么联动风险？
→ 一句话提示：慢客户端（如做大范围 SCAN 或订阅大消息）会让输出缓冲堆积，两个参数都要设——maxclients 管连接个数，output-buffer-limit 管单个连接能占多少内存，缺一个都可能 OOM。

**追问 2**：为什么发布滚动重启时连接数会瞬时翻倍？
→ 一句话提示：旧实例还没退、新实例已建池，两端各持一份连接池；容量账的 burst_factor 就是为这种瞬时峰值预留的，不然每次发布都可能触发 maxclients 报错。

## 背诵要点
- 连接账 = Σ(实例 × 节点数 × 池上限) × 1.3 抖动；Cluster 下漏乘节点数是头号错误。
- 调大 maxclients 只是把报错换成内存膨胀；FD 上限、输出缓冲限制要同步检查。
- 客户端池用 BlockingConnectionPool 排队而非无上限；`client list` 巡检空闲连接找泄漏。

## 复盘追问
- pub/sub 订阅者的输出缓冲为什么要单独设更宽的限额？提示：订阅类客户端平时空闲但消息高峰时积压迅猛，Redis 对 slave/pubsub 有独立的 buffer-limit 档位，默认比普通客户端宽松，漏配会在消息风暴时 OOM。
- 连接池池内连接长期 idle 被服务端踢掉（timeout 配置）会发生什么？提示：客户端拿到已断连接会报 ConnectionError，需要靠客户端健康检查（socket_keepalive/health_check_interval）与空闲回收对齐服务端 timeout。
