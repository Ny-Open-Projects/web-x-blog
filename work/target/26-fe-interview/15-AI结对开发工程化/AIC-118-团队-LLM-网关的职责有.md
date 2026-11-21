---
title: [AIC-118] 团队自建 LLM 网关要承担哪些职责？为什么要收敛而不是各工具直连模型？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-118：团队自建 LLM 网关要承担哪些职责？为什么要收敛而不是各工具直连模型？
**答**:
- 直连的问题：密钥散落各处（泄漏面大）、无统一日志（排障靠猜）、成本不可见、供应商切换要改 N 处、无脱敏（AIC-076 的内容层防线缺失）。
- 网关职责清单：① 鉴权与配额（按团队/项目限流）② 脱敏中间件（手机号/密钥/内网 IP）③ 日志与计费（trace、token、费用，脱敏存储）④ 路由与降级（模型路由 AIC-160、供应商故障切换）⑤ prompt 版本与注入防护的统一卡点。
- 收敛原则：「所有外部 LLM 调用必须过网关」写成红线（AIC-075），网关是唯一持有真实密钥的地方。
- 成本视角：收敛后才有按项目的成本分账，AI 产出ROI 分析（AIC-050/087）才有数据基础。
- 追问钩子：网关本身要高可用——LLM 挂了业务不能挂，降级策略（缓存、备用供应商、确定性检查兜底）是设计重点。

```javascript
// 网关请求处理管道
async function gateway(req) {
  const { sanitized, hits } = sanitize(req.prompt);       // 脱敏
  const model = route(req);                                // 路由：按任务类型选模型
  const budget = checkBudget(req.project);                 // 配额
  if (!budget.ok) throw new Error('quota exceeded');
  const res = await provider.call(model, { ...req, prompt: sanitized });
  logTrace(req, { model, res, maskedHits: hits });         // 留痕计费
  return res;
}
```
