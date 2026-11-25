---
title: [JS-323] 模块循环引用：ESM 与 CJS 的行为差异
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 模块]
type: 面试题
---

## JS-323：模块循环引用：ESM vs CJS

**答**：
- CJS：循环时返回「部分导出的缓存对象」——a.js 先执行，b.js 拿到的 a 导出对象只有已执行部分；「函数声明提升」常救场
- ESM：编译期静态分析建依赖图 → 声明提升（var 初始化前为 TDZ）→ 循环引用在「绑定层」解决——引用晚求值即可正常（实时绑定）
- ESM 的坑：循环中在顶层直接访问未初始化的 let/const 会 ReferenceError；函数声明安全（提升）
- 工程守则：拆公共模块消除循环（根治）；循环不可避免时「延迟调用」不用顶层求值
- 面试话术：能讲出「CJS 值拷贝 vs ESM 实时绑定」的根本差异即扎实

```javascript
// ESM 循环安全写法
// a.js
import { helper } from './b.js';
export function main() { return helper(); }   // 函数声明：调用时才解析，安全
// ❌ export const x = helper();  // 顶层求值：循环时 b 未就绪，TDZ

// CJS 部分导出现象
// a.js: exports.a = 1; require('./b')
// b.js: const a = require('./a'); console.log(a.a) // 1（已导出部分）
```
