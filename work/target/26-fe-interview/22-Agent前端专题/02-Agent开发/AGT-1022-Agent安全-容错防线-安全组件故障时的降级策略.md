---
title: [1022] 注入检测器挂了、分类器超时，安全防线怎么降级
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 可用性]
type: 面试题
---

## 1022：注入检测器挂了、分类器超时，安全防线怎么降级

**答**：
- fail-closed 原则分级：高危动作（外发/删除/支付）的防线故障必须 fail-closed（拒绝执行），可用性让位安全；低危链路（内容建议类）可 fail-open 降级 + 告警。
- 降级链：主检测器（LLM 分类器）→ 规则检测器（正则/特征词，便宜稳定）→ 静态白名单（只允许预审内容），每级延迟与召回不同，SLA 明确。
- 恢复回补：降级期间放行的内容打标，主检测器恢复后回补扫描，疑似违规追溯处理。
- 追问钩子：fail-closed 会不会把可用性搞崩？——会，所以「哪些动作 fail-closed」要按业务风险清单预定义并演练，事故现场再讨论就晚了。

```ts
async function guardOrDegrade(content, action) {
  try {
    return await withTimeout(detector.scan(content), 800);   // 主检测
  } catch {
    if (action.risk === 'high') return rejectFailClosed(action); // 高危拒绝
    const rule = ruleDetector(content);                       // 低危降级
    metrics.inc('guard_degraded');
    return rule.risky ? block(content) : passTagged(content);  // 打标待回补
  }
}
```
