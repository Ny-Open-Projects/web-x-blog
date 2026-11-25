---
title: [WCN-023] WC 组件如何避免 FOUC？define 前的占位、` :not(:defined)` 与 DSD 各怎么用？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-023：WC 组件如何避免 FOUC？define 前的占位、`:not(:defined)` 与 DSD 各怎么用？

**答**：
- 问题：`<my-card>` 在 define 前是 unknown element（inline、无样式），define 后影子树渲染，期间产生布局跳动。
- 方案一：全局占位样式 `my-card:not(:defined) { display: block; min-height: 120px; visibility: hidden }`，`:defined` 伪类在升级后自动切换，纯 CSS 零 JS。
- 方案二：把组件样式提前从影子树抽出为普通 `<link>`/`<style>` 用于 unknown 阶段，或用 DSD（Declarative Shadow DOM）直接让服务端 HTML 自带影子树。
- 方案三：懒 define + 占位骨架（skeleton light DOM），define 后内容被 slot 投影而非重挂载。
- 对比选择：全站静态内容多 → DSD 最优；SPA 内嵌 WC → `:not(:defined)` + 懒 import 足够；无 JS 可用的营销页 → 必须服务端渲染影子树。
- 追问钩子：`:defined` 只反映"是否已注册"，不代表"已渲染完成"，异步组件要自己再派发 `ready` 事件。

```html
<style>
  /* unknown element 阶段的占位：防布局跳动 */
  stat-card:not(:defined) { display: block; height: 64px; border-radius: 8px;
    background: linear-gradient(90deg, #f3f4f6 25%, #e5e7eb 50%, #f3f4f6 75%);
    background-size: 200% 100%; animation: shimmer 1.2s infinite; }
  @keyframes shimmer { to { background-position: -200% 0; } }
</style>

<stat-card value="1280">今日访问</stat-card>

<script type="module">
  // 懒加载 define；升级后 :defined 生效，占位消失
  import('./stat-card.js');
</script>
```
