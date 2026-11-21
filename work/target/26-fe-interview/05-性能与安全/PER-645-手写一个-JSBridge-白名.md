---
title: [PER-645] 手写一个 JSBridge 白名单校验层（H5 侧封装）：调用前校验方法注册表、参数 schema 与频控
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-645：手写一个 JSBridge 白名单校验层（H5 侧封装）：调用前校验方法注册表、参数 schema 与频控

**答**：
- H5 侧封装的价值：统一入口收敛调用（不散落 window.NativeBridge 直接调用），在入口做方法注册表校验、参数 schema（手写轻校验）、频控与审计日志。
- 要点：schema 用极简声明（`{url: 'string', timeout: 'number?'}`）；频控滑动窗口（每方法每秒上限）；调用超时与错误码统一，防 H5 业务侧各自兜底不一致。
- 边界：bridge 不存在（低版本容器）返回明确错误码而不是静默；未注册方法直接拒绝并上报（可能是非法调用探测）。
- 评分点：滑动窗口频控与未注册方法上报。

```javascript

const REGISTRY = {
  openUrl: { schema: { url: 'string' }, rate: 5 },          // 每秒上限
  getLocation: { schema: {}, rate: 2 },
  scanCode: { schema: {}, rate: 1 },
};
const callCount = new Map();                                 // method -> timestamps
function bridgeCall(method, params = {}) {
  const reg = REGISTRY[method];
  if (!reg) { report('bridge-unknown', { method });          // 未注册 = 探测嫌疑
    return Promise.reject({ code: 'BRIDGE_UNREGISTERED' }); }
  // 滑动窗口频控
  const now = performance.now();
  const arr = (callCount.get(method) ?? []).filter(t => now - t < 1000);
  if (arr.length >= reg.rate) return Promise.reject({ code: 'BRIDGE_RATE_LIMIT' });
  arr.push(now); callCount.set(method, arr);
  // schema 校验
  for (const [k, t] of Object.entries(reg.schema)) {
    const optional = t.endsWith('?');
    const type = t.replace('?', '');
    const v = params[k];
    if (v === undefined) { if (!optional) return Promise.reject({ code: 'BRIDGE_SCHEMA', field: k }); continue; }
    if (typeof v !== type) return Promise.reject({ code: 'BRIDGE_SCHEMA', field: k });
  }
  return new Promise((resolve, reject) => {
    const cbId = `cb_${crypto.randomUUID()}`;
    window[cbId] = (res) => { delete window[cbId]; res.ok ? resolve(res.data) : reject(res); };
    window.NativeBridge?.invoke(method, JSON.stringify(params), cbId) ??
      reject({ code: 'BRIDGE_UNSUPPORTED' });
    setTimeout(() => { delete window[cbId]; reject({ code: 'BRIDGE_TIMEOUT' }); }, 8000);
  });
}
```
