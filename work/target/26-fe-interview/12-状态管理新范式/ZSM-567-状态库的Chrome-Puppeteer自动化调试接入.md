---
title: [ZSM-567] 状态库与浏览器自动化（Puppeteer/CDP）的调试接入怎么做
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-567：状态库与浏览器自动化（Puppeteer/CDP）的调试接入怎么做

**答**：
- 场景：CI 里复现状态 bug、E2E 断言「状态而不是 DOM」、批量采集状态轨迹。核心思路：通过 Chrome DevTools Protocol（CDP）的 `Runtime.evaluate` 在页面上下文里直接调用暴露出来的状态 API——前提是应用在 dev/test 构建把 store 挂到 `window.__stores`。
- 读：`page.evaluate(() => __stores.cart.getState())` 拿快照，做结构断言（比 DOM 断言稳，不怕样式变动）。
- 写与驱动：`evaluate(() => __stores.cart.getState().add('g1'))` 直接驱动状态——绕过 UI 交互做「状态级单元测试」，配合 UI 测试（Puppeteer 点击）形成两层。
- 轨迹采集：`page.exposeFunction('stateHook', cb)` 把状态变更回调暴露到 Node 侧，页面里 tracer 每次 setState 调 `stateHook(摘要)`——Node 端实时收到变更流，可写入文件做回放。
- 追问钩子：window 暴露 store 只允许在非生产构建（`import.meta.env.DEV` 守卫），否则是安全漏洞（任意 JS 可改状态）；生产需要的话走专用调试通道（受 CORS/token 限制的 WebSocket）。

```javascript
// 应用侧：仅 dev 暴露调试入口
if (import.meta.env.DEV) {
  window.__stores = { cart: useCartApi, user: useUserApi }
  // 状态变更钩子（配合 exposeFunction）
  window.__stateHook = window.__stateHook ?? (() => {})
  attachTracer(useCartApi, { onEvent: (e) => window.__stateHook(e) })
}

// Node 侧：Puppeteer 驱动
const page = await browser.newPage()
await page.goto('http://localhost:3000')

// 状态级断言（不依赖 DOM）
const cart = await page.evaluate(() => __stores.cart.getState())
assert.equal(cart.items.length, 0)

// 直接驱动状态：跳过 UI 细节
await page.evaluate(() => __stores.cart.getState().add({ id: 'g1', qty: 1 }))

// 实时状态流到 Node
await page.exposeFunction('stateHook', (e) => fs.appendFileSync('trace.jsonl', JSON.stringify(e) + '\n'))
await page.evaluate(() => { window.__stateHook = (e) => window.stateHook(e) })

// 混合模式：UI 点击 + 状态断言
await page.click('#checkout')
const phase = await page.evaluate(() => __stores.checkout.getState().phase)
assert.equal(phase, 'done')
```
