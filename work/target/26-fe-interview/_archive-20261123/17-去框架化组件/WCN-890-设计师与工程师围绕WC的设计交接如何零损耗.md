---
title: [WCN-890] 设计师与工程师围绕 WC 的「设计交接（handoff）」如何做到零损耗？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-890：设计师与工程师围绕 WC 的「设计交接（handoff）」如何做到零损耗？

**答**：
- 结论先行：交接损耗来自「信息在传输中丢失或变形」——解法是把设计意图变成「机器可读、代码可消费的单一真相源」，让工程师读的是数据而非猜截图。
- 单一真相源：设计稿用 Figma Variables（token）+ Auto Layout（间距/布局规则）+ 组件变体（状态），导出成 token JSON / schema，直接生成 CSS 变量与组件骨架——工程师不再「看图猜像素」。
- 交接内容标准化：每个组件交接包含——变体与状态清单、token 引用（而非硬编码值）、交互说明（hover/点击/键盘）、a11y 要求、边界情况（超长文本/空态）——用 checklist 保证不漏。
- 工具链打通：Figma → token → 代码生成 → Storybook，设计与代码双向可追溯（组件上标注对应设计节点）；视觉回归自动比对设计稿，偏差自动提醒。
- 协作机制：Design Engineer 角色作为桥梁；设计走查与代码 review 同步进行；设计变更通过 token/设计稿更新自动传导到代码（CI 检测差异）。
- 追问钩子：面试官会问「设计稿改了代码没跟上怎么办」——答：CI 定期比对设计稿 token 与代码 token 的哈希，不一致就告警；把「设计稿与代码同源」做成自动化管线，而非靠人记得同步。

```javascript
// 交接清单完整性校验：确保设计意图不丢
const HANDOFF = ['variants', 'tokens', 'interactions', 'a11y', 'edgeCases'];
function checkHandoff(spec) {
  const missing = HANDOFF.filter(k => !spec[k] || (Array.isArray(spec[k]) && !spec[k].length));
  return { ready: missing.length === 0, missing };
}
console.log(checkHandoff({
  variants: ['default', 'hover', 'disabled'],
  tokens: ['--color-primary'],
  interactions: ['click'],
  a11y: ['focus-visible'],
  // edgeCases 缺失 → 不 ready
}));
```
