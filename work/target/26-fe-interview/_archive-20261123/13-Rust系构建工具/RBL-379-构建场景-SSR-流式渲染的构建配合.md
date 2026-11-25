---
title: [RBL-379] SSR 流式渲染对构建的要求
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-379：SSR 流式渲染对构建的要求

**答**:
- 流式渲染链路：server 产物（node bundle）+ client 产物（hydration）+ Suspense 边界的 chunk 依赖关系——构建要保证「流式吐出的 chunk 与 client chunk 清单一致」
- 关键点：server 侧动态 import 保持（流式按需加载 segment）、client manifest 与 server 输出对齐（flush 时注入的 preload/script 正确）、CSS 流式注入（chunk css 随流输出）
- 验证：流式场景的端到端冒烟（mock 慢数据源验证流式边界 + hydration 一致）——「全量渲染对但流式错」是高发 bug
- 性能配合：server bundle 拆分（冷启动加载面小）+ 预热（server 产物预编译字节码——Node snapshot/v8-compile-cache）

```text
三件对齐：server chunk ↔ client manifest ↔ CSS 流式注入
验证：慢数据源流式冒烟 + hydration diff=0
性能：server bundle 拆分 + 字节码预热
```
