---
title: [AGT-882] 团队引入 AI 工程化（人人都会用 vs 专业小组），组织上怎么落地？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-882：团队引入 AI 工程化（人人都会用 vs 专业小组），组织上怎么落地

**答**：
- 双轨制：全员基础（工具使用/prompt 基础/门禁遵从，1~2 次培训+文档）+ 专业小组（AI 工程化小组：rules/门禁/评测/平台建设，2~3 人兼职）——专业能力集中，普通能力普及。
- 专业小组的职责：AI 产出质量度量体系、rules 与模板维护、疑难场景攻坚、规范演进；对全团队是"服务方"不是"审批方"（赋能不设卡）。
- 演进指标：全员 AI 使用率/采纳率/质量事件率，小组产出的工具被自发使用的比例（推广靠好用不靠行政）。

```javascript
const AI_ORG = {
  all: { skills: ['工具使用', '门禁遵从'], onboarding: '2h' },
  guild: { size: '2-3人兼职',
    duties: ['度量体系', 'rules维护', '评测', '攻坚'],
    principle: '赋能不设卡' },
};
function health() {
  return { adoption: usageRate(), quality: incidentRate(),
   自发使用: guildToolsUsage() > 0.6 };            // 好用才有生命力
}
```

