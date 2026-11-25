---
title: [WCN-723] 流式 SSR 下 WC 如何做渐进式 hydration 与占位策略？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-723：流式 SSR 下 WC 如何做渐进式 hydration 与占位策略？

**答**：
- 结论：服务端输出自定义元素的「影子标记 + 骨架 slot」，客户端按流到达顺序用 customElements.whenDefined 分块激活；未激活区域保留骨架避免布局跳动。
- 用 `hydration` 属性或注释锚点标记激活边界，按视口优先级调度（首屏优先、below-fold 延后）；激活时复用服务端 DOM 而非重建。
- 追问钩子：客户端激活时服务端 DOM 与本地状态不一致（如时间、随机数）怎么办？考察 hydration mismatch 的规避（确定性渲染 + 激活后修正）。

```javascript
// 流式激活调度器（简化）
function hydrateWhenReady(root) {
  const candidates = [...root.querySelectorAll('[data-ssr-wc]')];
  // 按是否在视口内排序：首屏优先
  candidates.sort((a, b) =>
    (b.getBoundingClientRect().top < innerHeight) - (a.getBoundingClientRect().top < innerHeight));
  for (const el of candidates) {
    const tag = el.localName;
    customElements.whenDefined(tag).then(() => {
      el.removeAttribute('data-ssr-wc');         // 复用 DOM，标记已激活
      el.dispatchEvent(new Event('hydrated'));
    });
  }
}
hydrateWhenReady(document);
```
