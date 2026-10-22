# 126 QPS 怎么算，用哪个状态变量

> 分类：管理监控 | 难度：L2 | 题型：八股题 | 频率：高 | 关键词：**QPS** / **Questions** / **Com_*** / **Uptime** / **差值采样**
> 原文锚点：第 53~79 段「把 com 开头的全局变量计数器汇总，两次采样的差值除以两次采样的时间差」

## 一句话总述
QPS = **一段时间内请求数的增量 ÷ 时间增量**，用 `Questions`（或全部 `Com_*` 之和）配合 `Uptime` 做两次采样求差。

## 面试官视角
- **考察意图**：会不会只看监控大盘数字，说不出这个数字是怎么来的。
- **P5** 知道 QPS 是每秒请求数 / **P6** 能写出「两次采样求差 / 时间差」的公式 / **P7** 会补「`Questions` 含**管理命令与存储过程内语句**，`Com_*` 不含，所以两者口径不同，趋势比绝对值更有用」。
- **红旗**：「QPS 就是 select 数」；「直接读一次状态变量就是 QPS」；「QPS 越高越好」。
- **惊艳点**：`Questions` 与 `Com_select+Com_insert+...` 之和**通常不相等**——前者还统计了 `COM_PING`、`COM_STATISTICS` 等协议命令 —— 验证：同时查询两类变量对比（8.0.36 `[经验]`）。

## 主问答
**Q：MySQL 的 QPS 是怎么算出来的？**
**A：**
1. **先给结论**：`QPS = (Questions₂ − Questions₁) / (Uptime₂ − Uptime₁)`，两次采样求差。
2. **再给机制**：`Questions`（以及 `Com_*` 系列）是**自实例启动以来的累计计数器**，本身不是速率；`Uptime` 是已运行秒数，两者组合才能换算成速率。
3. **最后给边界**：`Questions` 包含 DML、DDL 与**管理类命令**，`Com_*` 只统计 SQL 语句级执行次数，两个口径不能混用；采样间隔太短（<1 秒）噪声大，太长则掩盖毛刺。
**加分层**：生产监控一般取 10~60 秒窗口，并同时看 `Threads_running`，才能判断是「请求多」还是「请求卡住」。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | QPS 全称 | 概念 | 每秒查询数 | 换题 |
| L2 | 用哪个变量 | 基础 | Questions 或 Com_* | 判 P5 |
| L3 | 为什么要求差 | 机制 | 计数器是累计值 | 判 P6 |
| L4 | 两个口径差在哪 | 边界 | Questions 含管理命令 | 判 P6+ |
| L5 | 采样窗口怎么定 | 实战 | 10~60 秒，配合并发数看 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 5.6~8.0（验证 8.0.36） | 状态变量一直是累计计数器语义，无版本翻转 | 直接用 `SHOW GLOBAL STATUS` 采样求差 |

## 关键代码
```sql
-- 两次采样（间隔 10 秒），手动算 QPS
SHOW GLOBAL STATUS LIKE 'Questions';
SHOW GLOBAL STATUS LIKE 'Uptime';
-- 一条语句直接出结果（会话级两次取值相减）
SELECT (SELECT VARIABLE_VALUE FROM performance_schema.global_status WHERE VARIABLE_NAME='Questions') /
       (SELECT VARIABLE_VALUE FROM performance_schema.global_status WHERE VARIABLE_NAME='Uptime') AS qps_avg;
```

## ⚠️ 原文纠错
原文说「QPS 包括 DML 和 DDL 语句以及管理命令」——按官方对 `Questions` 的定义，它统计的是**服务器执行的语句数（不含存储过程内部语句）**，管理命令如 `COM_PING`/`COM_STATISTICS` 计入 `Questions` 但**不计入 `Com_*`**；已按官方口径写明两者差异，避免混用。机翻「quiris / showg / comupda」还原为 **`Questions` / `SHOW GLOBAL STATUS` / `Com_update`**。未发现其他技术错误。

## 总结与追问预判
- 累计计数器 + 两次采样 = 速率，口径要统一。
- 下一题：见 127（TPS 口径）、128（并发数与连接数）。
