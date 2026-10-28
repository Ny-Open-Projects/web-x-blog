---
disableNunjucks: true
title: "064 log_error_services 输出组件"
date: 2026-10-16 02:26:05
categories: [MySQL面试题集]
tags: [MySQL面试题集]
---

> 分类：日志类 | 难度：L3 | 题型：工程题 | 频率：低 | 关键词：**log_error_services** / **log_sink_json** / **组件链**
> 原文锚点：第 73~77、136~154 段「这个参数的值就是以分号分割的各个错误日志组件的名称…log_filter_internal 和 log_sink_internal 是默认启用的两个错误日志组件」

## 一句话总述
8.0 起错误日志改成**组件化管线**：`log_error_services` 用**分号分隔**的组件串定义"过滤 → 输出"链路，默认 `log_filter_internal; log_sink_internal`，可换成 JSON 或系统日志输出。

## 面试官视角
- **考察意图**：考你是否知道 8.0 的错误日志架构变化，以及"日志要能被采集"的工程诉求。
- **P5** 只知道 `log_error` / **P6** 说清 8.0 用组件串、默认 internal 过滤+落盘 / **P7** 说明为何要用 JSON。
- **红旗**：① 说组件用**逗号**分隔（实际是**分号**）；② 以为开组件就不再写 `log_error` 的文件；③ 不知这是 8.0 才有的。
- **惊艳点**：切 `log_sink_json` 后日志变成**结构化记录**，省掉正则解析 `[经验]` —— 验证：改后 `tail -1 <log_error 路径>`。

## 主问答
**Q（面试官原话）：** 8.0 的错误日志能输出成 JSON 给日志系统采集吗？怎么配？

**A：**
1. **先给结论**：能。用 `log_error_services` 指定组件链，把输出组件换成 `log_sink_json`。
2. **再给机制**：它是 8.0 的组件化框架，值是**分号分隔**的组件列表，语义是从左到右的管线——先 `log_filter_*` 过滤，再 `log_sink_*` 输出；默认 `log_filter_internal; log_sink_internal`。
3. **最后给边界**：换 sink 只改**格式/目的地**，**路径仍由 `log_error` 决定**（JSON 也写进那个文件）；交给系统日志用 `log_sink_syseventlog`。改完必须**验证仍能被采集**。

**加分层**：结构化是为了**可观测性**而非好看——上 JSON sink 就要配套改采集侧解析规则。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 8.0 错误日志怎么配输出 | 概念 | log_error_services | 换题 → 不及格 |
| L2 | 默认组件是什么 | 机制 | filter_internal + sink_internal | 判 P5 |
| L3 | 分隔符是什么 | 细节 | 分号 | 判 P6 |
| L4 | 换 JSON 后路径变不变 | 边界 | 仍由 log_error 决定 | 判 P6+ |
| L5 | 什么时候值得上 JSON | 架构判断 | 有日志平台采集时 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| ≤ 5.7 | 无组件框架，只能写文件或系统日志 | "5.7 没有 log_error_services" |
| 8.0 | 引入错误日志**服务组件**框架（filter + sink） | 按组件链答，并说明默认两项 |

## 关键代码
```sql
SHOW VARIABLES LIKE 'log_error_services';
-- 默认：log_filter_internal; log_sink_internal

-- 切成 JSON 输出（仍写入 log_error 指定的文件）
SET GLOBAL log_error_services = 'log_filter_internal; log_sink_json';

-- 输出到系统日志（syslog / 事件日志）
SET GLOBAL log_error_services = 'log_filter_internal; log_sink_syseventlog';

SET PERSIST log_error_services = 'log_filter_internal; log_sink_json';  -- 持久化
```

## ⚠️ 原文纠错
原文"log_filter_internal 和 log_sink_internal 是默认启用的两个错误日志组件"正确，未发现技术错误。补充原文未强调的一点：组件串的分隔符是**分号**（原文提到"以分号来分割"，但演示中容易被忽略），写错分隔符会导致参数不生效。另：原文把 `log_sink_syseventlog` 描述为"输出到系统日志文件"正确。机翻音译（loggfutureinterneal、logshockinginterneal、jason、logcentersystemeventlog）已还原为 log_filter_internal、log_sink_internal、JSON、log_sink_syseventlog。

## 总结与追问预判
- 8.0 组件化：`log_filter_*` → `log_sink_*`，**分号**分隔。
- 换 JSON 是为了**可被采集**，不是换格式本身。
- 下一题：见 063（级别）、062（路径）。
