---
title: [DP-090] axios 源码里能识别出哪些模式？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-090：axios 源码里能识别出哪些模式？
**答**：
- **适配器**：xhr/http/自定义 adapter 抹平双端差异（DP-027）。
- **职责链**：request/response 拦截器队列 + dispatchRequest 中点（DP-063）；`mergeConfig` 用策略表按字段类型合并。
- **工厂**：`axios.create(instanceConfig)` 生成带独立默认配置的实例；`Axios.prototype.request` 是请求工厂入口。
- **模板方法**：`dispatchRequest` 固定流程：转换请求体 → 调适配器 → 转换响应体；`CancelToken`/`AbortController` 用**状态机**管理取消状态。

```javascript
// axios 源码模式速览（对照 lib/）
// 1. 工厂：axios.create 生成独立实例（默认配置互不污染）
function createInstance(defaultConfig) {
  const context = new Axios(defaultConfig);
  const instance = bind(Axios.prototype.request, context);
  instance.create = (conf) => createInstance(mergeConfig(defaultConfig, conf)); // 可继续派生
  return instance;
}
function mergeConfig(a, b = {}) {
  const mergeMap = {              // 策略表：不同字段类型不同合并策略
    url: 'value',                 // b 有值则覆盖
    method: 'default',            // 有默认值兜底
    headers: 'object',            // 浅合并对象
    params: 'object',
    timeout: 'default',
  };
  const out = {};
  for (const [key, strategy] of Object.entries(mergeMap)) {
    if (strategy === 'object') out[key] = { ...a[key], ...b[key] };
    else if (strategy === 'default') out[key] = b[key] ?? a[key] ?? undefined;
    else out[key] = b[key] ?? a[key];
  }
  return out;
}
// 2. 模板方法：dispatchRequest 固定骨架
async function dispatchRequest(config) {
  config.data = transformData(config.transformRequest, config);  // 步骤1：出站转换（钩子）
  const adapter = pickAdapter(config);                            // 步骤2：适配器分派（策略）
  const response = await adapter(config);
  response.data = transformData(config.transformResponse, response); // 步骤3：入站转换（钩子）
  return response;
}
const transformData = (fns, ctx) => (fns || []).reduce((d, fn) => fn(d, ctx.headers || {}), ctx.data ?? ctx);
// 3. 状态机：取消令牌
class CancelToken {
  #reason = null;
  get reason() { return this.#reason; }   // pending -> canceled 两个状态
  cancel(message) {
    if (this.#reason) return;             // 幂等：重复取消无效（状态机约束）
    this.#reason = { message };
    this.#listeners?.forEach((fn) => fn(this.#reason));
  }
  throwIfRequested() { if (this.#reason) throw this.#reason; } // 请求前检查
}
const token = new CancelToken();
token.cancel('用户手动取消');
try { token.throwIfRequested(); } catch (e) { console.log('请求已取消', e.message); }
```
