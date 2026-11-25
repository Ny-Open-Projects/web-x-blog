---
title: [AGT-873] 低代码平台接 Agent（自然语言生成页面配置），融合架构与边界怎么定？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-873：低代码平台接 Agent（自然语言生成页面配置），融合架构与边界怎么定

**答**：
- 架构：Agent 输出的是「平台 DSL/schema」（受控配置）而不是代码——低代码平台已有 schema 校验与渲染引擎，AI 只做 schema 生成，校验/渲染/版本管理复用平台能力。
- 边界：AI 生成的配置先落「草稿区」可视化预览，用户确认后才进正式页面；复杂逻辑（业务规则）不生成（低代码的规则引擎由人配），AI 只做布局/数据绑定/样式。
- 质量闭环：AI 生成配置的采纳率/修改幅度统计，修改幅度大的场景标记为"AI 不擅长"，路由到人工模板。

```javascript
async function nlToPage(prompt) {
  const schema = await ai.compose(prompt, {
    dsl: PLATFORM_DSL,                             // 受控schema
    allow: ['layout', 'binding', 'style'],
    forbid: ['business-rules'],                    // 规则引擎人工配
  });
  const valid = schemaValidate(schema);            // 平台校验复用
  return draftZone(valid, { preview: render(valid),
    confirm: '确认后进正式页面' });                 // 草稿区确认
}
```

