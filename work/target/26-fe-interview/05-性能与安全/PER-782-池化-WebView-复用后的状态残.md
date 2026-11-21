---
title: [PER-782] 池化 WebView 复用后的状态残留清理：cookie、storage、滚动位置与 JS 状态的复位清单
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-782：池化 WebView 复用后的状态残留清理：cookie、storage、滚动位置与 JS 状态的复位清单

**答**：
- 复用最大的坑是"上一页的残留"：Cookie/登录态（可能串号）、localStorage（业务键冲突）、scroll 位置、URL hash、事件监听、定时器、Service Worker 消息通道。
- 复位清单分级：必须清（URL→about:blank、滚动归零、清内存态 JS 变量）、按需清（localStorage 按前缀、Cookie 按域）、不能清（HTTP 缓存目录——复用收益来源）。
- 清理时机：release 时同步清基础项，heavy 清理（SW 注销、Storage 清理）放 idle 异步做，避免复用瞬间卡顿。
- 兜底：复位后由容器侧校验关键项（URL/标题/栈），不达标降级为销毁重建。

```javascript
const RESET_CHECKLIST = {
  sync: [                                     // release 同步执行
    'loadUrl(about:blank)',                   // URL 与 JS 状态归零
    'window.scrollTo(0,0)',
    'clearTimersAndListeners()',              // 遍历登记表逐一移除
  ],
  asyncIdle: [                                // idle 异步执行
    'localStorage 清业务前缀 app_x_*',
    'cookie 按 host 清业务域',
    'unregister SW（若页面注册过）',
  ],
  keep: ['HTTP 磁盘缓存', '已下发的 JSAPI 白名单'],
};
function releaseWebView(w) {
  RESET_CHECKLIST.sync.forEach(fn => safeRun(fn, w));
  requestIdleCallback(() => RESET_CHECKLIST.asyncIdle.forEach(fn => safeRun(fn, w)));
  const ok = verifyReset(w);                  // 校验 URL/标题归零
  if (!ok) Pool.destroy(w);                   // 降级销毁重建
}
```
