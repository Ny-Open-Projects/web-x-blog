---
title: [WCN-073] 笔试：手写 Signals 驱动的 DOM 绑定器（bind-text / bind-class / 列表 keyed 更新）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-073：笔试：手写 Signals 驱动的 DOM 绑定器

**题目**：实现绑定助手：① `bindText(el, sig)` — signal 变化直接改 textContent；② `bindClass(el, sig, map)` — 值到 class 的映射切换；③ `bindList(container, sigList, rowTpl, keyOf)` — keyed 列表更新：新增 append、删除 remove、复用同 key 节点只更新内容（不做全量重建）；④ 全部返回 dispose；⑤ 使用上题的 effect。

**答**：

```javascript
import { effect } from './mini.js';

export function bindText(el, sig) {
  return effect(() => { el.textContent = String(sig()); });
}

export function bindClass(el, sig, map) {
  return effect(() => {
    const v = sig();
    for (const [val, cls] of Object.entries(map)) {
      el.classList.toggle(cls, val === String(v));
    }
  });
}

export function bindList(container, sigList, rowTpl, keyOf) {
  const nodes = new Map(); // key -> { el, item }
  return effect(() => {
    const list = sigList();
    const seen = new Set();
    let cursor = container.firstChild;
    for (const item of list) {
      const k = keyOf(item);
      seen.add(k);
      let node = nodes.get(k);
      if (!node) {
        node = { el: rowTpl(item), item };
        nodes.set(k, node);
        container.insertBefore(node.el, cursor ?? null); // 就地插入保持顺序
      } else {
        rowTpl(node.el, item);            // 复用：更新内容
      }
      cursor = node.el.nextSibling;
    }
    for (const [k, node] of nodes) {      // 删除消失的 key
      if (!seen.has(k)) { node.el.remove(); nodes.delete(k); }
    }
  });
}

// 口径：
// bindList(ul, itemsSig,
//   (el, it) => { if (!el) { el = document.createElement('li'); } el.textContent = it.name; return el; },
//   (it) => it.id);
```

**评分点**：
- keyed 复用：Map 按 key 存节点，同 key 就地更新不重建（DOM 复用是考点）。
- 顺序维护用 insertBefore + cursor（与 diff 算法思想一致）。
- 每个绑定返回 dispose，随组件销毁。
- bindClass 用 classList.toggle 而非重写 className（保留外部传入的其他 class）。
