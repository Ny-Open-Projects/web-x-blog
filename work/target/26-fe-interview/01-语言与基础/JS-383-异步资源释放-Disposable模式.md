---
title: [JS-383] 异步资源释放：Disposable 模式与生命周期绑定
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-383：异步资源释放：Disposable 模式与生命周期绑定

**答**：
- 前端可释放资源清单：定时器、事件监听、Worker、WebSocket、IntersectionObserver、rAF 循环、AbortController、objectURL——「创建即注册释放」是纪律
- Disposable 模式：资源封装返回 dispose()（或注册到统一清理器），组件/作用域销毁时统一调用——React useEffect cleanup、Vue onUnmounted、纯 JS 用作用域清理器
- 显式协议（Explicit Resource Management 提案）：Symbol.dispose/asyncDispose + using 语法——未来标准化写法，现在可用 polyfill 思维提前布局
- 释放的顺序与幂等：dispose 要幂等（重复调用不炸）、依赖顺序（先断消费者再关生产者）——清理器按注册逆序释放
- 泄漏自查：组件卸载后资源仍活跃（定时器还在跑）——用「实例存活计数」埋点或 Heap Snapshot 检测 detached 实例

```javascript
// 作用域清理器
function createScope() {
  const disposers = [];
  return {
    track(resource, dispose) { disposers.push(dispose); return resource; },
    listen(el, ev, fn) { el.addEventListener(ev, fn); disposers.push(() => el.removeEventListener(ev, fn)); },
    disposeAll() { for (const d of disposers.reverse()) try { d(); } catch (e) { console.error(e); } },
  };
}
// 用法: 所有资源过 scope, 销毁一处调用
const scope = createScope();
const timer = scope.track(setInterval(tick, 1000), () => clearInterval(t));
scope.listen(btn, 'click', onClick);
onDestroy(() => scope.disposeAll());
```
