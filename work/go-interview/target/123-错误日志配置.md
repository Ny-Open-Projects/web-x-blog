# 123 错误日志配置

> 分类：MySQL 日志 | 难度：L2 | 题型：八股题 | 频率：中 | 关键词：**log_error**/**log_error_verbosity**/**perror**
> 原文锚点：第 7~21 段「错误日志与 log_error_verbosity 配置」

## 一句话总述
错误日志记录 MySQL 服务的启动、运行、关闭异常，路径由 `log_error` 指定，详细程度由 `log_error_verbosity` 控制。

## 面试官视角
- 考察意图：能否定位启动失败/崩溃，并说清 `log_error_verbosity` 的版本演变。
- 分档：P5 知错误日志看异常；P6 知 verbosity 级别；P7 能讲 5.7↔8.0 改名。
- 红旗答案：把错误日志和 binlog 混为一谈。
- 惊艳点：点出 `perror <code>` 直接读错误码含义。

## 主问答
**Q（面试官原话）：** 怎么定位 MySQL 启动失败或崩溃？
**A：**
1. **路径配置**：`log_error` 指定文件位置；8.0 默认已给路径，用 `SHOW VARIABLES LIKE 'log_error'` 查。
2. **详细级别 `log_error_verbosity`**：`0` 禁用、`1` 仅错误、`>1`（如 2）额外记失败连接与拒绝访问；8.0 默认 **2**。
3. **版本改名**：5.7 及之前叫 `log_warnings`（5.5 默认 1、5.7 默认 2），8.0 统一改名 `log_error_verbosity`，默认仍 2。
4. **错误码解读**：`perror 1009` 打印错误码含义（1009=删除库出错）。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 错误日志记什么？ | 基础 | 启动/运行/关闭异常 | P5 |
| L2 | 怎么看路径？ | 操作 | SHOW VARIABLES LIKE 'log_error' | P6 |
| L3 | verbosity=2 多了啥？ | 细节 | 失败连接+拒绝访问 | P6 |
| L4 | 8.0 与 5.7 参数名为何不同？ | 版本 | 5.7 log_warnings→8.0 改名 | P7 |
| L5 | 怎么读错误码？ | 进阶 | perror <code> | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| MySQL 5.5+ | 8.0 将 `log_warnings` 改名 `log_error_verbosity` | 默认均为 2；5.7 用 log_warnings，8.0 用 log_error_verbosity |

## 关键代码
```sql
SHOW VARIABLES LIKE 'log_error%';
```
```bash
perror 1009
```

## 总结与追问预判
错误日志是排障入口：`log_error` 定路径、`log_error_verbosity` 定详细度；8.0 改名但语义延续，`perror` 配合读码。

## ⚠️ 原文纠错
1. 事实核校： [经验]`log_warnings`（5.5 默认 1、5.7 默认 2）→ 8.0 改名 `log_error_verbosity`（默认 2），正确。
2. 崩坏词归一：logoerrorverversity/logo沃敏/logoarroverversity→log_error_verbosity、马刺go八点零→MySQL 8.0、PIL→perror、幺零零九→错误码 1009、桌频数据→表数据。
