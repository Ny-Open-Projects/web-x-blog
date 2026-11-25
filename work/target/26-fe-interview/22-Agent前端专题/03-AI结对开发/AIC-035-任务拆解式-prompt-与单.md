---
title: [AIC-035] 大任务直接丢给 AI 为什么容易烂尾？怎么在 Prompt 层做「任务拆解」？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-035：大任务直接丢给 AI 为什么容易烂尾？怎么在 Prompt 层做「任务拆解」？
**答**：
- 烂尾机理：长输出后半段质量衰减（注意力稀释）、上下文窗口装不下所有依赖、单轮无法既规划又实现——任务越大失败率越高。
- Prompt 层拆解：先让 AI 输出「步骤计划」（文件清单 + 每步验收标准），人确认后再逐个文件执行，每步是一个小 prompt。
- 拆解粒度经验：一个 prompt 对应「一个文件或一个函数级改动」，输出控制在几百行以内；跨文件依赖用「上一步产物」作为下一步输入。
- 顺序有讲究：先类型/接口，再实现，最后测试——让模型沿着「契约 → 实现 → 验证」推进，减少接口漂移。
- 追问钩子：这套流程正是 Agent 模式的内核（规划→执行→验证循环），区别只是循环由人驱动还是 agent 自动驱动。

```javascript
// 人工驱动的逐步执行框架
async function stepwiseBuild(requirement) {
  const plan = await callLLM(`把需求拆成执行步骤：每步一个文件，给出验收标准。\n需求：${requirement}`);
  const steps = JSON.parse(plan); // [{ file, action, acceptance }]
  const results = [];
  for (const step of steps) {
    const prev = results.map(r => `// ${r.file}\n${r.code}`).join('\n');
    const code = await callLLM(`执行步骤：${JSON.stringify(step)}
已有产物（只读不改）：
${prev}
只输出本步骤文件，验收标准：${step.acceptance}`);
    results.push({ file: step.file, code });
  }
  return results;
}
```
