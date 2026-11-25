---
title: [WEB-405] Coverage 面板和 Tree-Shaking 有什么关系？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-405：Coverage 面板和 Tree-Shaking 有什么关系？
**答**：
- Coverage 面板记录 JS/CSS 每文件实际执行字节比例；首屏"红色长条"多 = 包大了或没按需加载。
- 构建期 Tree-Shaking 只删静态可达性未用代码；运行时未用可能来自：动态分支、第三方 SDK 全量引入、polyfill 全量。
- 动作：高红比文件按路由拆（React.lazy）、大 SDK 换按需子包（lodash-es）、polyfill 用 browserslist 精确到目标浏览器。

```javascript
import { debounce } from 'lodash-es';   // ESM 按需 → 可 shake
// 反面: import _ from 'lodash' 全量 70KB
const poly = (targets) => corejs(targets) // browserslist 定死目标
console.log('Coverage 红色比例 > 60% 的文件值得拆分');
```
