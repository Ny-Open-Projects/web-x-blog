---
title: [V3-516] 笔试：手写渲染函数（模拟编译产物形态）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 编译器]
type: 笔试题
---

## V3-516：笔试：手写渲染函数（模拟编译产物形态）

**答**：手写等价于模板的 render 函数（模拟编译产物）：① 模板 `<div class="box"><span>标题</span><p>{{ msg }}</p><button @click="add">+1</button></div>`；② 产物要求：静态节点提升到函数外、动态文本带 patchFlag=1（TEXT）、事件 handler 用缓存（_cache）、button 带 patchFlag=8（PROPS）；③ 用 h/createVNode API 写出；④ 说明每个 flag 对应的更新路径。写出实现。

```javascript
import { createElementVNode as v, createTextVNode as t, openBlock, createElementBlock } from 'vue';

// 静态提升: 只创建一次
const HOISTED_SPAN = v('span', null, '标题', 1 /* STABLE */);

export function render(_ctx, _cache) {
  return (openBlock(), createElementBlock('div', { class: 'box' }, [
    HOISTED_SPAN,                                              // 静态: patch 跳过
    t(_ctx.msg, 1 /* TEXT */),                                 // 只修 textContent
    v('button', {
      onClick: _cache[0] || (_cache[0] = (...args) => _ctx.add(...args)),  // handler 缓存
    }, '+1', 8 /* PROPS */, ['onClick']),                      // 只 diff onClick prop
  ]));
}
// flag 1(TEXT)   → patch 时只调 node.textContent = v
// flag 8(PROPS) → 只对比 dynamicProps 数组里的 prop
// 缓存 handler → props 浅比较稳定, 子组件不重渲
```

**评分点**：
- 静态 vnode 提升到 render 外（复用引用）
- patchFlag 正确标注（TEXT/PROPS）与 dynamicProps 第四参数
- 事件 handler 用 _cache 缓存（引用稳定）
- 能说明各 flag 的定向更新路径
