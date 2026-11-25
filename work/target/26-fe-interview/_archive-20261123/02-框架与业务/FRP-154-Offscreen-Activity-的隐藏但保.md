---
title: [FRP-154] Offscreen（Activity）的"隐藏但保活"预渲染是如何设计的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-154：Offscreen（Activity）的"隐藏但保活"预渲染是如何设计的？

**答**：
- Offscreen（现名 Activity）让子树以 **hidden 模式渲染**：DOM 已挂载但 `display: none`，state 完整保留；为"提前预渲染、切换不重渲"服务。
- 生效机制在 fiber 树结构里：`<Activity mode="hidden">` 创建 Offscreen fiber，其子树的 effect **被推迟**（隐藏时不执行 effect/不触发事件），显示时 React 再"补执行"effect——这叫"延迟副作用"。
- 预渲染（prerender）：提前把可能要显示的页面 hidden 渲染好，切换时只是改 mode——commit 走最小路径，无白屏。
- 它与 Suspense 共享"挂起树/隐藏树"的底层机制：隐藏的树仍可被并发渲染，但永远不会提交 effect。

```javascript
// 简化实现，帮助理解 Offscreen 的隐藏渲染与延迟 effect
const ActivityMode = { Visible: 'visible', Hidden: 'hidden' };

function reconcileOffscreenFiber(fiber, mode) {
  if (mode === ActivityMode.Hidden) {
    // 子树继续渲染（预渲染！），但打上 hidden 标记
    fiber.subtreeFlags |= OffscreenHiddenFlag;
    // commit 时：DOM 挂载但 display none，effect 队列跳过
    return { shouldMountDom: true, shouldRunEffects: false };
  }
  return { shouldMountDom: true, shouldRunEffects: true };
}

function commitOffscreen(fiber, { shouldRunEffects }) {
  const el = fiber.stateNode;
  el.style.display = fiber.mode === 'hidden' ? 'none' : '';
  if (!shouldRunEffects) {
    // 隐藏树：把 layout/passive effect 暂存 —— 显示时再执行
    deferEffects(fiber.subtreeFlags);
  } else {
    flushDeferredEffects(fiber);   // 从 hidden 转 visible：补执行延迟的 effect
  }
}

// 使用场景
function Tabs() {
  const [tab, setTab] = useState('a');
  return (
    <>
      <button onClick={() => setTab('a')}>A</button>
      <button onClick={() => setTab('b')}>B</button>
      {/* B 页面提前渲染好、状态保留；切回来不重新请求不丢 state */}
      <Activity mode={tab === 'a' ? 'visible' : 'hidden'}>
        <PageA />
      </Activity>
      <Activity mode={tab === 'b' ? 'visible' : 'hidden'}>
        <PageB />   {/* hidden 期间 effect 不跑（不轮询/不订阅），显示时恢复 */}
      </Activity>
    </>
  );
}
// 与 v-show 的区别：不只隐藏 DOM，还暂停副作用 —— "预渲染 + 副作用暂停"两个能力
```

## 二十三、React 表单与模式原理
