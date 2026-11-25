---
title: [WCN-621] 笔试：实现跨 Shadow 边界的 ARIA ID 引用修复器（aria-labelledby 指向外部元素）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-621：笔试：实现跨 Shadow 边界的 ARIA ID 引用修复器（aria-labelledby 指向外部元素）

**答**：
- 需求：WC 内部 aria-labelledby='external-id' 引用主文档（或父 shadow）的元素，浏览器无法跨树解析。实现 fixAriaRefs(host)，把引用元素的内容/可访问名复制到 shadow 内并改写引用。
- 思路：从 host 向外查找 refId（getRootNode 逐层）；找到后取其 textContent 写入 shadow 内一个克隆节点，并让 aria-labelledby 指向该克隆。
- 边界：refId 不存在要清理悬空引用；引用变化时要更新（MutationObserver 或重跑）；保持幂等。

```javascript
function fixAriaRefs(host) {
  const root = host.shadowRoot;
  if (!root) return;
  root.querySelectorAll('[aria-labelledby],[aria-describedby]').forEach(el => {
    for (const attr of ['aria-labelledby', 'aria-describedby']) {
      const ids = (el.getAttribute(attr) || '').split(/\s+/).filter(Boolean);
      const resolved = ids.map(id => {
        const target = host.getRootNode().getElementById?.(id)
          || document.getElementById(id);
        if (!target) { el.removeAttribute(attr); return null; }
        let clone = root.querySelector(`[data-aria-clone="${id}"]`);
        if (!clone) {
          clone = document.createElement('span');
          clone.dataset.ariaClone = id;
          clone.hidden = true;
          root.appendChild(clone);
        }
        clone.textContent = target.textContent || target.getAttribute('aria-label') || '';
        return clone.id || (clone.id = `ds-aria-${id}`);
      }).filter(Boolean);
      if (resolved.length) el.setAttribute(attr, resolved.join(' '));
    }
  });
}
fixAriaRefs(document.querySelector('ds-dialog'));
```

**评分点**：
- 能跨越 host.getRootNode() 逐层查找引用元素（不只 document）。
- 复制可访问名到 shadow 内并改写引用，使浏览器可解析。
- 悬空引用（找不到目标）正确清理，避免 aria 指向空。
- 幂等 + data-aria-clone 复用克隆节点，避免重复追加。
