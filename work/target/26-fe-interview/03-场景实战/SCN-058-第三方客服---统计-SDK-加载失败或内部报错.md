---
title: [SCN-058] 第三方客服 / 统计 SDK 加载失败或内部报错把主站拖垮，如何做隔离与超时兜底？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-058：第三方客服 / 统计 SDK 加载失败或内部报错把主站拖垮，如何做隔离与超时兜底？
**答**：
- 原则：第三方脚本一律不进主 bundle、不阻塞主流程，失败只降级自身功能（隐藏客服入口），绝不影响下单等主链路。
- 加载层：异步加载 + 硬超时（超时移除 script 标记失败）；接入层：初始化与调用全部 try-catch 包裹。
- SDK 提供的异步接口同样包超时（Promise.race），防止其内部 promise 永不 resolve 导致业务挂起；必要时用 iframe 沙箱隔离高危 SDK。

```javascript
// 第三方 SDK 加载器：超时兜底 + 失败降级 + 调用隔离
function loadSDK(src, { timeout = 5000 } = {}) {
  return new Promise((resolve, reject) => {
    const s = document.createElement('script');
    const timer = setTimeout(() => { s.remove(); reject(new Error('sdk timeout')); }, timeout);
    s.src = src;
    s.async = true;
    s.onload = () => { clearTimeout(timer); resolve(); };
    s.onerror = () => { clearTimeout(timer); reject(new Error('sdk failed')); };
    document.head.appendChild(s);
  });
}

// 接入点：失败只降级自身入口，不碰主流程
loadSDK('https://sdk.third.com/chat.js')
  .then(() => window.ThirdChat.init({ appId: 'xxx' }))
  .catch((err) => {
    document.querySelector('#cs-entry')?.remove();   // 失败隐藏客服入口
    report({ type: 'sdk-degraded', err: err.message });
  });

// SDK 的异步接口包一层超时，防止内部 promise 永不 resolve
const withTimeout = (p, ms = 3000) =>
  Promise.race([p, new Promise((_, rej) => setTimeout(() => rej(new Error('api timeout')), ms))]);
```

## 十四、表单与交互进阶
