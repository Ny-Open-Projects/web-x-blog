# 136 ES 写入全生命周期（深卡）

> 分类：Elasticsearch · 写入全景 | 难度：L3 | 题型：综合题 | 频率：中 | 关键词：**routing→buffer→translog→refresh→segment→flush→merge→副本→NRT**
> 原文锚点：第 1~64 段「修改删除(segment 不可变/.del)、副本同步、落盘线程池、写入全流程(buffer→translog→refresh→segment→flush→merge)、translog 恢复、近实时」

## 思路与架构
把一次 ES 写入从"客户端"到"磁盘可恢复"串成一条主链路，并标出本卡各子主题在链路上的位置：

1. **routing 寻址**（详见 `135-coordinating-node-routing`）：协调节点 `hash(routing)%主分片数` 定位分片。
2. **主分片写 buffer + translog**：文档进内存 index buffer（不可搜）+ translog 记 OS cache。
3. **refresh（默认 1s）**：buffer → OS cache 的 segment，文档**可搜**（近实时 NRT 由此来）；get 可从 buffer 取、search 不行。
4. **flush / commit**：translog 达阈值 → buffer refresh + 写 commit point + fsync OS cache 到磁盘 + 清 translog。
5. **段合并 merge**：后台把小 segment 合成大 segment，丢弃已标记删除的文档（物理删除），耗资源、低峰调度。
6. **副本同步**（详见 `136-replica-sync`）：主成功后转发 in-sync 副本，默认异步、可 `wait_for_active_shards` 提持久性。
7. **崩溃恢复**（详见 `136-translog-recovery`）：重启读 translog 恢复内存数据，类比 binlog。

## 方案取舍
| 子机制 | 默认行为 | 调优方向 | 代价 |
| --- | --- | --- | --- |
| refresh | 1s | 调大 refresh_interval 提吞吐 | 可见延迟变长 |
| translog | request(每次 fsync) | 改 async 提吞吐 | 丢 n 秒 |
| 副本确认 | 主成功即返 | wait_for_active_shards 提可靠 | 延迟升 |
| bulk | — | 同 routing 打包收敛扇出 | 需维度划分 |

**取舍总纲**：ES 写入默认"近实时 + 高吞吐 + 主成功即返"，可靠性的每一档提升都以延迟/吞吐为代价（与 MySQL/Redis 一致性旋钮同构）。

## 答题技巧
- 被问"ES 怎么写入数据的"：按"routing → buffer+translog → refresh(NRT) → flush → merge → 副本同步 → 恢复"七步讲，比孤立说 refresh/translog 更完整。
- 被问"为什么是近实时"：归到 refresh 默认 1s——数据在 buffer 不可搜，refresh 到 OS cache 才可见。
- 被问"修改/删除怎么处理"：segment 不可变 → 删除写 `.del` 文件、更新=标记删+写新、merge 时物理删除；forcemerge `only_expunge_deletes` 强制清已删段（详见 `137-*` segment 系列，本卡不重复其机制）。
- 边界声明：本卡是**写入全景的串联与取舍总纲**。segment 不可变/段合并/force merge 的机制细节归 `137-*`（segment 系列）；refresh/translog 的调优旋钮归 `1316-refresh-translog`；routing/协调节点归 `135-*`；副本同步细节归 `136-replica-sync`；线程池 reject 归 `136-write-threadpool-reject`；translog 恢复归 `136-translog-recovery`。本卡只做整合，不重述已被专项卡覆盖的论证。
