---
title: [ENG-155] qiankun 完整接入的工程清单有哪些？主应用与子应用要改什么？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-155：qiankun 完整接入的工程清单有哪些？主应用与子应用要改什么？
**答**：
- 主应用：registerMicroApps 注册子应用 + initGlobalState 全局状态 + addGlobalUncaughtExceptionHandler 统一兜底子应用异常。
- 子应用改造点：产物改 umd 格式、publicPath 动态化、导出 bootstrap/mount/unmount 三个生命周期。
- 样式隔离双管齐下：experimentalStyleIsolation 加前缀隔离，子应用自身规范全局选择器命名空间。
- 独立与嵌套双形态：子应用单独跑是完整站点，被基座加载才走微前端生命周期，用 window.__POWERED_BY_QIANKUN__ 区分。

```typescript
// ===== main-app/src/micro/register.ts 主应用接入 =====
import { registerMicroApps, start, initGlobalState, addGlobalUncaughtExceptionHandler } from 'qiankun'

const actions = initGlobalState({ user: null, theme: 'light' })
export const onGlobalStateChange = actions.onGlobalStateChange

registerMicroApps(
  [
    { name: 'order', entry: '//localhost:8001', container: '#sub-root', activeRule: '/order' },
    { name: 'stock', entry: '//localhost:8002', container: '#sub-root', activeRule: '/stock' },
  ],
  { beforeLoad: app => console.log(`加载 ${app.name}`) },
)

start({
  sandbox: { experimentalStyleIsolation: true },  // 样式前缀隔离
  prefetch: 'all',
})

addGlobalUncaughtExceptionHandler(e => reportMicroError(e))  // 子应用异常统一上报

// ===== sub-app/vite.config.ts 子应用改造为可加载的 umd 产物 =====
// import { defineConfig } from 'vite'
// import qiankun from 'vite-plugin-qiankun'
// export default defineConfig({
//   base: '/order/',
//   server: { port: 8001, cors: true },
//   plugins: [qiankun('order', { useDevMode: true })],
//   build: { target: 'es2015', formats: ['umd'] },
// })
```
