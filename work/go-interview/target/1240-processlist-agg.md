# 1240 processlist 聚合分析：定位问题客户端与长 SQL

> 分类：数据库 / MySQL 锁 | 难度：L4 | 题型：实操题 | 频率：中 | 关键词：**聚合排查、GROUP BY、长事务、Sleep 过滤、批量 KILL**

> 原文锚点：第 25~29 段「通过客户端的 IP 进行分组，分组之后通过客户端的连接数进行排序，并且是逆序排序…可以找出最耗时的 SQL，通过 time 字段进行排序…需要过滤出 command 不等于 sleep 的状态…找出超过三分钟的 SQL，通过时间逆序排序，使用 concat 函数拼接出 kill 语句」

## 一句话总述
把 `information_schema.PROCESSLIST` 当表聚合，可一次回答三个实战问题：**哪个客户端连接最多**、**哪条 SQL 跑得最久**、**哪些超时会话需要清理**。

## 面试官视角
P6 会敲 `SHOW PROCESSLIST` 肉眼看；P7 要能写出**可复用的聚合 SQL**，并指出终止会话属高危操作、需二次确认。

## 主问答
**Q（面试官原话）：** 几百个连接，你怎么快速找出谁在拖垮数据库？

1. **按客户端 IP 分组**：对 HOST 分组统计连接数并倒序，连接数最多者最可疑 `[源码]`。
2. **找最耗时语句**：按 TIME 倒序排列，即看到执行时间最长的会话 `[源码]`。
3. **必须过滤空闲连接**：排除 `COMMAND = 'Sleep'`，否则结果被空闲会话淹没 `[源码]`。
4. **设时间阈值**：如筛出持续超过 3 分钟的会话，聚焦真正阻塞的请求 `[源码]`。
5. **拼接终止语句**：用字符串拼接函数自动生成终止会话的语句，复制后执行即可批量清理 `[源码]`。
6. **先观察再动手**：终止会话属高危操作，先记录 ID 与 INFO，确认非核心业务再执行 `[经验]`。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 怎么找连接数最多的客户端？ | 按 HOST 分组 |
| L2 | 怎么找最慢的 SQL？ | 按 TIME 倒序 |
| L3 | 为什么要过滤空闲连接？ | 空闲会话会淹没结果 |
| L4 | 如何批量清理？ | 拼接生成终止语句 |
| L5 | 终止会话有什么风险？ | 需二次确认业务影响 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| MySQL 5.x / 8.0 | processlist 表均可查 | 用 SQL 聚合替代肉眼排查 |
| 8.0 起 | 部分状态迁 performance_schema | processlist 仍是最快入口 |
| 所有版本 | TIME 单位为秒 | 阈值按秒设定 |
| 所有版本 | 终止会话 | 属高危操作，需审批 |

## 关键代码
```sql
-- 1) 按客户端 IP 分组，找出连接数最多的客户端
SELECT SUBSTRING_INDEX(HOST, ':', 1) AS client_ip, COUNT(*) AS conns
FROM information_schema.PROCESSLIST
GROUP BY client_ip
ORDER BY conns DESC;

-- 2) 排除空闲连接，找出执行时间最长的会话
SELECT ID, USER, HOST, DB, TIME, STATE, INFO
FROM information_schema.PROCESSLIST
WHERE COMMAND <> 'Sleep'
ORDER BY TIME DESC
LIMIT 10;

-- 3) 筛出持续超过 3 分钟(180 秒)的会话，并自动生成终止语句
SELECT ID, TIME, INFO, CONCAT('KILL ', ID, ';') AS kill_stmt
FROM information_schema.PROCESSLIST
WHERE COMMAND <> 'Sleep' AND TIME > 180
ORDER BY TIME DESC;
```

## 总结与追问预判
**聚合三问：谁连得多、谁跑得久、谁该清理**。务必补一句「终止会话是高危操作，要先记录上下文并确认业务影响」——这是区分 P6 与 P7 的关键。锁的明细查法见同批 1240-lock-views。

## ⚠️ 原文纠错
1. 事实核校：按 HOST 分组统计连接数、TIME 倒序找长 SQL、过滤空闲连接、阈值筛选、拼接生成终止语句——均为生产常用手法 `[经验]`。
2. 补充：原文示例直接用 HOST 分组，实际 HOST 含端口号，同一客户端不同端口会被拆散，应按端口号前的 IP 部分分组 `[经验]`。
3. 崩坏词归一：源码将分组、排序、过滤、拼接等 SQL 关键字音译为多组崩坏词，本卡统一为规范写法 `[经验]`。
