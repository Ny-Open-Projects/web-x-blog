---
title: "[Q6713] 半同步复制 after_sync 与 after_commit 的丢数据分界"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6713 · 半同步复制 after_sync 与 after_commit 的丢数据分界

难度：P7 ｜ 标签：MySQL、半同步复制、故障切换、数据安全

基线：Python 3.12；MySQL 8.0 半同步插件；纯 Python 模拟两种 ACK 时机下的切换丢写。

**问**：MySQL 开了半同步复制，团队认为"至少一个从库确认才算成功"，于是对外承诺不丢数据。一次主库宕机切从库后，仍然丢了几百笔已返回成功的订单。半同步不是已经等从库了吗？`after_sync` 和 `after_commit` 的区别到底在哪？

**答**：
- **结论**：半同步的"确认"有两个时机。`after_commit`（旧默认）：主库**先提交事务、再等从库 ACK**，客户端拿到成功时主库已提交，但从库可能还没收到 binlog；主库宕机、从库被提升，这批"已 ACK 但未复制"的事务就丢了。`after_sync`（MySQL 5.7.2+ 推荐）：主库**先等从库 ACK，再在存储引擎层提交**，客户端成功时从库已有 binlog，切换不丢。名字里的 sync 指的就是"先同步再提交"。
- **取舍**：`after_sync` 把网络 RTT 放进提交路径，写延迟上升；从库故障或延迟时主库会退化为异步（`rpl_semi_sync_master_timeout` 后），此时承诺自动失效，必须有监控。`after_commit` 延迟略低但存在丢窗口，只在能容忍少量丢失的场景用。
- **实战**：① 金融链路用 `after_sync` + `rpl_semi_sync_master_wait_for_slave_count=1`，并把超时退化当成一级告警；② 切换剧本要校验候选从库的 `relay_master_log_file/exec_master_log_pos` 是否覆盖最后一批已 ACK 事务；③ 不要只依赖半同步，应用侧仍要幂等与对账——半同步降低窗口，不提供跨机房强一致。

```python
def replicate(
    commits: int, ack_mode: str, ack_lag_ratio: float, crash_at: int
) -> dict[str, int]:
    """ack_mode: after_commit / after_sync；ack_lag_ratio 表示未及时复制的比例。"""
    acked_but_missing = 0
    client_success = 0
    for i in range(commits):
        if i >= crash_at:
            break
        replicated = (i % 100) >= int(ack_lag_ratio * 100)
        if ack_mode == "after_sync" and not replicated:
            continue                     # 没等到 ACK，不算客户端成功
        client_success += 1
        if not replicated:
            acked_but_missing += 1       # after_commit：成功了但从库没有
    return {"client_success": client_success, "lost_after_failover": acked_but_missing}


if __name__ == "__main__":
    print("after_commit:", replicate(1000, "after_commit", 0.03, 900))
    print("after_sync  :", replicate(1000, "after_sync", 0.03, 900))
    print("结论：after_commit 的 ACK 在提交之后，切换会丢已成功事务")
```

**追问一**：`after_sync` 下从库 ACK 了但主库在提交前崩溃，事务算成功还是失败？
→ 解析：客户端还没收到成功，事务对客户端是失败；主库重启后该事务可能已写入 binlog 但引擎层未提交，崩溃恢复会按 binlog 重放，最终可能提交。所以应用必须用幂等键处理"客户端以为失败、服务端可能成功"的模糊态。

**追问二**：半同步退化为异步后，怎么发现承诺已经失效？
→ 解析：监控 `Rpl_semi_sync_master_status`（OFF 即退化）、`Rpl_semi_sync_master_no_tx` 与超时计数；退化期间把写降级到"可丢失"的业务分级，或直接拒绝高风险写，别让承诺静默失效。
