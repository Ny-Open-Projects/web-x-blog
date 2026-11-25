---
title: [SCN-1210] AI 对话的会话分支与编辑重发（树状对话）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1210：AI 对话的会话分支与编辑重发（树状对话）

**答**：
- 树状：编辑历史消息重发 → 分支对话（树结构），切换分支查看不同走向。
- 实现：消息带 parentId，切换分支重渲染路径；分支数与 token 成本提示。
- 交互：版本切换器（< 2/4 >）切换同级分支。

```javascript
// 树状对话
class ConversationTree {
  constructor() { this.nodes = new Map(); }
  add(parentId, msg) {
    const id = crypto.randomUUID();
    this.nodes.set(id, { id, parentId, ...msg, children: [] });
    if (parentId) this.nodes.get(parentId).children.push(id);
    return id;
  }
  pathTo(nodeId) {
    const path = [];
    let cur = nodeId;
    while (cur) { path.unshift(this.nodes.get(cur)); cur = this.nodes.get(cur).parentId; }
    return path;
  }
  siblings(nodeId) {
    const n = this.nodes.get(nodeId);
    return n.parentId ? this.nodes.get(n.parentId).children : [];
  }
}
```
