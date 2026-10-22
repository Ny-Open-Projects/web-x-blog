# 128 并发数与连接数：两个别混为一谈的指标

> 分类：管理监控 | 难度：L2 | 题型：八股题 | 频率：高 | 关键词：**Threads_running** / **Threads_connected** / **max_connections** / **sleep**
> 原文锚点：第 87~103 段「并发数是同时运行的线程数；连接数包括正在执行的和处于 sleep 状态的会话」

## 一句话总述
**并发数** = `Threads_running`（真正在跑的线程）；**连接数** = `Threads_connected`（含大量 sleep）。前者对标 **CPU 核数**，后者对标 `max_connections`。

## 面试官视角
- **考察意图**：这是最经典的一对易混指标，答混了基本等于没做过容量评估。
- **P5** 知道两个变量名字 / **P6** 能说清 sleep 会话拉高连接数但不消耗 CPU / **P7** 会补「并发数持续 > CPU 核数说明线程在排队；连接数/max_connections > 80% 就该告警」。
- **红旗**：「连接数高说明数据库忙」；「并发数就是连接数」；「max_connections 越大越好」。
- **惊艳点**：`Threads_running` 长期高于 CPU 核数，说明**线程在等锁/等 IO** 而不是在算——这时加 CPU 没用，要去查锁和慢查（8.0.36 `[经验]`）。

## 主问答
**Q：并发数和连接数有什么区别？分别怎么设告警？**
**A：**
1. **先给结论**：并发数看 `Threads_running`，连接数看 `Threads_connected`；前者超 CPU 核数要警惕，后者与 `max_connections` 比值超 **80%** 要告警。
2. **再给机制**：多数连接处于 **sleep** 状态（应用持连接但不发请求），它们占连接槽位、占一点内存，但**不占 CPU**；只有 `Threads_running` 里的线程才真正消耗 CPU 与锁资源。
3. **最后给边界**：`max_connections` 一旦打满，新连接直接被拒，前端报 `Too many connections`；但把它调得过大，会在高负载时引入**大量上下文切换与内存开销**，反而加速雪崩。
**加分层**：连接数打满先查应用侧连接池泄漏，别急着调大 `max_connections`——那通常只是把问题推迟。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 两个变量叫什么 | 概念 | running / connected | 换题 |
| L2 | sleep 算连接数吗 | 基础 | 算 | 判 P5 |
| L3 | 并发数超核数说明什么 | 机制 | 线程在排队等锁等 IO | 判 P6 |
| L4 | 打满会报什么错 | 边界 | Too many connections | 判 P6+ |
| L5 | 打满了先查什么 | 实战 | 应用连接池是否泄漏 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 5.6~8.0（验证 8.0.36） | `max_connections` 默认一直是 151；8.0 起可用 `Admin_port` 保留管理员连接 | 答 80% 阈值 + 管理员应急连接思路 |

## 关键代码
```sql
-- 并发数 vs 连接数 vs 上限：一次看全
SELECT
  (SELECT VARIABLE_VALUE FROM performance_schema.global_status WHERE VARIABLE_NAME='Threads_running')   AS running,
  (SELECT VARIABLE_VALUE FROM performance_schema.global_status WHERE VARIABLE_NAME='Threads_connected') AS connected,
  @@max_connections AS max_conn,
  ROUND(CAST((SELECT VARIABLE_VALUE FROM performance_schema.global_status WHERE VARIABLE_NAME='Threads_connected') AS UNSIGNED)
        / @@max_connections * 100, 1) AS used_pct;
```

## ⚠️ 原文纠错
原文「一旦连接数超过 max_connections，新的请求就无法建立连接」正确；但原文把并发数笼统描述为「同时运行的数据库请求数」而未强调它**与 sleep 会话无关**，也未给出 80% 告警阈值以外的判据（并发数 vs CPU 核数），已补全。机翻「mxconnection / sysrining」还原为 **`max_connections` / `Threads_running`**。未发现其他技术错误。

## 总结与追问预判
- running 看忙不忙，connected 看槽位够不够，两把尺子。
- 下一题：见 129（缓冲池命中率）、126（QPS）。
