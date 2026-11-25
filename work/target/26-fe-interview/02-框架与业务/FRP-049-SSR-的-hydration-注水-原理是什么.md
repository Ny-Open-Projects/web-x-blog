---
title: [FRP-049] SSR 的 hydration（注水）原理是什么？为什么会出现水合不匹配？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-049：SSR 的 hydration（注水）原理是什么？为什么会出现水合不匹配？

**答**：
- SSR 输出的 HTML 已含完整 DOM；客户端 JS 加载后 hydration 阶段**不重建 DOM**，而是在已有 DOM 上"认领"：复刻组件树生成 fiber/vnode，与现有 DOM 对齐，只补挂事件与组件状态。
- React 通过 `__reactFiber$`/`__reactProps$` 等 DOM 属性绑定；Vue3 用 vnode 的 el 直接指向已有元素。
- 水合不匹配（mismatch）：服务端与客户端渲染结果不一致（Date.now/random/typeof window 分支/HTML 转义差异），React 18 会在首个差异处丢弃服务端 DOM 改为客户端重渲，代价大且有闪烁。
- 消除手段：随机值放到 useEffect 或挂载后再生成、统一时间用 UTC/服务端传入的 props、Svelte/Vue 的一致性检查；React 19 已改进错误提示定位。

```javascript
// 简化实现，帮助理解 hydration
function hydrate(vnode, domElement) {
  if (vnode.type !== domElement.tagName.toLowerCase()) {
    // 不匹配：React 18 的做法是丢弃服务端 DOM，客户端整体重渲
    console.warn('hydration mismatch，回退客户端渲染');
    return render(vnode, domElement.parentNode);
  }
  // 1. 复用现有 DOM：vnode.el = domElement，不重新创建
  vnode.el = domElement;

  // 2. 补挂交互：事件委托在 root 层统一注册（见 FRP-037），这里无需逐元素绑定
  //    类组件此时才创建实例，函数组件执行 render 计算出 fiber 树

  // 3. props 对齐：不执行 DOM 写入，只比对必要时告警
  // React 在此检查 attributes 与期望是否一致，第一个不一致处触发 client render

  // 4. 递归处理 children
  let childEl = domElement.firstChild;
  vnode.children?.forEach((child) => {
    if (typeof child === 'string') {
      childEl = childEl.nextSibling; // 文本直接认领
    } else {
      hydrate(child, childEl);
      childEl = childEl?.nextSibling;
    }
  });

  // 5. 之后正常调度 effects：useEffect 会在 hydration 后执行
}

// 水合不匹配的典型来源：
// function Time() {
//   // 服务端渲染时刻 与 客户端注水时刻 不同 -> 内容不同 -> mismatch
//   return <span>{new Date().toLocaleTimeString()}</span>; // 错误示范
// }
```

## 追问（补充）

**追问**：

1. 出现 mismatch 时 React 18 是整页重渲还是只重渲出错的那个组件？ → 在第一个不一致的节点上把整棵 root 的服务端 DOM 丢弃、从 root 重新 client render，不是局部修补，所以代价按整页算；React 19 改为尽量保留可复用节点并打印带 diff 的错误信息，方便定位到具体元素。
2. 为什么 hydration 期间写 useLayoutEffect 会报警告，而 useEffect 不会？ → 水合时 DOM 已存在，React 不走 layout 插入流程，无法保证 layoutEffect 在浏览器绘制前成对执行；18 直接告警，19 允许它在 hydrate 完成后补跑但仍建议用 useEffect。
3. 线上已上线又没法改代码，怎么定位是哪棵子树造成的 mismatch？ → 先用 `suppressHydrationWarning` 逐层收窄范围，再对 Date.now、Math.random、`typeof window` 分支三类来源做二分；也可以把可疑子树改成 `dynamic(..., {ssr:false})` 先止损，再回头修根因。
