---
title: [PER-644] JSBridge 的安全设计：H5 调用 Native 能力的授权模型、白名单与参数校验怎么做？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-644：JSBridge 的安全设计：H5 调用 Native 能力的授权模型、白名单与参数校验怎么做？

**答**：
- JSBridge 是 H5 攻击 Native 的主通道，授权模型三层：**域名白名单**（只有业务域的 H5 能调 bridge，容器侧校验当前 URL 的 origin）、**API 分级**（只读类开放、写操作类需签名确认、资金/设备类仅原生页面可用）、**调用频控**（防恶意 H5 疯狂调起）。
- 参数校验在 Native 侧做而不是 H5 侧（H5 不可信）：schema 校验 + 长度/类型限制，防命令注入（拼 URL/拼命令的 bridge 方法是重灾区）。
- 回调安全：callbackId 不能成为任意 JS 执行入口（Native 侧只调用预注册的回调）；返回数据含敏感信息时校验请求方域名。
- 排查要点：grep bridge 方法清单，标注每个方法的谁可调（白名单域）、参数是否 schema 校验、是否拼命令三列，拼命令的方法（如 openUrl 拼进 Intent）全部改造。

```javascript

const bridgeSecurity = {
  auth: {
    domainWhitelist: '容器校验当前 H5 origin，白名单外 bridge 不可见',
    apiTiers: { read: '直接开放', write: 'H5 需带业务签名，Native 验签', fund: '仅原生页面，bridge 不暴露' },
    rateLimit: '单页面每秒 <= 20 次，超限告警',
  },
  params: { rule: 'Native 侧 schema 校验，不信任 H5 传入的任何值',
    forbid: '拼 URL/Intent/命令的 bridge 方法（openUrl 拼接类）必须改造为结构化参数' },
  callback: { rule: 'callbackId 只能命中预注册回调，禁止 eval/WebView.evaluateJavascript(任意串)' },
  audit: 'bridge 方法清单三列审计：谁可调 / 参数校验 / 是否拼命令',
};
console.log(bridgeSecurity.params.forbid);
```
