---
title: [OPT-016] moment→dayjs、lodash→lodash-es 这类依赖替换如何推进？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-016：moment→dayjs、lodash→lodash-es 这类依赖替换如何推进？

**答**：
- moment 全量含 locale 约 300KB 且架构上无法 tree-shaking；dayjs 核心 2KB、API 兼容，提供 adapter 式插件（timezone/duration），是官方推荐迁移目标。
- lodash CJS 全量不可摇树，换 `lodash-es`（ESM）后 `import { debounce } from 'lodash-es'` 只打包被引用的函数。
- 推进策略：先在 CI 加体积守卫暴露问题 → 新代码禁用旧库（ESLint no-restricted-imports）→ 存量按模块渐进替换。
- 类似替换还有 moment-timezone→dayjs timezone、`core-js` 全量→按 browserslist 精准 polyfill。

```javascript
// 一一对应：依赖替换前后的写法对比
// 替换前：moment 全量 300KB+，CJS 无法 tree-shaking
// import moment from 'moment';
// import 'moment/locale/zh-cn';
// moment().format('YYYY-MM-DD');

// 替换后：dayjs 核心 2KB，插件按需加载
import dayjs from 'dayjs';
import isSameOrBefore from 'dayjs/plugin/isSameOrBefore';
dayjs.extend(isSameOrBefore);

console.log(dayjs('2026-01-01').format('YYYY-MM-DD'));

// lodash 改用 ESM 版本，只打包用到的函数
import { debounce } from 'lodash-es';
window.addEventListener('resize', debounce(() => console.log('resized'), 200));
```
