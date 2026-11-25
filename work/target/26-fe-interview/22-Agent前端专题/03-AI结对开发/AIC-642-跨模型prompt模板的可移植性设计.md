---
title: [AIC-642] 跨模型的 Prompt 模板怎么设计才可移植？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-642：跨模型的 Prompt 模板怎么设计才可移植？

**答**：
- 结论先行：**可移植的 Prompt 模板 =「模型无关的核心意图 + 模型自适应的外壳」**。不要为每个模型写一套 prompt（维护地狱），也不要假设一套 prompt 在所有模型上表现一样（AIC-270 上下文偏好差异）。
- 分层设计：1) **核心层**（模型无关）：任务目标、约束、验收标准、few-shot 示例——这些是意图本身，所有模型都吃；2) **适配层**（模型相关）：格式偏好（有的吃 markdown，有的吃 XML 标签）、system/user 角色分配、token 预算——按模型配置切换。
- 实现：用模板引擎把核心层与适配层分离，渲染时根据目标模型选择适配器（AIC-414 模板渲染器）。核心层只写一次，新模型接入只写一个适配器。
- 验证：新模型接入时，用固定的评测集跑核心层，确认表现达标再上线；不达标只调适配器，不改核心层意图——避免「为了迁就某模型把需求改歪」。
- 追问钩子：为什么「意图与格式要分离」？——因为意图是稳定的（需求不变），格式是多变的（换模型就要调）；把稳定部分和易变部分解耦，换模型时只动易变部分，核心意图零回归——这是软件工程「关注点分离」在 Prompt 工程的应用。

```typescript
type Model = 'claude'|'gpt'|'qwen';

const CORE = `目标：{goal}
约束：{constraints}
输出：{format}`;

const ADAPTERS: Record<Model, { wrap: (core: string) => string; formatHint: string }> = {
  claude: { wrap: c => `<task>
${c}
</task>`, formatHint: '用 markdown' },
  gpt:    { wrap: c => `### 任务
${c}`, formatHint: '用 JSON' },
  qwen:   { wrap: c => `【任务】${c}【/任务】`, formatHint: '用中文 markdown' },
};

function render(model: Model, goal: string, constraints: string) {
  const core = CORE.replace('{goal}', goal)
    .replace('{constraints}', constraints)
    .replace('{format}', ADAPTERS[model].formatHint);
  return ADAPTERS[model].wrap(core); // 核心不变，只换外壳
}

console.log(render('claude', '修bug', '不改API').startsWith('<task>')); // true
console.log(render('gpt', '修bug', '不改API').includes('### 任务')); // true
```
