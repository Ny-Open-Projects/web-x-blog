---
title: [WCN-429] 笔试：实现 slot 内容的分布检查（哪些 light DOM 节点落到哪个 slot）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-429：笔试：实现 slot 内容的分布检查（哪些 light DOM 节点落到哪个 slot）。
**题目**：`slotMap(el)`：返回 `{slotName: [node...]}`（assignedNodes 展平，含默认 slot 'default'）。用于文档调试与测试断言。

```javascript
function slotMap(el, { ignoreWhitespace = true } = {}) {
  const map = {};
  for (const slot of el.shadowRoot.querySelectorAll('slot')) {
    const name = slot.name || 'default';
    map[name] = slot.assignedNodes().filter(n =>
      !(ignoreWhitespace && n.nodeType === 3 && !n.textContent.trim()));
  }
  return map;
}
// 测试：expect(slotMap(el)['header']).toEqual([headerNode])

```

**评分点**：
- shadowRoot.querySelectorAll('slot') 逐个 assignedNodes。
- 默认 slot（无 name）记 'default'。
- 过滤空文本节点（选项）。
- 输出顺序保持文档序。
