---
title: [WCN-103] WCN 在 Vue 中如何封装？defineCustomElement 与双向数据桥怎么做？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 跨框架复用]
type: 面试题
---

## WCN-103：WCN 在 Vue 中如何封装？defineCustomElement 与双向数据桥怎么做？

**答**：
- Vue 官方 `defineCustomElement(SFC)`：把 Vue 组件编译为自定义元素，props 自动映射为 attribute/property，emit 的事件成为 CustomEvent（kebab-case，需 `emits` 声明）。
- 方向一（Vue → WCN）：Vue 项目直接消费第三方 WC——`<x-card :user-id="id" @x-change="onChg">`；Vue 会给有对应 property 的 props 走 property 传递。
- 方向二（WCN 内部用 Vue）：组件逻辑用 Vue 写、对外是 WC；注意内部 createApp 生命周期要映射到 connected/disconnected。
- v-model 双向桥：WC 派发 `input`/`change`（或 `update:modelValue`）+ 接收 modelValue prop，Vue 侧即可 `v-model`；defineCustomElement 会自动转换 modelValue/`update:modelValue` 对。
- 坑：defineCustomElement 的样式编译进影子树（scoped 仍有效）；teleport/插槽复杂场景语义受限——复杂组件建议"WC 壳 + Vue 内容投影"或反向。

```javascript
// MyCard.ce.vue 编译为 WC
import { defineCustomElement } from 'vue';
import MyCard from './MyCard.ce.vue';

export const XMyCard = defineCustomElement(MyCard);
customElements.define('x-my-card', XMyCard);
// MyCard.ce.vue 内：
// props: { userId: Number }        → <x-my-card user-id="42">
// emits: ['update:modelValue']     → v-model 可用
```
