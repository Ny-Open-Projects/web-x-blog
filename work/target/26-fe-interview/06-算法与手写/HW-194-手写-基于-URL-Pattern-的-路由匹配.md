---
title: [HW-194] 手写 URLPattern 路由匹配——内置 pattern 匹配（groups 提取）与降级正则
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：URLPattern API（Chrome 95+）替代手写正则路由（HW-071 的现代版）：`new URLPattern({ pathname: '/goods/:id' })` → exec 返回 groups.id；支持通配 `:id?`/`:path+`；降级到正则版（同语义）。

```javascript
class Router {
  #routes = [];
  add(pattern, handler) {
    if (typeof URLPattern === 'function') {
      const p = new URLPattern({ pathname: pattern });    // '/goods/:id' '/static/*'
      this.#routes.push({ p, handler });
    } else {
      const re = new RegExp('^' + pattern.replace(/:([^/]+)/g, '(?<$1>[^/]+)').replace(/\*/g, '.*') + '$');
      this.#routes.push({ re, handler });
    }
    return this;
  }
  match(path) {
    for (const r of this.#routes) {
      if (r.p) {
        const m = r.p.exec({ pathname: path });
        if (m) return { handler: r.handler, params: m.pathname.groups };
      } else {
        const m = path.match(r.re);
        if (m) return { handler: r.handler, params: m.groups ?? [] };
      }
    }
    return null;
  }
}
// URLPattern 优势：标准 API（groups 具名/通配语义一致/查询串匹配 pathname+search 都支持）
// 与 SW 结合：registerRoute 的 URL Pattern 匹配（Workbox 风格）—— 缓存路由声明式定义
// 降级正则保持同语义（:name 具名组 + * 通配）
```

**评分点**：
- URLPattern exec 的 groups 提取与通配语法——本题核心。
- 降级正则保持同语义（具名组转换正确）。
- 与 SW 缓存路由（Workbox 风格）的结合价值。
- 能说出正则手写路由的易错点（结尾 /、多段 :param、query 匹配）。
