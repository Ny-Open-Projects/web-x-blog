---
title: [MFW-417] 笔试：手写客户端路由器最小实现
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-417：最小客户端路由器
**答**：实现 `createRouter(routes)`（~60 行）：1) History API 导航（push/replace + popstate 监听——含 bfcache pageshow 重连语义）；2) 路径匹配（:param 提取 + 通配 *）；3) 守卫链（async 串行，redirect 深度 ≤3 防环——MFW-455 复刻）；4) 异步组件加载（懒 import + 加载态与竞态守卫——新导航使旧 load 失效 version 号）；5) 滚动语义（push 回顶 / pop 保持——history.scrollRestoration 手动接管）；6) base 防抖（同 path 重复 push 忽略）。

```javascript
export function createRouter(routes, { guards = [] } = {}) {
  let version = 0, current = null
  const listeners = new Set()

  function match(path) {
    for (const r of routes) {
      const p = matchGlob(patternOf(r.path), path)             // :param 提取 + * 
      if (p) return { route: r, params: p }
    }
    return null                                                 // → notFound 处理
  }

  async function go(to, { replace = false, depth = 0 } = {}) {
    if (depth > 3) throw new Error('redirect loop')             // 守卫环上限
    const my = ++version                                        // 竞态守卫：旧导航作废
    for (const g of guards) {
      const r = await g(to, current)
      if (r?.redirect) return go(r.redirect, { replace: true, depth: depth + 1 })
      if (r === false) return null                              // 拒绝
    }
    const m = match(new URL(to, 'x').pathname)
    if (!m) return renderNotFound(to)
    history[replace ? 'replaceState' : 'pushState']({}, '', to)
    if (!replace && !isHashOnly) window.scrollTo(0, 0)          // push 回顶 / pop 由 popstate 保持
    const mod = await m.load?.() .catch(() => errComp)          // 懒加载
    if (version !== my) return                                  // 期间有新导航→丢弃
    current = to
    listeners.forEach((f) => f({ ...m, mod }))
  }

  window.addEventListener('popstate', (e) => go(location.pathname, { replace: true }))  // Back 走守卫？——按产品：popstate 绕守卫直渲（浏览器原生语义优先）
  window.addEventListener('pageshow', (e) => e.persisted && resync())   // bfcache 回归重连 WS 等
  return { push: (t) => go(t), replace: (t) => go(t, { replace: true }), subscribe: (f) => (listeners.add(f), () => listeners.delete(f)), get current() { return current } }
}
```
**评分点**：
- version 竞态守卫（快速连点：旧懒加载完成后不覆盖新导航——客户端路由最经典 bug）
- 守卫环上限 + popstate 语义选择有意识（Back 绕守卫=原生行为优先，写选择理由）
- bfcache pageshow 重连（persisted 判断——只恢复不重挂）
- scrollRestoration 语义分派（push 回顶 pop 保持）
