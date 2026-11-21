---
title: [HW-072] 手写 Hash 路由器，并说明 hash 与 history 模式的本质差异与选型
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：hash 路由锚在 `location.hash`（# 后部分）：变化天然触发 `hashchange`，无需服务器配置、刷新不 404；history 模式路径真实但需要服务端 fallback。hash 的代价：URL 带 #、SEO 弱、锚点功能被占用。实现要点：解析 hash、normalize 无 hash 时的默认路由、pushState 兼容（hashchange 双通道防重复解析）。

```javascript
class HashRouter {
  constructor({ default: fallback = '/' } = {}) { this.routes = []; this.fallback = fallback; }
  register(path, handler) { this.routes.push({ path, handler }); }
  #current() { return location.hash.slice(1) || this.fallback; }   // '#/goods/1' => '/goods/1'
  push(to) { location.hash = to; }                                  // 触发 hashchange
  replace(to) { const url = location.href.replace(/(#.*)?$/, '#' + to);
    history.replaceState(null, '', url); this.#resolve(to); }       // replace 不触发 hashchange，手动 resolve
  #resolve(path) {
    for (const r of this.routes) {
      const m = path.match(new RegExp('^' + r.path.replace(/:(\w+)/g, '([^/]+)') + '$'));
      if (m) return r.handler(m.slice(1));                          // 位置参数
    }
    this.#resolve(this.fallback);                                   // 404 兜底到默认路由
  }
  listen() {
    addEventListener('hashchange', () => this.#resolve(this.#current()));
    addEventListener('load', () => this.#resolve(this.#current()));
  }
}
// hash vs history 选型：
// hash：免服务器配置、file:// 可跑、老浏览器兼容 —— 内嵌页/快速部署
// history：URL 干净、SSR 友好、SEO —— 正式产品默认选它（配 nginx try_files fallback）
```

**评分点**：
- hash 解析（slice(1) + 默认路由兜底）与 replace 不触发 hashchange 需手动 resolve 的细节。
- 404 兜底到默认路由（防死路由）。
- 能对比 hash/history：服务器配置、SEO、锚点占用、file:// 场景。
- hashchange 与 load 双监听齐全。
