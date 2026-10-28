---
disableNunjucks: true
title: "059 binlog_cache_size 与落盘判据"
date: 2026-10-16 02:16:14
categories: [MySQL面试题集]
tags: [MySQL面试题集]
---

> 分类：服务器配置 | 难度：L3 | 题型：工程题 | 频率：中 | 关键词：**binlog_cache_size** / **Binlog_cache_disk_use** / **大事务**
> 原文锚点：第 314~316 段「binlog_cache_size 是基于会话的一个参数…设置的太小时就会发生写磁盘的情况…相关的状态值 Binlog_cache_disk_use 和 Binlog_cache_use，可以通过这两个数值判断 binlog_cache_size 是否过大或者过小」

## 一句话总述
`binlog_cache_size` 是**会话级**的未提交事务 binlog 缓冲；太小会把 binlog 溢写到临时文件，判据就是 `Binlog_cache_disk_use` 是否大于 0。

## 面试官视角
- **考察意图**：看你会不会用**状态量**而非感觉调参，是否理解大事务的内存放大路径。
- **P5** 知道是会话级、缓存未提交 binlog / **P6** 说出两个判据 / **P7** 给出"看比值→调→复测"闭环并指出根因是大事务。
- **红旗**：① 直接给个 1M 不说判据；② 不知会话级会按连接数放大；③ 认为 disk_use > 0 就必调大。
- **惊艳点**：`Binlog_cache_disk_use / Binlog_cache_use` 抬升往往是**单事务写入量过大**的信号，先拆事务再谈调参 `[经验]` —— 验证：两次 `SHOW GLOBAL STATUS LIKE 'Binlog_cache%';` 取差值。

## 主问答
**Q（面试官原话）：** binlog_cache_size 设多大合适？怎么判断够不够？

**A：**
1. **先给结论**：默认 32KB 通常够用，用 `Binlog_cache_disk_use` 是否为 0 判断，别凭感觉给值。
2. **再给机制**：它是**每会话**独立分配的缓冲，暂存**未提交事务**的 binlog event，提交时整块写出；不够则溢出写磁盘临时文件，`Binlog_cache_disk_use` +1。
3. **最后给边界**：按会话分配，**调大同样按连接数放大**；disk_use 上升的根因常是**单事务改了太多行**，正解是拆批而非无限调大。

**加分层**：闭环是采样两个状态量的**增量比**，持续 >0 才调，调完复测把 disk_use 压回 0。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 这个参数缓存什么 | 概念 | 未提交事务的 binlog | 换题 → 不及格 |
| L2 | 全局还是会话 | 机制 | 会话级，按连接放大 | 判 P5 |
| L3 | 太小会怎样 | 边界 | 溢出写磁盘临时文件 | 判 P6 |
| L4 | 用什么判据 | 工程判断 | disk_use / use 比值 | 判 P6+ |
| L5 | 一直涨怎么办 | 架构判断 | 拆大事务，而非无限调大 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| 5.6 / 5.7 | 默认 32KB，会话级分配 | "默认够用，看 disk_use 决定是否调" |
| 8.0 | 仍为会话级、默认 32KB；状态量命名不变 | 同上，并补"先拆大事务" |
| 8.0（GTID 场景） | 大事务还会推高 `binlog_group_commit` 等待与复制延迟 | 大事务的危害不止内存，需一并说明 |

## 关键代码
```sql
-- 采样：取两次差值，避免被累计值误导
SHOW GLOBAL STATUS LIKE 'Binlog_cache_use';        -- 使用缓冲的事务总数
SHOW GLOBAL STATUS LIKE 'Binlog_cache_disk_use';   -- 溢写到磁盘的事务数，目标 = 0
SHOW VARIABLES LIKE 'binlog_cache_size';
SHOW VARIABLES LIKE 'max_binlog_cache_size';       -- 上限保护，超过则事务直接报错

-- 调整（会话级参数，全局调大会按连接数放大）
SET GLOBAL binlog_cache_size = 65536;              -- 仅在 disk_use 持续 >0 时调
```

## ⚠️ 原文纠错
原文"设置太小会发生写磁盘的情况"与"用这两个状态值判断是否过大或过小"均正确，未发现技术错误。需补充原文未提的两点：① 它是**会话级**参数（原文只说"基于会话"，未说明会随连接数放大）；② 存在上限保护参数 `max_binlog_cache_size`，超限事务会直接报错而非无限写盘。机翻音译（blogcachesize、belogcatchset、belogcathedeacheuse、belogcatchuse、绘画）已还原为 binlog_cache_size、binlog_cache_size、Binlog_cache_disk_use、Binlog_cache_use、会话。

## 总结与追问预判
- 会话级、默认 32KB；判据是 `Binlog_cache_disk_use` 压回 0。
- 持续落盘先**拆大事务**，别只调参数。
- 下一题：见 053（max_allowed_packet，同样是大事务参数）、054（sync_binlog）。
