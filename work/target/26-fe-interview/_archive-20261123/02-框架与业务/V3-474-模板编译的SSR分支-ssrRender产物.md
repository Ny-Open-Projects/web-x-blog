---
title: [V3-474] 模板编译的 SSR 分支：ssrRender 与 hydration 标记
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 编译器]
type: 面试题
---

## V3-474：模板编译的 SSR 分支：ssrRender 与 hydration 标记

**答**：
- 双产物编译：compileTemplate 同时产出 client render 函数与 server ssrRender 函数（mode: 'base'）——SSR 产物是「字符串拼接」而非 vnode 创建
- ssrRender 特点：无 patchFlag/无静态 vnode（直接拼 HTML 字符串），事件与响应式绑定在 hydration 时才激活——服务端只产「形状」
- hydration 标记：动态部分在 HTML 上预留 data-v-xxx 与顺序匹配（无显式标记的 v3 直接按 vnode 结构匹配）——v3.4 的 optimized hydration 靠静态/动态结构跳过匹配静态部分
- 指令的 SSR 空缺：自定义指令在 SSR 侧只有 getSSRProps（服务端 props 注入）——v-loading 这类「操作 DOM 的指令」SSR 无意义，编译层自动跳过
- 深水点：ssrRender 的错误恢复——拼接中途组件报错（async setup reject）→ SSR 流降级为客户端渲染（Vue 的 SSR fallback 机制），编译层产出的结构保证可恢复

```javascript
// 同一模板双产物
render()        { return _createElementVNode('div', { onClick: ... }) }
ssrRender(ctx)  { _ssrRenderAttr('class', ...); _ssrInterpolate(ctx.msg); }
// hydration: 客户端 render 重建 vnode 与已有 DOM 匹配
```
