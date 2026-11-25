---
title: [RBL-274] 构建产物怎么支持增量更新（HMR 传输层设计）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-274：构建产物怎么支持增量更新（HMR 传输层设计）

**答**:
- 传输两种：全量模块替换（重新请求更新后的模块 URL，Vite ESM 式）vs patch 式（服务端算 diff，客户端应用——省传输但实现复杂）
- ESM 式实现：变更模块 URL 加时间戳 query（module.js?t=123）→ import 刷新缓存 → accept 回调重新执行
- 边界：循环依赖的更新顺序（拓扑排序模块图保证依赖先更新）、副作用的 dispose 语义（旧模块清理再替换）
- 选择建议：通用场景全量模块替换够用且简单；超大模块（低代码引擎 bundle）才值得 patch 式

```text
ESM 式流程：
1. WS 收 { updates: ["/src/a.js?t=123"] }
2. 动态 import 更新模块 → module.hot.accept 处理
3. 旧模块 dispose 清理 → 新模块执行
```
