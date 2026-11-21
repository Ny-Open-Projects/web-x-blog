---
title: [FRP-107] DevTools 是怎么拿到组件树和 fiber 的？浏览器扩展的注入机制是什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-107：DevTools 是怎么拿到组件树和 fiber 的？浏览器扩展的注入机制是什么？

**答**：
- 通道是**全局钩子**：React 在启动时检测 `window.__REACT_DEVTOOLS_GLOBAL_HOOK__`，存在则调用 `hook.inject(internals)` 把 reconciler 内部对象（currentDispatcherRef、各种 commitHook）交给扩展；Vue 同理暴露 `__VUE__`（`app.config.globalProperties` 与 devtools hook）。
- 扩展侧注入链：Chrome 扩展的 **content script** 在页面加载早期（document_start）往 `window` 上挂空 hook 对象 → 页面里的框架代码 inject 自身 internals → 扩展通过 CustomEvent/postMessage 把序列化的组件树发给 **devtools panel**（isolated world，需要桥接）。
- 组件树遍历：拿到 internals 后沿 `fiber.return`/`child/sibling` 链构建树，读取 `tag/stateNode/memoizedProps/state` 渲染面板；Vue 走 `instance.uid/parent/subTree/proxy`。
- 这解释了两个现象：DevTools 需要"页面加载前"就装好（后装刷新页面才能生效）、生产包关掉 devtools 标记后组件树为空。

```javascript
// 简化实现，帮助理解 hook 注入与组件树采集
// ===== 扩展 content script（document_start 阶段先于页面脚本执行）=====
window.__REACT_DEVTOOLS_GLOBAL_HOOK__ = {
  renderers: new Map(),
  inject(internals) {
    // 框架启动时把自己的 reconciler 内部对象交上来
    this.renderers.set(internals.id, internals);
    console.log('[devtools] renderer injected:', internals.id);
  },
  onCommitFiberRoot(root) { this._emit(this.walkTree(root.current)); },
  _emit(tree) { /* window.postMessage 桥接到 devtools panel */ void tree; },
  // 组件树遍历：沿 child/sibling 链构建
  walkTree(fiber, depth = 0) {
    const node = {
      name: typeof fiber.type === 'function' ? fiber.type.name : String(fiber.type),
      tag: fiber.tag,                    // 0 函数 1 类 5 DOM 6 文本
      props: { ...fiber.memoizedProps }, // 面板展示用（脱敏可在此做）
      state: fiber.memoizedState?.memoizedState, // 第一个 Hook 的值
      depth,
      children: [],
    };
    for (let child = fiber.child; child; child = child.sibling) {
      node.children.push(this.walkTree(child, depth + 1));
    }
    return node;
  },
};

// ===== 框架侧（React 启动时）=====
const hook = window.__REACT_DEVTOOLS_GLOBAL_HOOK__;
if (hook) {
  hook.inject({ id: 1, currentDispatcherRef: {}, supportsFiber: true });
}

// ===== 模拟一次 commit 上报 =====
const App = function App() {};
const fiberRoot = {
  current: {
    type: 'HostRoot', tag: 3, memoizedProps: {}, memoizedState: null,
    child: { type: App, tag: 0, memoizedProps: { page: 1 }, memoizedState: { memoizedState: 0 },
      child: { type: 'div', tag: 5, memoizedProps: {}, child: null, sibling: null },
      sibling: null },
  },
};
hook.onCommitFiberRoot(fiberRoot);
const tree = hook.walkTree(fiberRoot.current);
console.log(JSON.stringify(tree, null, 1)); // HostRoot -> App -> div
```
