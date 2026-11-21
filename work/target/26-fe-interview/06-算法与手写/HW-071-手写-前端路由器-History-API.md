---
title: [HW-071] 手写前端路由器（History API 版）——push/replace、popstate、路由参数与守卫
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：路由器五件套：注册表（path→handler，支持 :param）、push/replace（history.pushState + 手动触发 handler）、popstate（前进后退自动匹配）、参数解析（正则 :param）、前置守卫链（可取消导航）。注意 pushState 不触发 popstate，必须手动调用匹配逻辑。

```javascript
class Router {
  constructor() { this.routes = []; this.guards = []; }
  register(path, handler) {
    const re = new RegExp('^' + path.replace(/:([^/]+)/g, (_, name) => `(?<${name}>[^/]+)`) + '$');
    this.routes.push({ re, handler, path });
  }
  beforeEach(guard) { this.guards.push(guard); }
  match(path) {
    for (const r of this.routes) {
      const m = path.match(r.re);
      if (m) return { handler: r.handler, params: m.groups || {} };
    }
    return null;
  }
  async navigate(to, { replace = false } = {}) {           // 编程式导航
    for (const g of this.guards) {
      const verdict = await g(to, location.pathname);
      if (verdict === false) return false;
      if (typeof verdict === 'string') return this.navigate(verdict);   // 重定向
    }
    replace ? history.replaceState(null, '', to) : history.pushState(null, '', to);
    this.#resolve(to);
    return true;
  }
  #resolve(path) {
    const hit = this.match(path);
    hit ? hit.handler(hit.params) : console.warn(`no route: ${path}`);
  }
  listen() {                                               // 前进/后退
    addEventListener('popstate', () => this.#resolve(location.pathname));
    addEventListener('DOMContentLoaded', () => this.#resolve(location.pathname));
  }
}
// 用法
const router = new Router();
router.register('/goods/:id', ({ id }) => renderGoods(id));
router.beforeEach(async (to) => to.startsWith('/admin') && !(await isAdmin()) ? '/login' : true);
router.listen();
router.navigate('/goods/42');
```

**评分点**：
- :param 编译成具名正则组（m.groups 取参数），通配路径能正确匹配。
- pushState 不触发 popstate——手动 #resolve，这是最高频扣分点。
- 守卫链支持 false 取消与重定向字符串，async 守卫 await。
- popstate + 首次进入都解析；no-route 有兜底提示。
