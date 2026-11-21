---
title: [TST-123] 笔试：手写 fetch 拦截器（mini MSW，路径参数 + 一次生效 handler）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-123：笔试：手写 fetch 拦截器（mini MSW，路径参数 + 一次生效 handler）
**答**：
- 需求：实现 `mockFetch`——monkeypatch `globalThis.fetch`，注册 handler 列表按「方法 + 路径模板」（支持 `:id` 参数与 `*` 通配）匹配，命中则不发出真实请求；支持 `once` handler（用后即焚，LIFO 优先）；未命中放行真实 fetch；`restore()` 恢复。
- 核心：保存原生 fetch 引用；路径模板编译成正则并提取参数名；handler 返回 `Response`（或对象自动包成 Response）。
- 边界：query string 不参与路径匹配但可通过 request.url 拿到；多个 handler 按注册倒序匹配（后注册优先，模拟 `server.use` 插队）；async handler 抛错要 reject 而不是吞掉。

```javascript
function createMockFetch() {
  const native = globalThis.fetch;
  const handlers = []; // { method, regex, keys, once, respond }

  const compile = (path) => {
    const keys = [];
    const pattern = path.replace(/:([^/]+)/g, (_, k) => (keys.push(k), '([^/]+)')).replace(/\*/g, '.*');
    return { regex: new RegExp(`^${pattern}$`), keys };
  };

  function mock(method, path, respond, { once = false } = {}) {
    const { regex, keys } = compile(path);
    handlers.push({ method: method.toUpperCase(), regex, keys, once, respond });
    return () => { // 返回取消函数
      const i = handlers.indexOf(handlers.find((h) => h.path === path));
      if (i > -1) handlers.splice(i, 1);
    };
  }

  const patched = async (input, init = {}) => {
    const url = new URL(typeof input === 'string' ? input : input.url, location.origin);
    const method = (init.method || 'GET').toUpperCase();
    for (let i = handlers.length - 1; i >= 0; i--) {      // 后注册优先
      const h = handlers[i];
      if (h.method !== method) continue;
      const m = url.pathname.match(h.regex);
      if (!m) continue;
      if (h.once) handlers.splice(i, 1);                  // once 用后即焚
      const params = Object.fromEntries(h.keys.map((k, j) => [k, decodeURIComponent(m[j + 1])]));
      const req = { url: url.href, params, init };
      const res = await h.respond(req);
      return res instanceof Response ? res : new Response(JSON.stringify(res.body), { status: res.status ?? 200 });
    }
    return native(input, init);                           // 未命中放行
  };

  const restore = () => { handlers.length = 0; globalThis.fetch = native; };
  mock.restore = restore;
  return { mock, restore };
}

// ---- 用法 ----
const { mock } = createMockFetch();
mock('GET', '/api/goods/:id', () => ({ status: 200, body: { id: 9 } }));
mock('POST', '/api/cart', () => ({ status: 500, body: { msg: 'fail' } }), { once: true });
const r = await fetch('/api/goods/9');
console.log(await r.json()); // { id: 9 }
```

**评分点**：
1. 是否保留原生 fetch 引用并支持 restore（测试污染 = 直接扣分）。
2. 路径模板 `:id` 编译与参数提取正确性（decodeURIComponent）。
3. once + LIFO 匹配顺序是否正确（对应 MSW server.use 语义）。
4. 未命中放行真实请求 + 异步 handler 抛错不吞。
