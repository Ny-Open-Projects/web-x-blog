---
title: [WCN-327] DSD 输出的元素级缓存（同 props 元素复用 HTML 片段）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-327：DSD 输出的元素级缓存（同 props 元素复用 HTML 片段）？
**答**：
- 缓存键：props 稳定序列化 + 元素版本 + 主题上下文（token 版本）。
- 缓存粒度：元素片段级（非整页）——页面组装时拼接。
- 失效：元素版本升级/token 变更 → 全量失效（版本号进键天然隔离）。
- 度量：命中率与 HTML 传输节省。

```javascript
const key = stableStringify(props) + '@' + ELEMENTS_VERSION + '@' + THEME_VERSION;
const html = cache.get(key) ?? cache.set(key, renderDSD(props));
r
```
