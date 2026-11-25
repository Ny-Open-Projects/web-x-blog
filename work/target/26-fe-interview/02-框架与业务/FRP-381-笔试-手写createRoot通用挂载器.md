---
title: [FRP-381] 笔试：手写通用挂载器（跨框架 root 管理）
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## FRP-381：笔试：手写通用挂载器

**答**：实现 `createRootHost(container)`：① mount(framework, app)：按 framework（'react'|'vue'）分派创建 root——统一管理生命周期；② 重复 mount 防护（先 unmount 旧的）；③ unmountAll：容器销毁时全部卸载（页级清理）；④ 状态桥注入（各框架 root 挂载时传内核 store）；⑤ 挂载失败隔离（一个框架失败不影响另一个）。写出实现。

```javascript
export function createRootHost(container) {
  const roots = new Map();        // key -> { unmount, framework }
  const host = {
    mount(key, framework, appFn, props = {}) {
      if (roots.has(key)) host.unmount(key);        // 重复防护
      const el = document.createElement('div');
      el.dataset.host = key;
      container.appendChild(el);
      try {
        const unmount = framework === 'react'
          ? mountReact(el, appFn, props)            // createRoot().render() → 返回 unmount
          : framework === 'vue'
            ? mountVue(el, appFn, props)            // createApp().mount() → 返回 unmount
            : (() => { throw new Error(`unknown framework: ${framework}`); })();
        roots.set(key, { unmount, framework });
        return el;
      } catch (e) {
        el.remove();
        report({ type: 'mount-fail', key, framework, error: String(e) });   // 失败隔离
        return null;
      }
    },
    unmount(key) {
      const r = roots.get(key);
      if (!r) return;
      r.unmount();                                   // 各框架的卸载钩子
      container.querySelector(`[data-host="${key}"]`)?.remove();
      roots.delete(key);
    },
    unmountAll() { for (const key of [...roots.keys()]) host.unmount(key); },
    get active() { return [...roots.keys()]; },
  };
  // 页面卸载兜底
  window.addEventListener('pagehide', () => host.unmountAll(), { once: true });
  return host;
}
// mountReact(el, App, props): const root = createRoot(el); root.render(wrapProps(App, props)); return () => root.unmount();
// mountVue(el, App, props):  const app = createApp(App); app.provide('props', props); app.mount(el); return () => app.unmount();
```

**评分点**：
- 双框架分派与统一 unmount 句柄
- 重复 mount 防护与失败隔离（el 清理 + 上报）
- unmountAll 的页级清理与 pagehide 兜底
- props 注入的框架差异（provide vs 透传）

## 变体与延伸（补充）

**变体与延伸**：

1. 同一个容器被挂两次会怎样？ → 第二次 `createRoot` 会警告且两个 root 争同一 DOM，表现为后挂的覆盖前者、前者卸载时清空整棵子树。应用 `WeakMap<Element, Root>` 做幂等，重复挂载直接返回已有句柄。
2. 卸载后还有异步 setState 怎么办？ → `root.unmount()` 之后 React 会忽略更新，但定时器、订阅、事件监听不会自动清；必须在卸载前按注册逆序执行清理，否则切页十次就有十份监听。
3. 微前端里 React 与 Vue 同时挂载如何隔离？ → 样式走 Shadow DOM 或统一前缀，全局事件在各自 unmount 里成对移除；共享的 `window` 状态要显式命名空间，否则子应用切换后监听器翻倍。
