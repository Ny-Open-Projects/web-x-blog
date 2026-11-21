---
title: [BAS-039] debugger 语句和断点怎么配合使用？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-039：debugger 语句和断点怎么配合使用？
**答**：
- 代码里写 `debugger;`，DevTools 打开时执行到该行自动暂停，等于硬编码断点。
- Sources 面板行号右键可加条件断点（满足条件才停）和 Logpoint（只打日志不暂停）。
- 暂停时看 Scope 作用域、Watch 表达式、Call Stack 调用栈；上线前用构建配置移除 debugger。

```javascript
function avg(list) {
  const total = list.reduce((s, n) => s + n, 0);
  debugger; // DevTools 打开时在此暂停，检查 list 与 total
  return total / list.length;
}
```
