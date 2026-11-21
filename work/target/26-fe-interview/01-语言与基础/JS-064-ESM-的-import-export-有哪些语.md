---
title: [JS-064] ESM 的 import/export 有哪些语法形式？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-064：ESM 的 import/export 有哪些语法形式？

**答**：
- 命名导出：`export const x` / `export { a, b as c }`；默认导出：`export default`，一个模块只能一个。
- 导入：默认导入、命名导入、命名空间 `import * as ns`、副作用导入 `import './style.css'`。
- export 是**只读视图**（live binding）：导出值变化，导入方能看到更新。
- import 声明会被提升，必须位于模块顶层。

```javascript
// utils.js
export const version = '1.0';
export function format(s) { return s.trim(); }
export default class Logger { /* ... */ }
export { format as fmt }; // 重命名导出

// main.js
import Logger from './utils.js';            // 默认导入
import { version, fmt } from './utils.js';  // 命名导入
import * as utils from './utils.js';        // 命名空间
import './polyfill.js';                     // 副作用导入

// 动态导入（见 JS-066）
const mod = await import('./utils.js');

// live binding
// counter.js: export let n = 0; export function inc() { n++ }
// main.js: import { n, inc } from './counter.js'; inc(); console.log(n); // 1
```
