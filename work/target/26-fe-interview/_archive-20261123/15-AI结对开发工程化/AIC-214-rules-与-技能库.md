---
title: [AIC-214] Cursor rules 与「技能/命令」（如自定义 slash command、agent 技能）如何配合分工？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-214：Cursor rules 与「技能/命令」（如自定义 slash command、agent 技能）如何配合分工？
**答**：
- rules 管「约束」（什么该做什么不该做），技能/命令管「流程」（一步步怎么做某类任务）。
- 高频任务封装成技能：发版流程、组件生成脚手架、故障排查手册——技能内可以引用规则。
- 规则防膨胀：过程性内容全部外移到技能，规则只留硬约束。
- 两者都要进评测：技能看任务成功率，规则看违规率。

```javascript
// 技能定义引用规则（伪代码）
const skill = {
  name: 'create-component',
  steps: ['确认命名符合 rules/components.mdc', '生成文件骨架',
          '写入示例与 a11y 属性', '运行 lint + 组件测试'],
  rulesReferenced: ['components.mdc', 'a11y.mdc'],
};
r
```
