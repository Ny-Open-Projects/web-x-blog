---
title: [AIC-622] 多轮对话里 AI 开始「原地打转」，怎么识别并换策略？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-622：多轮对话里 AI 开始「原地打转」，怎么识别并换策略？

**答**：
- 结论先行：**原地打转的本质是「用同一类方法反复尝试」**。识别看两个信号——diff 相似度高（改来改去都是那几行）、错误签名不变（AIC-609）；破解靠「换维度」而非「加力度」。
- 识别方法：1) 记录每轮的 diff 与错误签名，连续 2-3 轮高度相似即判定打转（AIC-430 循环检测）；2) 观察 AI 的措辞——开始重复「我修改了...应该可以了」却没给新根因，是典型打转信号。
- 换策略四招：1) **换输入**：补充新证据（真实报错堆栈、复现步骤），而非重复「还是不对」；2) **换角色**：让 AI「假装是审查者」找自己代码的问题，而非继续当实现者；3) **换粒度**：把问题拆小，先让 AI 只解决一个子问题（AIC-311 任务拆解）；4) **换模型/换会话**：换个模型或新会话，打断思维定势（AIC-084 多 Agent）。
- 「加力度」为什么无效：把 prompt 写得更严厉（「你必须修好」）不改变 AI 的方法集合，只会让它更自信地重复同样错误。
- 追问钩子：为什么「让 AI 当审查者」能破局？——因为生成和审查调用的是不同的「思维框架」；同一个 AI 在审查模式下会应用到生成模式下没用的检查规则，相当于用「第二双眼睛」看同一份代码，能发现实现时的盲点。

```typescript
type Turn = { diff: string; error: string; cause?: string };

function isSpinning(turns: Turn[], window = 3): boolean {
  if (turns.length < window) return false;
  const tail = turns.slice(-window);
  const sameError = tail.every(t => t.error === tail[0].error);
  const sameDiff = tail.every(t => t.diff === tail[0].diff);
  const noNewCause = tail.every(t => !t.cause);
  return (sameError && noNewCause) || sameDiff;
}

function pickStrategy(turns: Turn[]): string {
  if (!isSpinning(turns)) return 'continue';
  if (turns.every(t => !t.cause)) return 'add-evidence';   // 缺根因 → 补证据
  if (turns.length > 5) return 'switch-model';            // 长期打转 → 换模型
  return 'role-swap-to-reviewer';                          // 否则换审查视角
}

console.log(pickStrategy([
  { diff: 'a', error: 'E', cause: undefined },
  { diff: 'a', error: 'E', cause: undefined },
  { diff: 'a', error: 'E', cause: undefined },
])); // 'add-evidence'
```
