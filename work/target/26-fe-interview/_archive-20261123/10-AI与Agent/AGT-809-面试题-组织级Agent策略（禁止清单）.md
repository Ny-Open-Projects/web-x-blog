---
title: [AGT-809] 企业要限制 Agent 行为（禁止外发邮件带客户数据/禁止调用某类工具），策略体系怎么建？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-809：企业要限制 Agent 行为（禁止外发邮件带客户数据/禁止调用某类工具），策略体系怎么建

**答**：
- 策略三层：平台策略（SaaS 方硬规则，租户不可改）、租户策略（企业管理员配置：禁用工具/输出过滤/数据流向限制）、用户偏好（最低）。策略引擎在运行时关键点强制：工具调用前（拦截禁用工具）、输出后（内容过滤）、数据流（标记数据不可出域）。
- 数据流向限制是重点：给数据打「出域标记」（客户数据不出租户边界），Agent 组合工具时（读 CRM→发邮件）流经检查——读到的敏感数据不能进外发工具参数。
- 策略变更审计与生效：变更需审批+全租户生效通知，紧急封禁可秒级生效（事故响应）。

```javascript
const POLICY_CHECKS = {
  preTool: (tc, ctx) => !ctx.tenant.blockedTools.includes(tc.tool),
  postData: (data, nextTool) => nextTool.allowedData.includes(data.classification),
  output: (text, ctx) => !matchesDenyList(text, ctx.tenant.deny),
};
async function guardedCall(tc, ctx, dataFlow) {
  if (!POLICY_CHECKS.preTool(tc, ctx))
    return blocked(tc, 'tenant-policy');
  const incoming = dataFlow.current();            // 当前流经数据
  if (incoming && !POLICY_CHECKS.postData(incoming, tc.meta))
    return blocked(tc, `数据「${incoming.classification}」不可流向该工具`);
  return execute(tc);
}
```

