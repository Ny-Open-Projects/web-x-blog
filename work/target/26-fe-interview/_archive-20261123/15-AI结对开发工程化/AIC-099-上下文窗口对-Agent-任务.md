---
title: [AIC-099] 上下文窗口大小对 Agent 任务能力有什么影响？「窗口幻觉」是什么现象？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-099：上下文窗口大小对 Agent 任务能力有什么影响？「窗口幻觉」是什么现象？
**答**：
- 影响：窗口决定任务复杂度上限——窗口不够时 agent 要么塞不下关键依赖（漏改），要么过度压缩上下文（丢失约束）；但大窗口 ≠ 好效果，注意力在超长上下文里会稀释，「大海捞针」类检索在中部内容上准确率下降。
- 窗口幻觉：agent 声称「已读取/已修改」了超出窗口或未实际操作的内容——它把「计划中的动作」叙述成「已完成」，这是 agent 报告必须与 diff 对账（AIC-098）的原因之一。
- 实践策略：单次窗口预算分配——系统提示+规则占 20%、任务与验收占 20%、代码上下文占 50%、缓冲 10%；长任务靠外部记忆（文件/清单）跨窗口衔接，而不是指望一个窗口装下一切。
- 验证手段：要求 agent 每次修改后重新读取文件确认（read-back），能显著压低「声称已改实际没改」。
- 追问钩子：面试官常追问「长上下文是不是万能」，答案是「能装下≠能用好」，引用注意力稀释和中间遗忘即可。

```javascript
// 窗口预算分配（与 AIC-148 笔试题同构）
const BUDGET = { rules: 0.2, task: 0.2, code: 0.5, buffer: 0.1 };
function allocate(windowTokens, { rules, task, code }) {
  const cap = (k, t) => t * BUDGET[k] * windowTokens;
  if (tokens(code) > cap('code', windowTokens)) throw new Error('代码上下文超预算，需裁剪');
  return { rules: cap('rules', windowTokens), task: cap('task', windowTokens), code: cap('code', windowTokens) };
}
```
