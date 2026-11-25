---
title: [BLD-274] contenthash 的陷阱有哪些？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-274：contenthash 陷阱？
**答**：
- 陷阱一：chunk 内模块 ID 不稳定（自增 ID 平移——SCN-BLD-219）→ hash 全变。
- 陷阱二：CSS 提取的 hash 只含 CSS 内容——但 CSS 文件名变化（JS chunk 名变化）时 HTML 引用更新，旧 CSS 缓存浪费。
- 陷阱三：hash 不含「影响运行时的外部因素」（Define 值变化但源码没变 → hash 不变 → 缓存脏）——Define 值必须进 hash 输入。
- 陷阱四：长缓存与「引用传染」——一个高频变更模块被多个 chunk 引用导致全部 chunk hash 变化（SCN-BLD-219 deterministic 缓解）。
- 追问钩子：为什么「Define 值必须进 hash 输入」是隐蔽的脏缓存源——`define: { __API__: '"v1"' }` 改成 v2 后，源码字节没变（代码里只有 __API__ 标识符）——contenthash 不变 → 用户 CDN 缓存的旧 chunk 仍带 v1——hash 输入必须覆盖「所有影响最终字节的输入」，Define 值是最容易被遗忘的一个。

```javascript
// hash 输入完整性
output: { hashFunction: 'sha256' },
cache: { buildDependencies: [configFile] },            // 配置变更失效
// Define 值进键
const configHash = hash(JSON.stringify(defines));       // 手动并入缓存键
```
