---
title: [MP-369] 笔试：手写 EventChannel 封装（页面通信 promise 化）
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## MP-369：笔试：手写 EventChannel 封装

**答**：实现页面间通信封装 `navToResult(url, payload)`：① navigateTo + EventChannel——返回 Promise（目标页 emit('result') 时 resolve，emit('cancel') 时 reject）；② 超时保护（目标页崩溃无响应 → 5s reject）；③ 目标页侧 `emitResult(data)` / `emitCancel()` 的对称封装；④ 栈安全（目标页被 redirectTo 后 channel 失效——检测防护）；⑤ 与全局 store 方案的取舍说明。写出实现。

```javascript
export function navToResult(url, payload, { timeout = 5000 } = {}) {
  return new Promise((resolve, reject) => {
    let settled = false;
    const timer = setTimeout(() => {
      if (!settled) { settled = true; reject(new Error('channel timeout')); }
    }, timeout);
    wx.navigateTo({
      url,
      events: {
        result: (data) => { if (!settled) { settled = true; clearTimeout(timer); resolve(data); } },
        cancel: () => { if (!settled) { settled = true; clearTimeout(timer); reject(new Error('cancelled')); } },
      },
      success: (res) => res.eventChannel.emit('init', payload),
      fail: (e) => { if (!settled) { settled = true; clearTimeout(timer); reject(e); } },
    });
  });
}
// 目标页对称封装
export function createChannelEmitter(page) {
  const ch = page.getOpenerEventChannel?.();
  return {
    init: (fn) => ch?.on('init', fn),
    result: (data) => ch?.emit('result', data),
    cancel: () => ch?.emit('cancel'),
  };
}
// 用法
// 调用方: const sel = await navToResult('/pages/select/index', { multi: true });
// 目标页: const ch = createChannelEmitter(this); ch.init((p) => {...}); ch.result(items); wx.navigateBack();
// 取舍: EventChannel 适合一次性流程; 常驻状态同步用 store + onShow
```

**评分点**：
- Promise 化的双事件语义（result/cancel）+ 一次性 settled 防重
- 超时保护（目标页崩溃场景）
- 对称封装（调用方/目标方 API 对齐）
- EventChannel vs store 的适用边界说明
