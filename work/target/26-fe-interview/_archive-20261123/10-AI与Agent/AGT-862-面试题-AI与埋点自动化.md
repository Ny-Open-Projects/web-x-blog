---
title: [AGT-862] 埋点（事件定义/参数/上报）用 AI 辅助的工程化：一致性怎么保证？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-862：埋点（事件定义/参数/上报）用 AI 辅助的工程化：一致性怎么保证

**答**：
- 埋点一致性靠「事件 schema 中心」：事件定义（名/参数/触发时机）单一来源注册，AI 根据 DOM/交互意图生成的是「对 schema 的实现」而不是新事件——AI 不得发明事件名（命名漂移是埋点灾难之源）。
- 自动验证：开发环境埋点实时校验（参数类型/必填/枚举），不符即 console 告警；schema 变更影响面分析（哪些页面用了旧参数）。
- AI 的增值点：从 PR diff 推断「需要补埋点的交互」（新增按钮无埋点→提示），从漏斗分析发现冗余事件。

```javascript
// 事件 schema 中心：AI 只做实现
const EVENT_SCHEMA = registry.get('order_submit', {
  params: { orderId: 'string', amount: 'number' },
});
function aiInstrument(el, intent) {
  const match = registry.findByIntent(intent);     // 匹配已有schema
  if (!match) return flag('需注册新事件schema', intent);  // 不发明
  return track(match.name, validate(match.schema, params));
}
```

