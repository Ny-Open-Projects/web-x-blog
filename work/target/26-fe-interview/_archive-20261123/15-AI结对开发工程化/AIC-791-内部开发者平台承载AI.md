---
title: [AIC-791] 如何用内部开发者平台承载 AI 能力
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-791：如何用内部开发者平台承载 AI 能力

**答**：
- 结论先行：IDP（Internal Developer Platform）= 把 AI 能力作为「黄金路径」的一部分嵌入开发者日常工作流（新建项目、提 PR、发布），让开发者「无感」用上 AI，而不是额外学一套工具。
- 落地：1) 项目模板内置 AI 规则/技能配置；2) PR 流程自动触发 AI 审查；3) 门户提供能力目录与文档；4) 用「可发现、可自助、可治理」三原则衡量 IDP 成熟度。
- 价值：AI 从「个人工具」升级为「组织能力」，由平台团队统一治理（版本、成本、安全）。
- 追问钩子：为什么 AI 能力要嵌进「黄金路径」而不是单独推广？——单独推广依赖个人意愿，嵌入路径则成为默认选项，采用率与一致性都更高。

```javascript
// IDP 黄金路径：项目模板内置 AI 配置
function goldenPath(template) {
  return {
    scaffold: ['src/', 'tests/'],
    aiDefaults: { rules: 'team.rules', review: true, testGen: true }, // 默认开启 AI 能力
    docs: true,
  };
}
const project = goldenPath('react-ts');
console.log(project.aiDefaults.review); // true —— 新建项目即自带 AI 审查
```
