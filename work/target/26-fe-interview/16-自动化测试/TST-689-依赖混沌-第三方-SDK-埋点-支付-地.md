---
title: [TST-689] 依赖混沌：第三方 SDK（埋点 / 支付 / 地图）挂掉时怎么验证核心流程？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-689：依赖混沌：第三方 SDK（埋点 / 支付 / 地图）挂掉时怎么验证核心流程？

**答**：
- 结论：把第三方 SDK 当「不可信依赖」——假设它会加载失败、超时、抛错，核心流程必须可降级。
- 手段：拦截 script 加载、mock SDK 方法抛错、注入超时；断言核心路径仍可用。
- 关键原则：SDK 调用一律 try/catch + 超时，绝不让它阻塞主流程。
- 追问钩子：支付 SDK 超时后用户重复点击，怎么防止重复扣款？

```javascript
function guardSDK(sdk, { timeout = 2000, fallback } = {}) {
  return async (method, ...args) => {
    try {
      return await Promise.race([
        sdk[method](...args),
        new Promise((_, rej) =>
          setTimeout(() => rej(new Error('sdk timeout')), timeout)),
      ]);
    } catch (e) {
      console.warn('SDK 降级:', method, e.message);
      return fallback ? fallback(...args) : undefined;
    }
  };
}
const safePay = guardSDK(window.PaySDK, { fallback: () => ({ degraded: true }) });
```
