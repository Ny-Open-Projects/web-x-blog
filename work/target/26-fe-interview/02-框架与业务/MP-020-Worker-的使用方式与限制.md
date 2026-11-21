---
title: [MP-020] Worker 的使用方式与限制？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-020：Worker 的使用方式与限制？
**答**：
- `wx.createWorker(path)` 创建 worker，与主线程通过 `postMessage/onMessage` 通信，计算在独立线程执行不阻塞页面。
- 限制：**同时最多 1 个**；worker 代码必须放在项目 `workers/` 目录（app.json 声明）；worker 内不能访问 wx 大部分 API 与页面实例。
- 适用：大数据排序、图片/加解密、复杂字符串处理；简单逻辑别用，通信成本反而高。

```javascript
// app.json 需声明 "workers": "workers"
// —— 主线程 ——
const worker = wx.createWorker('workers/heavy/index.js')
worker.postMessage({ type: 'hash', payload: bigString })
worker.onMessage((res) => { console.log('worker 返回', res); worker.terminate() })

// —— workers/heavy/index.js ——
worker.onMessage(function ({ type, payload }) {
  if (type === 'hash') worker.postMessage({ result: heavyHash(payload) })
})
```
