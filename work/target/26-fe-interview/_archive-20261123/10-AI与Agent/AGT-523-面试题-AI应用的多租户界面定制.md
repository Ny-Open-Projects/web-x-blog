---
title: [AGT-523] SaaS 化的 AI 产品，多租户的品牌定制（logo/主题/系统提示人设）怎么在前端落地？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-523：SaaS 化的 AI 产品，多租户的品牌定制（logo/主题/系统提示人设）怎么在前端落地

**答**：
- 品牌层用 CSS 变量 + 运行时主题注入（租户配置拉取后 setProperty），不要为每个租户打包一份主题。
- 「人设定制」双通道：租户可配系统提示的附加段（人设/口吻/禁词），前端展示配置生效状态，并在调试面板可见最终拼装的 system。
- 边界必须保留：平台安全规则（合规声明、免责话术、禁止的行为）是租户不可覆盖的硬编码层，防止租户配出"扮演不受限模型"。

```javascript
async function applyTenantTheme(tenantId) {
  const t = await api.tenantConfig(tenantId);
  for (const [k, v] of Object.entries(t.theme))   // { --brand: '#x08', ... }
    document.documentElement.style.setProperty(k, v);
  copilot.setPromptSuffix(t.personaSuffix);       // 人设附加段
  copilot.setLockedPrompt(SAFETY_BASE);           // 平台硬规则不可覆盖
}
```

