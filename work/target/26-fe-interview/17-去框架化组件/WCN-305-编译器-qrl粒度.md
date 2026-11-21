---
title: [WCN-305] Qwik 的 qrl（可恢复引用）粒度设计（多大算一个 chunk）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-305：Qwik 的 qrl（可恢复引用）粒度设计（多大算一个 chunk）？
**答**：
- 粒度 = 最小可恢复单元（一个事件处理闭包），编译器按「闭包捕获集」切 chunk。
- 共享依赖提取：多个 handler 共用工具 → 共享 chunk（避免复制）。
- 粒度过细（每个 handler 一 chunk）网络请求多——合并策略（同文件 handler 打包）。
- 调试：序列化格式可读（qwik/json），可人工检查捕获集是否最小。

```javascript
// 编译器输出：handler[0] 捕获 count
export const handler = qrl(() => { console.log(count.value); }, 'chunk-a.js');
// 捕获集最小化：只序列化用到的变量
r
```
