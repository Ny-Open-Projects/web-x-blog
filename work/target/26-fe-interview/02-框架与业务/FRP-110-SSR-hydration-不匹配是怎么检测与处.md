---
title: [FRP-110] SSR hydration 不匹配是怎么检测与处理的？常见的修复流程是什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-110：SSR hydration 不匹配是怎么检测与处理的？常见的修复流程是什么？

**答**：
- 检测：hydrate 时客户端 render 会生成 vnode 树，**逐节点与服务端 HTML 的 DOM 比对**——文本内容、属性、元素类型、className 不一致即报 mismatch（开发环境抛详细警告，指明两端各自的值；生产环境静默）。
- 处理策略：文本/属性级不匹配 → **以客户端为准打补丁**（client render 该子树）；元素结构级不匹配 → **丢弃服务端 DOM，整子树走客户端渲染**（`forceClientRender` 标记，React 18 的 hydration 失败回退）。
- 常见根因：服务端/客户端输出不确定性（`Date.now()/Math.random()/locale 时间格式`）、服务端与客户端渲染了不同分支（`typeof window` 判断）、非法 HTML 嵌套被浏览器重排（如 `<p>` 内嵌 `<div>` 导致 DOM 结构变样）。
- 修复流程：复现（开发警告定位节点）→ 使输出确定性（时间戳用 UTC/由服务端传入随机种子）→ 结构问题修正 HTML 语义 → 局部无法确定的用 `suppressHydrationWarning`（仅该节点文本/属性层）或懒加载客户端专属部分。

```javascript
// 简化实现，帮助理解 hydration 比对与回退
function hydrate(serverEl, clientVNode) {
  // 1. 元素类型比对：结构级不匹配 -> 整个子树客户端重渲染
  if (serverEl.tagName.toLowerCase() !== clientVNode.type) {
    console.warn('hydration mismatch: 元素类型不同，回退 client render');
    const fresh = clientRender(clientVNode); // 丢弃服务端 DOM 重建
    serverEl.replaceWith(fresh);
    return fresh;
  }
  // 2. 文本比对：内容级不匹配 -> 以客户端为准
  if (serverEl.textContent !== clientVNode.children) {
    console.warn(
      `hydration mismatch: text "%s" != "%s"（常见根因：Date.now/Math.random/locale）`,
      serverEl.textContent, clientVNode.children,
    );
    serverEl.textContent = clientVNode.children; // client patch
  }
  // 3. 属性比对：服务端 DOM 属性 vs 客户端 vnode props
  for (const [k, v] of Object.entries(clientVNode.props || {})) {
    if (serverEl.getAttribute(k) !== String(v)) {
      console.warn(`hydration mismatch: attr ${k}="${serverEl.getAttribute(k)}" != "${v}"`);
      serverEl.setAttribute(k, v);
    }
  }
  return serverEl; // 复用成功：只绑定事件（React 在这里完成事件系统接管）
}

function clientRender(vnode) { // 完整客户端挂载
  const el = document.createElement(vnode.type);
  el.textContent = vnode.children;
  return el;
}

// 复现经典案例：时间格式不一致
const serverTime = new Date(0).toLocaleString('zh-CN');       // 服务器时区/本地化
const clientTime = '1970/1/1 08:00:00';                       // 假设客户端算出不同结果
hydrate(
  Object.assign(document.createElement('div'), { textContent: serverTime }),
  { type: 'div', children: clientTime, props: {} },
);
// 修复方案：时间戳随页面下发，两端用同一函数格式化；或对时间节点 suppressHydrationWarning
```
