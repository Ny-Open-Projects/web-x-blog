---
title: [WEB-107] CORB 与 ORB 是什么？它们和 CORS 的关系是什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-107：CORB 与 ORB 是什么？它们和 CORS 的关系是什么？
**答**：
- CORB（跨域读取阻塞）：对 no-cors 模式拉来的跨源资源，若其类型与目标上下文不符（如把 HTML/JSON 塞进 `<img>`/`<script>`），在渲染进程进入解析前就把响应体清空——防 Spectre 类侧信道读跨源数据。
- 升级版 ORB（Opaque Response Blocking）放宽为按"响应是否看起来像媒体"启发式判断，覆盖更多 MIME 组合，规定于 fetch 标准化流程中。
- 与 CORS 的关系：CORS 决定 JS 能不能"合法读"，CORB/ORB 决定浏览器要不要"物理递给你"；即使没开 CORS，响应进入错误上下文也会被 ORB 清空。
- 工程意义：给所有响应返回正确 Content-Type 并加 `X-Content-Type-Options: nosniff`，既安全也让 ORB 判定无歧义。

```http
# 服务端标准配置：正确的 Content-Type + nosniff
X-Content-Type-Options: nosniff

# 场景判定：
# <script src="//api.example.com/user.json"> 跨源 no-cors 加载 JSON
# CORB/ORB 判定：JSON 与 script 上下文不兼容 -> 响应体被清空，脚本报语法错也拿不到内容
# 如果服务端把 JSON 包成合法 JS（JSONP 时代做法），内容看起来可执行 -> ORB 放行
# 结论：ORB 是渲染进程内的最后一道闸，与 CORS 的"准入判定"互补
```
