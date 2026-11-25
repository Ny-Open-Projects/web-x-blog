---
title: [MFW-097] +page.js 和 +page.server.js 的差异与同构 load 的运行时机？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-097：+page.js 和 +page.server.js 的差异与同构 load 的运行时机？
**答**：
- `+page.server.js`：只在服务端运行，客户端**永远拿不到代码**（可安全用 DB/密钥），SSR 时直接执行，客户端导航时通过 `/__data.json` 内部端点取结果。
- `+page.js`（universal load）：服务端与客户端都会运行。SSR 时在服务端执行；客户端导航时在浏览器执行（可访问 DOM/localStorage）。适合调用公开 API 或做服务端结果的再加工。
- 两者可共存：universal load 拿到 server load 的结果（`data` 参数）再补充客户端数据，形成「私密数据服务端取 + 浏览器增强客户端取」的分层。
- 运行时机关键点：universal load 在**首次 SSR** 时于服务端跑（不是浏览器），这常被误解；`csr = false` 时也不影响。

```js
// +page.server.js：私密数据
export async function load({ params }) {
  return { product: await db.product.findUnique({ where: { id: params.id } }) };
}

// +page.js：universal —— 在 server load 结果之上做客户端增强
export async function load({ data, fetch }) {
  // data 即 server load 的返回值
  // fetch 是 SvelteKit 包装过的 fetch：自动带 cookie、结果可被复用缓存
  const reviews = await fetch(`https://public-api.example.com/reviews/${data.product.id}`)
    .then((r) => r.json());

  return {
    ...data,          // 透传服务端数据
    reviews,          // 追加客户端增强数据
    now: new Date().toISOString(), // 浏览器导航时才是真实客户端时间
  };
}
```
