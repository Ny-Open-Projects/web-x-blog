---
title: [WCN-926] 水合后事件重复绑定：服务端标记 + 客户端 hydrate 怎么避免二次 attach
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-926：水合后事件重复绑定：服务端标记 + 客户端 hydrate 怎么避免二次 attach

**答**：
- 结论先行：重复绑定通常因为「SSR 阶段绑过一次、客户端 hydrate 又绑一次」或「多次 hydrate 同一节点」；根本解法是给节点打水合状态标记，保证幂等。
- 标记方式：hydrate 前检查 `el.__hydrated` 或 `el.hasAttribute('data-hydrated')`，已水合则跳过；hydrate 完成后打标。
- 委托优于逐节点：把事件委托到文档/岛根节点，on 之前先 off（或用具名 handler 引用），避免 addEventListener 同函数重复添加。
- 框架侧：React hydration 不会重复绑定它自己管的事件，但第三方脚本/WC 手动绑定会——WC 用 `connectedCallback` 绑定要在 `disconnectedCallback` 解绑，且用标志防止重复。
- 追问钩子：面试官问「StrictMode 下 effect 跑两次怎么办」——答：清理函数必须成对（返回 off），保证第二次执行前先解绑，这正是幂等设计。

```javascript
// 幂等水合：标记 + 事件委托
function hydrateIsland(root) {
  if (root.__hydrated) return;      // 已水合，幂等返回
  root.__hydrated = true;
  const onClick = e => {
    if (e.target.matches('[data-action=buy]')) console.log('buy');
  };
  root.addEventListener('click', onClick);
  root.__cleanup = () => root.removeEventListener('click', onClick);
}
const el = document.getElementById('buy-box');
hydrateIsland(el);
hydrateIsland(el); // 第二次直接返回，不重复绑定
console.log(el.__hydrated); // true
```
