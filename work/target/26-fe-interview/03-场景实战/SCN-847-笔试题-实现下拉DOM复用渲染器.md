---
title: [SCN-847] 笔试题——实现下拉列表 DOM 复用渲染器（keyed diff + 同帧合并）？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-847：手写下拉复用渲染器

**需求与边界**：
- 需求：连续输入的高频数据更新用 keyed 复用（相同 sid 的行复用 DOM，只更新文本/高亮）；同帧多次数据到达合并渲染一次；消失项移除。
- 边界：① key 用 sid（服务端稳定 id）不用 index；② 位置变化用 style.order（Flex 重排）不重建；③ 渲染函数幂等（重复调用结果一致）。

**答**：
```javascript
function createReuseRenderer(container) {
  let scheduled = false, latest = null;
  function update(items) {                             // items: [{sid, text, offsets}]
    latest = items;
    if (!scheduled) {
      scheduled = true;
      requestAnimationFrame(() => { scheduled = false; render(latest); });   // 同帧合并
    }
  }
  function render(items) {
    const existing = new Map([...container.children].map(el => [el.dataset.sid, el]));
    items.forEach((item, i) => {
      let el = existing.get(String(item.sid));
      if (!el) {
        el = document.createElement('div');
        el.dataset.sid = item.sid;
        el.className = 'suggest-row';
        container.appendChild(el);
      } else existing.delete(String(item.sid));
      el.style.order = i;                              // 位置用 order，不动 DOM 结构
      const html = renderHighlight({ q: item.text, offsets: item.offsets });
      if (el.__html !== html) { el.innerHTML = html; el.__html = html; }   // 内容变化才写
    });
    existing.forEach(el => el.remove());               // 消失项移除
  }
  return { update };
}
```

**评分点**:
- sid 稳定 key（index key 会导致错位复用）。
- 同帧合并渲染（rAF 一次）。
- innerHTML 变化检测（避免无谓重写触发解析）。
- order 定位（Flex 重排不重建 DOM）+ 消失项清理。
