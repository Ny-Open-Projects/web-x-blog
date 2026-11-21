---
title: [FRP-076] HTML5 模式如何监听路由变化？pushState 与 popstate、hashchange 的触发时序有何区别？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-076：HTML5 模式如何监听路由变化？pushState 与 popstate、hashchange 的触发时序有何区别？

**答**：
- HTML5 模式依赖 `history.pushState/replaceState` + **popstate 事件**。关键陷阱：**pushState/replaceState 本身不触发任何事件**，所以路由器在调用它们之后要**手动执行导航更新**（更新 currentRoute → 触发响应式重渲染）。
- popstate 只在**用户触发**的历史变化时派发：浏览器前进/后退按钮、`history.back()/forward()/go()`；hash 路由模式下 hash 变化同时触发 `hashchange` 和 `popstate`（顺序：hashchange 在前）。
- hash 模式时序：`location.hash = '#/a'` → 立即触发 hashchange → router 更新视图；history 模式时序：`router.push('/a')` → pushState（无事件）→ **同步**更新路由状态；点击后退 → popstate → router 监听器拿 `event.state` 恢复路由。
- 实现要点：base 解析、同源校验（跨源 pushState 抛错）、popstate 回调里 `event.state?.position ?? 0` 恢复滚动等。

```javascript
// 简化实现，帮助理解 history 路由的事件时序
function createHistoryRouter() {
  const listeners = new Set();
  const currentRoute = { path: '/', state: null };

  function notify(to, source) {
    Object.assign(currentRoute, to);
    listeners.forEach((l) => l(currentRoute, source)); // 统一驱动视图更新
  }

  return {
    subscribe(fn) { listeners.add(fn); return () => listeners.delete(fn); },
    // pushState 不会触发 popstate：push 后必须手动导航
    push(path) {
      history.pushState({ pos: history.length }, '', path);
      notify({ path, state: { pos: history.length } }, 'push'); // 同步更新
      return 'pushState 不发事件，notify 由路由器主动调用';
    },
    // 浏览器后退/前进触发 popstate：从这里恢复
    start() {
      window.addEventListener('popstate', (e) => {
        notify({ path: location.pathname, state: e.state }, 'popstate');
      });
    },
    currentRoute,
  };
}

const router = createHistoryRouter();
router.subscribe((r, src) => console.log(`[${src}] 视图切到 ${r.path}`));
router.start();
router.push('/about');            // [push] 视图切到 /about —— 无事件，路由器手动驱动
history.back();                   // 触发 popstate -> [popstate] 视图切回 /
// hash 模式对比：
// location.hash = '#/b' -> hashchange 先触发 -> popstate 随后触发
// router.push hash 版：改 hash 自动触发 hashchange，路由器监听 hashchange 即可，无需手动 notify
```
