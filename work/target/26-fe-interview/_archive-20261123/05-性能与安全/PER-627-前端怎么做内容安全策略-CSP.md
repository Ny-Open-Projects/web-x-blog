---
title: [PER-627] 前端怎么做内容安全策略（CSP）的灰度上线？Report-Only 到 Enforce 的推进节奏
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-627：前端怎么做内容安全策略（CSP）的灰度上线？Report-Only 到 Enforce 的推进节奏

**答**：
- 推进四阶段：①**观测**（Report-Only 上线，违规只上报不拦截，跑 2~4 周收集真实违规分布）；②**误报治理**（分类违规：业务确实需要的 -> 加白名单；第三方导致的 -> 换接入方式；攻击尝试的 -> 保持拦截意图）；③**灰度强制**（按用户/路由比例下发 Enforce 头，其余保持 Report-Only，对比两组错误率）；④**全量强制**（保留 Report-Only 双头观察一个月防回归）。
- 技术要点：CSP 头由网关统一注入更可控（应用侧漏配某服务就破防）；nonce 模式比白名单模式抗 XSS 更强（`script-src 'nonce-xxx' 'strict-dynamic'`），但要求所有脚本加载走 nonce 注入，改造量大，按业务规模取舍。
- 回归监控：Enforce 后 `securitypolicyviolation` 事件与 CSP report-uri 双通道收数，违规数突增（新发版引入内联脚本）自动关联发版告警。
- 常见坑：`'unsafe-inline'` 与 nonce 不能共存（存在 unsafe-inline 时 nonce 被忽略）、`strict-dynamic` 会使白名单失效、SRI 与 CSP 组合时 crossorigin 必须正确。

```javascript

const cspRollout = {
  phase1: { header: "Content-Security-Policy-Report-Only: default-src 'self'; report-uri /csp-report", weeks: 3 },
  phase2: { rule: '违规分类：业务白名单 / 第三方改造 / 攻击保持拦截', output: '收紧后的策略版本 v2' },
  phase3: { gray: '按 uid 尾号 10% 下发 Enforce，对照组 Report-Only',
    compare: 'JS 错误率/页面可用性 diff < 0.1% 才放量' },
  phase4: { both: 'Enforce + Report-Only 双头并行一个月' },
  gotchas: ["'unsafe-inline' 存在时 nonce 被忽略", "strict-dynamic 使 host 白名单失效",
    'SRI 需 crossorigin=anonymous 配合'],
};
console.log(cspRollout.phase3.gray);
```
