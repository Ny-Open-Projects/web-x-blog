---
title: [WCN-107] WCN 如何跨框架做 SSR 与路由协同？DSD 输出在 Next/Nuxt/Astro 中分别怎么落地？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 跨框架复用]
type: 面试题
---

## WCN-107：WCN 如何跨框架做 SSR 与路由协同？DSD 输出在 Next/Nuxt/Astro 中分别怎么落地？

**答**：
- 共同点：服务端都要输出 Declarative Shadow DOM（结构+样式），客户端各自 define 升级；路由层面 WC 组件本身不含路由逻辑，导航归宿主框架，WC 通过事件上报意图。
- Astro：原生亲和——islands 模型下 `<script>` 组件按需加载，直接写 WC + DSD 静态页最省；`client:load` 控制 define 时机。
- Nuxt：插件里注册全局组件映射（`createElement('x-card')` 或 vue defineCustomElement 包装），SSR 用 vue-server-renderer 输出 DSD 兼容标记。
- Next：App Router 里 WC 用 `<script type="module" defer>` 加载；服务端渲染 DSD 需自定义 JSX 转换（`shadowrootmode` 属性可直接写在 JSX 上）；事件用 React 19 原生 CustomEvent 支持。
- 路由协同模式：WC 派发 `wc-navigate` 事件 → 宿主适配层调用各自路由 API（router.push/navigate）——路由命令权始终在宿主，WC 保持路由无关。

```tsx
// Next.js App Router：DSD 标记直接可用（React 19 支持任意属性透传）
export default function Page() {
  return (
    <x-card sku="A1">
      <template shadowrootmode="open">
        <style>{cardCss}</style>
        <div className="body">服务端渲染的内容</div>
        <slot />
      </template>
      <span>宿主投影</span>
    </x-card>
  );
}
// WC 内部导航意图：
// this.dispatchEvent(new CustomEvent('wc-navigate', { detail: { to: '/cart' }, bubbles: true, composed: true }))
// 宿主适配层统一监听并调用 useRouter().push(to)
```
