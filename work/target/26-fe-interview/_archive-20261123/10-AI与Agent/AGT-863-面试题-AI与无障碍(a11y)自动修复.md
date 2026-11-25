---
title: [AGT-863] AI 辅助 a11y 修复（自动补 alt/aria），哪些能自动、哪些必须人工判断？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-863：AI 辅助 a11y 修复（自动补 alt/aria），哪些能自动、哪些必须人工判断

**答**：
- 可自动：alt 缺失但图片有文件名/周边文本可推断的（低风险补齐，标注"自动生成待人工确认"）、aria 属性机械修复（按钮缺 type/tabindex 顺序）、对比度计算与配色建议。
- 必须人工：alt 的语义描述（描述意图而非外观，AI 猜意图不可靠）、复杂交互的键盘导航设计、可理解性判断（表单错误提示的措辞）。
- 门禁化：a11y 扫描（axe）进 CI，错误级阻断——AI 先修一轮机械问题，把人工审查集中在语义问题。

```javascript
async function a11yAutoFix(page) {
  const issues = await axe.run(page);
  const auto = issues.filter(i => FIXABLE.has(i.id));  // 机械可修
  const patches = await ai.fix(auto, { mark: 'auto-generated' });
  return {
    autoPatched: patches,                          // 标注待确认
    humanRequired: issues.filter(i => !FIXABLE.has(i.id))
      .map(i => ({ id: i.id, why: NEEDS_HUMAN[i.id] })), // 语义问题给原因
    gate: issues.filter(i => i.impact === 'critical'),
  };
}
```

