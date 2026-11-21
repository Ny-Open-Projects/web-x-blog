---
title: [MP-021] storage 同步与异步 API 的差异？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-021：storage 同步与异步 API 的差异？
**答**：
- 同步版 `wx.setStorageSync/getStorageSync`：立即返回、代码直观，但**阻塞逻辑层线程**，大对象/高频读写会卡顿。
- 异步版 `wx.setStorage/getStorage`：不阻塞，回调风格；不传 success/fail/complete 时返回 **Promise**。
- 容量：单 key 上限 1MB，总量上限 10MB；超限抛错需 try/catch 或 fail 兜底。
- 实践：启动关键路径用同步小数据；批量/大文件读写用异步并合并。

```javascript
// 同步：关键小数据，记得容错
try {
  wx.setStorageSync('token', token)
} catch (e) {
  console.error('storage 超限或不可用', e)
}

// 异步：Promise 风格，不阻塞
wx.setStorage({ key: 'user', data: user })
  .then(() => console.log('ok'))
  .catch(console.error)
```
