---
title: [MFW-785] 分段传输与渐进增强组合
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-785：分段传输与渐进增强组合

**答**:
- 分段传输（chunked）与渐进增强（RBL-512）的协同：1) **HTML 先行**（chunked 流的 HTML 部分立即可交互——form 原生提交（JS 未加载时用户可以搜索/下单——RBL-747 纯 HTML 的流式版）；2) **JS 后到增强**（JS chunk 下载 → 水合 → 交互增强（软导航/乐观 UI——JS 加载前的提交 = 整页刷新、加载后 = 软导航）；3) **增强的时序**：chunked 流的 HTML 段先到 → 用户开始交互（填表）→ JS chunk 后到 → 水合接管（表单已填的数据保留 RBL-552 状态保持）。
- 分段传输中的「交互窗口」：HTML chunk 与 JS chunk 之间的时间窗 = 用户可以「无 JS 交互」（原生表单/链接——渐进增强的窗口）；「窗口的长度」= JS 下载+水合时间（网络慢 = 窗口长——原生交互的使用率更高）。
- 追问钩子：为什么「chunked 流式传输」让渐进增强从「理论」变「实践」？——非流式（传统 SSR）：全部 HTML+JS 同时到（用户等待完整下载——无交互窗口）；流式：HTML 先到（用户立即交互）→ JS 后到（增强）——「HTML 先行 = 渐进增强的时间窗口」：流式传输创造了「JS 未加载但 HTML 已可用」的实际窗口（RBL-747 纯 HTML 模式的流式版）；渐进增强不再是理论（无 JS 也能用）而是「真实用户的体验路径」（弱网用户先交互后增强）。

```html
<!-- chunked 流的渐进增强时序 -->
<!-- t=200ms: HTML chunk 1（shell + 表单）-->
<form action="/search" method="GET">
  <input name="q" /><button>Search</button>
</form>
<!-- 用户在 t=500ms 开始搜索（JS 未加载——原生提交）-->
<!-- t=2s: JS chunk 到达 → 水合 → 后续交互增强 -->
<!-- 提交增强：JS 后 form 提交走 RSC（软导航）-->
<!-- JS 前 form 提交走原生 POST（整页刷新——RBL-512）-->
<script>(self.__next_f=self.__next_f||[]).push(chunk)</script>
<!-- 水合后：表单提交 → server action → 乐观 UI → 软导航（增强）-->
<!-- 水合前：表单提交 → 原生 POST → 整页刷新（纯 HTML）-->
<!-- 两种路径的最终结果一致（渐进增强）——体验不同（速度）-->
```
