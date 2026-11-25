---
title: [Q6635] REPLICAOF 误指主库导致数据被清空的事故复盘
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6635 · REPLICAOF 误指主库导致数据被清空的事故复盘

难度：P6 ｜ 标签：事故复盘 / Redis / 复制

**问**：运维想把一台从库改挂到新主库，执行 `REPLICAOF NEW_HOST 6379` 后发现目标写错了——命令敲到了一台**存有全量数据的主库**上，这台"主库"立刻清空自己、全量同步别的节点的数据。为什么 REPLICAOF 会无条件清库？这类事故如何用权限与流程防住？

**答**：
- **结论**：Redis 复制语义里，一个实例执行 `REPLICAOF host port` 的含义是"**放弃本地数据，成为对方的忠实副本**"——同步开始时先 `PSYNC`，若无法部分重同步则主库触发 BGSAVE 全量同步，从库在载入 RDB 前清空整个数据集（`replicaof` 之后本地旧数据不参与任何保留判断）。所以"对一台有数据的主库误执行 REPLICAOF"= 立即清空，且没有 undo。叠加风险：若被误操作的实例是 Cluster 里的主节点，槽位数据全丢，客户端 MOVED 风暴（Q6582）。防线四层：① **ACL 权限**：生产实例给运维账号只授 `+replicaof` 的白名单或干脆 `-replicaof`（6.0+ ACL 可按命令禁用），普通账号无权改复制拓扑；② **rename-command** 老办法（7.x 仍可用但 ACL 更优）；③ **配置守卫**：`replicaof` 由配置文件管理、运行时禁改（`enable-protected-configs` / 受保护模式）；④ 流程守卫：改复制拓扑走工单 + 先 `DUMP/备份` + 在副本上先验证 `REPLICAOF NO ONE` 恢复路径（Q6639 的误恢复同源风险）。
- **取舍**：ACL 禁掉 replicaof 会牺牲故障时的快速手动切换速度——应急时需走带审计的工单或预置的自动化脚本（脚本账号持有权限但逻辑固定）。rename-command 简单粗暴但破坏客户端兼容性与可发现性；折中：只在"有数据的主库"上禁，纯副本节点保留。
- **实战**：① 任何复制拓扑变更前先 `SAVE/BGSAVE` 或确认有异地备份（本机清空不等于有备份）；② 把"目标实例当前角色"做成变更脚本的第一步断言：`role` 不是 `slave` 就拒绝执行；③ 事后恢复：清空实例若有 AOF/RDB 尚存则重启加载，没有则从任意健康副本再同步回来——前提是 master 数据还在；④ 用 `redis-cli ---cluster check` 验证 Cluster 槽完整性。

```python
# REPLICAOF 事故模型: 复制变更是"放弃本地数据"语义, 需前置断言与权限守卫
# 基线: Python 3.9+ 标准库 (redis-py 5.x: r.execute_command('ROLE'))
from dataclasses import dataclass


@dataclass
class RedisNode:
    role: str                 # master / slave
    keys: int
    acl_allows_replicaof: bool


def try_replicaof(node: RedisNode, target: str) -> str:
    """模拟变更脚本: 三道守卫后才能执行 REPLICAOF。"""
    if not node.acl_allows_replicaof:
        return "BLOCKED: ACL 禁止 replicaof (生产主库应禁)"
    if node.role != "slave":
        return (f"BLOCKED: 目标是 {node.role} 且有 {node.keys} keys, "
                f"REPLICAOF 将清库 -> 先备份/确认")
    return f"OK: 开始同步 {target} (副本可安全重挂)"


def main() -> None:
    prod_master = RedisNode("master", 5_000_000, acl_allows_replicaof=False)
    plain_master = RedisNode("master", 5_000_000, acl_allows_replicaof=True)
    slave = RedisNode("slave", 5_000_000, acl_allows_replicaof=True)
    assert "ACL" in try_replicaof(prod_master, "new-host")
    assert "清库" in try_replicaof(plain_master, "new-host")   # 角色守卫拦截
    assert try_replicaof(slave, "new-host").startswith("OK")
    # 语义演示: replicaof 无条件放弃本地数据
    assert slave.keys > 0
    print("OK: 守卫顺序 = ACL 禁令 -> 角色断言(非 slave 拒绝) -> 备份 -> 执行")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么从库载入 RDB 前必须清空自身数据？
→ 一句话提示：副本的语义是"与主库完全一致"，全量 RDB 是主库某时刻快照，残留旧数据会造成新旧混合的不一致集合；清空是保证最终一致的最简实现。

**追问 2**：Cluster 模式下误操作一台主节点，除了清库还有什么连锁？
→ 一句话提示：槽位归属未变但数据没了，客户端拿到 MOVED 却读不到数据；需从其它副本恢复该槽段数据并核对 `CLUSTER SLOTS`，期间配合 Q6582 的拓扑刷新问题。

## 背诵要点
- `REPLICAOF` 语义 = 放弃本地数据做忠实副本：全量同步前清空自身，无 undo；误敲到主库 = 立即清库。
- 防线：ACL 禁 `replicaof`（6.0+）> rename-command > 流程断言（`role` 非 slave 拒绝执行）+ 变更前备份。
- Cluster 主库被误清 → 槽位数据丢失 + MOVED 风暴，靠其它副本回灌并核对槽完整性。

## 复盘追问
- 应急场景里 ACL 禁令会不会反而拖慢故障切换？提示：预置固定逻辑的自动化脚本（专用账号）+ 工单快速通道，权限收敛与速度靠预授权脚本平衡。
- 如何设计"复制拓扑变更"的标准操作剧本？提示：读角色 → 备份确认 → ACL 校验 → 执行 → role/offset 验证 → 回滚路径（REPLICAOF NO ONE + 回挂）。
