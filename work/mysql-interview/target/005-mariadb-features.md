# 005 MariaDB 特性与取舍

> 分类：版本选型 | 难度：L3 | 题型：对比题 | 频率：中 | 关键词：**MariaDB** / **窗口函数** / **binlog 闪回** / **Galera** / **GTID 不互通**
> 原文锚点：第 46~49、107~112 段「MariaDB 基于 5.5、窗口函数早、binlog 回滚、不支持 MGR」

## 一句话总述
MariaDB 由 MySQL 原作者另立、基于 5.5 分支发展，**新特性激进**（10.2 先支持窗口函数/CTE、binlog 闪回），但**与官方版非 100% 兼容**且不支持 MGR（用 Galera）。

## 面试官视角
- **考察意图**：是否理解 MariaDB 的差异化定位与兼容代价。
- **P5** 知道 MariaDB 是 MySQL 分支、有特性优势。
- **P6** 能说清窗口函数早于 8.0、binlog 闪回、Galera 替代 MGR。
- **P7** 能指出 GTID 不互通、迁移双向不保险的坑。
- **红旗**：说 MariaDB 和 MySQL 完全相同可无缝切换。
- **惊艳点**：点出「数据可从 MySQL 迁 MariaDB 易，反向可能出问题」`[经验]`。

## 主问答
**Q：MariaDB 和 MySQL 比有什么特点？**
**A：**
1. **结论**：MariaDB 特性激进——10.2 起支持窗口函数/CTE（早于 8.0）、有 binlog 闪回（类似 flashback）、用 Galera 集群而非 MGR。
2. **机制**：基于 5.5 源码发展，部分功能实现不同（如 GTID 生成算法），Spider 引擎做分片；安全上弱于官方版（无 super_read_only 早期、审计靠插件）。
3. **边界**：与 MySQL **非全兼容**——GTID 格式不同导致只能作从不能作主；从 MySQL 迁移到 MariaDB 容易，反向可能有问题。
**加分层**：若业务依赖 MGR 多主，MariaDB 不是直接替代品。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | MariaDB 是什么 | 概念 | MySQL 分支 | 换题 |
| L2 | 比 MySQL 强在哪 | 基础 | 窗口函数/闪回早 | 判 P5 |
| L3 | 为什么不能作 MySQL 主 | 复制原理 | GTID 格式不互通 | 判 P6 |
| L4 | 迁移 MariaDB 风险 | 判断 | 语法/GTID 差异 | 判 P6+ |
| L5 | Galera 踩过坑吗 | 实战 | 讲脑裂/流控案例 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| MariaDB 10.2+ / MySQL 8.0 | 窗口函数 MariaDB 10.2(2017) 先于 8.0(2018) | 按「特性激进+GTID 不互通」答 |

## 关键代码
```sql
-- MariaDB 原生 binlog 闪回（官方版需自行解析 binlog）
FLUSH BINARY LOGS;  -- 配合 mariadb-binlog --flashback 生成反向 SQL
```

## ⚠️ 原文纠错
原视频称「MariaDB 不支持 super_read_only」——该结论基于早期版本；MariaDB 10.1+ 已支持。答题聚焦「GTID 不互通、只能作从」这一更稳妥差异点 `[存疑]`。

## 总结与追问预判
- MariaDB = 新特性激进 + GTID 不互通 + Galera；迁移兼容性要谨慎。
- 下一题：见 006（GTID 跨版本复制）、002（四维对比）。
