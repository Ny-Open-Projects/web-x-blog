---
title: [BAS-038] console 有哪些实用的调试技巧？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-038：console 有哪些实用的调试技巧？
**答**：
- log 之外：table（表格化数组对象）、group/groupEnd（分组折叠）、time/timeEnd（计时）、dir（查看对象属性）。
- 占位符：%s 字符串、%d 数字、%c 样式、%o 对象。
- 经典坑：console.log 引用类型显示的是最终状态，要看快照就断点或序列化后打印。

```javascript
console.table([{ id: 1, name: 'a' }, { id: 2, name: 'b' }]);
console.group('请求详情');
console.log('url', '/api/list');
console.time('fetch');
// await fetch('/api/list')
console.timeEnd('fetch');
console.groupEnd();
console.log('%c 重点数据', 'color:#fff;background:#f40;padding:2px 4px;');
console.log(JSON.parse(JSON.stringify(bigObj))); // 打印快照而非引用
```
