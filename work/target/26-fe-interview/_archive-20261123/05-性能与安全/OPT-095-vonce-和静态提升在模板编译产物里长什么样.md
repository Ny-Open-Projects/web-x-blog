---
title: [OPT-095] v-once 和静态提升在模板编译产物里长什么样？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-095：v-once 和静态提升在模板编译产物里长什么样？

**答**：
- Vue3 编译器（patchFlags）已经把"静态节点"在编译期识别并** hoist 到 render 函数外**：静态 vnode 只创建一次，每次 patch 直接跳过（`PatchFlags.HOISTED`）。
- `v-once` 是手动挡：整段子树只渲染一次，后续更新完全不 diff，适合"确定永不变"的内容（版权文案、协议条款）。
- `v-memo`/`v-pre` 是同一谱系的其他档位：v-pre 完全跳过编译、v-memo 条件跳过 diff。
- 验证方式：用 Vue SFC Playground 切到编译产物，看 `_hoisted_1` 变量与 patchFlag 数字；dynamicChildren 列表里没有的节点就是跳过 patch 的。

```vue
<!-- 一一对应：源码与其编译产物对照（可在 SFC Playground 验证） -->
<template>
  <!-- 编译器自动静态提升：div 整块静态，产物里 _hoisted_1 只建一次 -->
  <div class="banner">
    <h1>618 大促</h1>
    <p>全场满 300 减 50</p>
  </div>

  <!-- 动态部分：带 patchFlag=1(TEXT)，diff 时只比对文本 -->
  <p>{{ price }}</p>

  <!-- v-once：手动永久缓存，且内容不再进入 dynamicChildren -->
  <footer v-once>
    <span>© 2026 Example Inc.</span>
    <span>ICP 备案号 00000000</span>
  </footer>
</template>

<script>
// 对应编译产物（简化），重点看 _hoisted 与 patchFlag：
// import { createElementVNode as _createV, createTextVNode as _text } from "vue";
// const _hoisted_1 = _createV("div", { class: "banner" }, [
//   _createV("h1", null, "618 大促"),                    // 模块级常量：只创建一次
//   _createV("p", null, "全场满 300 减 50"),
// ]);                                                   // patch 时被跳过
// export function render(_ctx) {
//   return (_openBlock(), _createBlock("div", null, [
//     _hoisted_1,
//     _createV("p", null, _text(_ctx.price), 1 /* TEXT */), // patchFlag=1 只 diff 文本
//   ]));
// }
export default { name: 'StaticHoistDemo' };
</script>

<!-- 实操建议：不要为提升率手写 v-once 覆盖动态内容——
     编译器对静态内容的自动处理已覆盖 90% 场景；
     v-once 只用于"运行时确定不变"（如一次性渲染的协议全文） -->
```

## 十六、Web Worker 与并行
