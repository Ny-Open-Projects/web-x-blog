---
title: [AGT-401] 笔试题——实现一个 ReAct 循环执行器（含护栏）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-401：手写一个 ReAct（推理-行动-观察）循环执行器

**需求与边界**：
- 输入：任务、工具集（name/schema/run）、LLM 客户端；输出：最终答案与执行轨迹。
- 边界要求：① 最大步数与成本熔断；② 工具参数 schema 校验失败带错误信息重试（≤1 次）；③ 工具抛异常不崩循环（转为观察反馈给模型）；④ 轨迹全程记录可回放。

**答**：
```javascript
async function reactAgent({ task, tools, llm, maxSteps = 8, costCap = 1.0 }) {
  const trace = []; let cost = 0; let prevError = null;
  const messages = [{ role: 'system', content:
    `你是任务执行器。每轮输出 JSON：
     {"thought":"...","tool":"名称或finish","args":{}}。
     工具失败时先分析原因再决定重试或换法。` },
    { role: 'user', content: task }];
  for (let step = 0; step < maxSteps; step++) {
    if (cost > costCap) return { answer: '预算熔断', trace, partial: true };
    const out = await llm(messages); cost += out.cost;
    const { thought, tool, args } = parseJson(out.text);   // 解析失败→重试提示
    if (tool === 'finish') return { answer: thought, trace };
    const def = tools.find(t => t.name === tool);
    if (!def) { messages.push(observe(`未知工具 ${tool}，可用：${tools.map(t=>t.name)}`)); continue; }
    const check = def.schema.safeParse(args ?? {});
    if (!check.success && !prevError) {                    // 参数错误重试一次
      prevError = check.error;
      messages.push(observe(`参数校验失败：${check.error}`));
      continue;
    }
    prevError = null;
    let observation;
    try { const r = await def.run(check.success ? check.data : args);
      observation = JSON.stringify(r).slice(0, 4000);      // 结果截断防爆
      cost += r.cost ?? 0;
    } catch (e) { observation = `工具异常：${e.message}`; } // 异常转观察
    trace.push({ step, thought, tool, args, observation });
    messages.push(observe(observation));
  }
  return { answer: '达到最大步数', trace, partial: true };
}
const observe = (o) => ({ role: 'user', content: `Observation: ${o}` });
```

**评分点**:
- 循环结构正确：解析→finish 判断→工具查找→schema 校验→执行→观察回填。
- 四类护栏齐全：步数熔断、成本熔断、参数错误重试上限、工具异常转观察不崩。
- 工具结果截断（防上下文爆炸）且轨迹全程记录可回放。
- 解析失败与未知工具有明确反馈路径（反馈给模型而非静默跳过）。
