# 063 log_error_verbosity 错误日志级别

> 分类：日志类 | 难度：L2 | 题型：八股题 | 频率：中 | 关键词：**log_error_verbosity** / **log_warnings** / **三个级别**
> 原文锚点：第 61~85 段「log_error_verbosity 是 MySQL 5.7 之后新增的参数，之前的版本中也有一个类似的参数叫做 log_warnings…这个参数定义了错误日志中所记录的错误信息的级别，一共可分为三个级别」

## 一句话总述
`log_error_verbosity` 控制错误日志的**记录级别**：`1` 只记 error、`2` 记 error+warning（**默认**）、`3` 再记 note；它是 5.7 新增，取代了旧的 `log_warnings`。

## 面试官视角
- **考察意图**：考一个"小参数"，看你是否知道日志**不是越详细越好**，以及版本演进。
- **P5** 知道有这么个级别参数。
- **P6** 能准确说出 1/2/3 三档含义与默认值。
- **P7** 能指出它的**前身是 `log_warnings`**，并说明线上该用哪一档。
- **红旗**：① 把级别记反（说 3 只记 error）；② 不知道默认级别是 2；③ 说"永远开 3 最保险"。
- **惊艳点**：默认级别 **2** 已经能覆盖绝大多数排障；长期开 3 会让 note 级刷屏、掩盖真正的 error `[经验]` —— 验证：`SET GLOBAL log_error_verbosity=3;` 后观察日志增量。

## 主问答
**Q（面试官原话）：** 错误日志太吵了，怎么控制它记多少东西？

**A：**
1. **先给结论**：用 `log_error_verbosity`：1=只记 error，2=error+warning（**默认**），3=error+warning+note。
2. **再给机制**：它是 5.7 引入的**动态全局**参数，取代了 5.6 及以前的 `log_warnings`；级别越高记录越全，但 note 级信息量最大。
3. **最后给边界**：**不是越详细越好**——长期开 3 会让日志被 note 淹没，反而抬高定位真正 error 的成本；建议常态保持 2，排特定问题时临时开到 3，查完调回。

**加分层**：这是全局动态参数，`SET GLOBAL` 即可生效，但要记得同步写配置文件，避免重启后回到默认值（见 045 卡）。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 有没有控制级别的参数 | 概念 | log_error_verbosity | 换题 → 不及格 |
| L2 | 三档分别记什么 | 机制 | 1 error / 2 +warning / 3 +note | 判 P5 |
| L3 | 默认是多少 | 细节 | 2 | 判 P6 |
| L4 | 5.6 里叫什么 | 版本翻转 | log_warnings | 判 P6+ |
| L5 | 线上该开几 | 工程判断 | 常态 2，临时 3 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| ≤ 5.6 | 只有 `log_warnings`，语义不同（1 表示启用 warning 记录） | "老版本用 log_warnings" |
| ≥ 5.7 | 新增 `log_error_verbosity`，默认 **2** | 按三档 1/2/3 答，并点明前身 |
| 8.0 | 沿用三档语义不变 | 同上 |

## 关键代码
```sql
SHOW VARIABLES LIKE 'log_error_verbosity';   -- 默认 2
SET GLOBAL log_error_verbosity = 3;          -- 排障期临时开到最详细
SET GLOBAL log_error_verbosity = 2;          -- 查完调回常态
SET PERSIST log_error_verbosity = 2;         -- 8.0：同时持久化，防重启回退
```

## ⚠️ 原文纠错
原文"目前一共可分为三个级别的错误信息"与官方一致；原文提到 5.7 之前有"类似参数 log_warnings"方向正确，但需补一句：**两者语义并不等价**（`log_warnings` 是 0/1/大于 1 的旧式开关，不是 1/2/3 级别），不能当同一参数沿用。机翻音译（logerrorwindows、log下划线键）已还原为 log_error_verbosity、log_warnings。

## 总结与追问预判
- 1=error、**2=error+warning（默认）**、3=再加 note。
- 常态 2，排障临时 3，改完要持久化。
- 下一题：见 062（错误日志路径）、064（错误日志输出组件）。
