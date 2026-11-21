---
title: [ENG-071] 交互式 CLI 怎么实现？inquirer 和 prompts 怎么选？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-071：交互式 CLI 怎么实现？inquirer 和 prompts 怎么选？
**答**：
- prompts 轻量、API 声明式、支持用函数实现条件联动（上一题选了才继续问）；inquirer 生态更全、插件多。
- 交互设计原则：能推断的默认值直接给 initial，不要连环问；提供 --yes 参数跳过全部交互方便 CI。
- 必须处理 onCancel：用户 Ctrl+C 时清理已创建的目录再退出，不留半成品。
- 复杂向导（多步依赖前面的答案）用状态机思路组织，每步只依赖已收集的字段。

```javascript
import prompts from 'prompts';

const answers = await prompts(
  [
    { type: 'text', name: 'projectName', message: '项目名称', initial: 'my-app' },
    { type: 'select', name: 'css', message: 'CSS 方案', choices: [
      { title: 'Tailwind', value: 'tailwind' },
      { title: 'CSS Modules', value: 'css-modules' },
    ] },
    { type: 'confirm', name: 'needLint', message: '接入 ESLint？', initial: true },
    {
      // 条件联动：只有上一步选了 lint 才追问插件
      type: (prev) => (prev ? 'multiselect' : null),
      name: 'lintPlugins',
      message: '选择 lint 插件',
      choices: [{ title: 'stylelint', value: 'stylelint' }],
    },
  ],
  { onCancel: () => process.exit(0) } // 用户中断即退出，由上层清理目录
);
```
