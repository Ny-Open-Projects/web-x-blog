---
title: [WCN-309] 元素 API 设计规范（property/事件/slot 的约定）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-309：元素 API 设计规范（property/事件/slot 的约定）？
**答**：
- property：camelCase + 类型明确（不滥用 any）；原始值可 reflect，对象不 reflect。
- 事件：CustomEvent<T> 带 detail 类型，命名过去式/现在时约定（changed/requesting）。
- slot：语义命名 + 默认内容文档化。
- 方法：命令式方法最小化（refresh/open/close），能用 property/事件表达的优先。

```javascript
/** API 规范示例 */
class DsMenu extends HTMLElement {
  open(): void;                        // 命令式最小集
  set items(v: MenuItem[]);            // property
  on('select', h: (e: CustomEvent<{ id: string }>) => void);  // 类型化事件
}
r
```
