---
title: [AIC-136] AI 能辅助可访问性（a11y）到什么程度？生成的组件怎么自动检查 ARIA 用法？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-136：AI 能辅助可访问性（a11y）到什么程度？生成的组件怎么自动检查 ARIA 用法？
**答**：
- AI 能做的：按规则生成语义化结构（button 不是 div、正确 heading 层级）、补 aria 属性、写 alt 文案、生成键盘导航逻辑（焦点陷阱、顺序）——前提是规则文件写清 a11y 约定。
- AI 的弱项：真实屏幕阅读器体验（朗读顺序与语义的实际效果）、颜色对比的实际感知、动效对前庭障碍的影响——需要真实工具与用户验证。
- 自动检查层：静态（eslint-plugin-jsx-a11y 抓 ARIA 误用）、运行时（axe-core 扫渲染结果）、E2E（键盘操作脚本）——AI 生成 → 三层自动检查 → 人工抽查，检查失败回喂 AI 修复。
- 规则化建议：把团队 a11y 约定写进规则文件（「所有交互元素必须可键盘操作」「图标按钮必须有 aria-label」），让 AI 生成时就遵守而不是事后修。
- 追问钩子：a11y 是「AI 生成质量门禁」的典型切片——规则前置 + 自动检查 + 人工抽验，三段式适用于所有非功能需求。

```javascript
// axe-core 自动检查接入（生成组件的验收闸门）
async function verifyA11y(component, mount) {
  const { container } = mount(component);
  const results = await axe.run(container);
  const violations = results.violations.map(v => ({
    rule: v.id, nodes: v.nodes.length, help: v.help,
  }));
  return violations.length ? { pass: false, violations } : { pass: true };
}
```
