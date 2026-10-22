# 125 binlog 怎么备份：定时拷贝 vs 远程实时拉取

> 分类：备份恢复 | 难度：L2 | 题型：工程题 | 频率：中 | 关键词：**mysqlbinlog --read-from-remote-server** / **REPLICATION SLAVE** / **raw** / **binlog 保留期**
> 原文锚点：第 462~474 段「使用拷贝命令把已生成的 binlog 复制走；或利用 5.6 之后的 --read-from-remote-server 实时备份」

## 一句话总述
binlog 备份两条路：`cp` **定时拷贝**已生成的文件（简单但不能拷正在写的那个），或 `mysqlbinlog --read-from-remote-server` **伪装成从库实时拉取**（能做准实时，要求账号有复制权限）。

## 面试官视角
- **考察意图**：知不知道「备份了数据 ≠ 能恢复」——binlog 没留住，PITR 就是空谈。
- **P5** 知道要备份 binlog / **P6** 能说出两种方式的差异与权限要求 / **P7** 会补「必须配合 `binlog_expire_logs_seconds` 保留期设计，保证保留期 ≥ 全备周期 + 恢复所需窗口」。
- **红旗**：「binlog 不用备份，留在本地就行」；「实时拉取不需要权限」；「expire 设 1 天够了」。
- **惊艳点**：远程实时拉取本质就是**让 mysqlbinlog 扮演 IO 线程**，所以账号必须有 **`REPLICATION SLAVE`** 权限（8.0.36 `[经验]`）。

## 主问答
**Q：binlog 也要备份吗？怎么备？保留多久合适？**
**A：**
1. **先给结论**：必须备——任何备份都只能覆盖到备份那一刻，之后的数据**只能靠 binlog**；定时 `cp` 或 `mysqlbinlog --read-from-remote-server` 实时拉取二选一。
2. **再给机制**：`cp` 方式最简单，但**无法拷贝正在被写入的当前 binlog**，所以总会差最后一小段；实时拉取方式是 mysqlbinlog 伪装成从库向主库请求事件，能做到准实时。
3. **最后给边界**：保留期要 ≥ **全备周期 + 一次恢复操作所需时间**，否则可能出现「全备有了，但补不齐」的空档；8.0 用 `binlog_expire_logs_seconds`，5.7 用 `expire_logs_days`。
**加分层**：选择实时拉取时要注意——它和本地从库一样占用主库一个 dump 连接，节点多了要算连接数成本。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | binlog 需要备份吗 | 概念 | 需要 | 换题 |
| L2 | 最简单怎么做 | 基础 | 定时 cp | 判 P5 |
| L3 | cp 的短板 | 机制 | 拷不了正在写的文件 | 判 P6 |
| L4 | 实时拉取要什么权限 | 边界 | REPLICATION SLAVE | 判 P6+ |
| L5 | 保留期怎么定 | 实战 | ≥ 全备周期 + 恢复窗口 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 5.6 起 `--read-from-remote-server` 可用（验证 8.0.36） | **8.0.1 起 `expire_logs_days` 被 `binlog_expire_logs_seconds` 取代**（默认 30 天） | 5.7 写天数，8.0 写秒数，两个参数名都要认得 |

## 关键代码
```bash
# 方式一：定时拷贝已生成的 binlog（当前正在写的那个拷不走）
cp /data/mysql/mysql-bin.00000[0-9] /bk/binlog/
# 方式二：伪装成从库实时拉取（账号需 REPLICATION SLAVE 权限）
mysqlbinlog --read-from-remote-server --raw --host=192.168.1.91 \
  --user=repl --password=*** --stop-never mysql-bin.000001
```
```sql
-- 保留期设计：8.0 用秒，5.7 用天
SET GLOBAL binlog_expire_logs_seconds = 7*24*3600;
```

## ⚠️ 原文纠错
原文说这种方式「需要提供一个具有 replication slave 权限的用户」，正确，已保留并强化；但原文**未提保留期设计**这一配套要点，已补入主问答与追问链。机翻「replicationswiver / 靠贝 / 二级制日志」还原为 **`REPLICATION SLAVE` / cp / binlog**。未发现其他技术错误。

## 总结与追问预判
- binlog 是恢复链的最后一段，保留期要盖住全备周期。
- 下一题：见 124（binlog 增量恢复）、117（备份周期设计）。
