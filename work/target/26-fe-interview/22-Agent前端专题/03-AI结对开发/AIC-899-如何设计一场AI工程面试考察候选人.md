---
title: [AIC-899] 让你设计一场考察「AI 工程能力」的面试，怎么考才不流于形式？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-899：让你设计一场考察「AI 工程能力」的面试，怎么考才不流于形式？
**答**：
- 别考「你知道哪些 AI 工具」（背答案），要考**判断力与实践**：给真实场景让候选人做决策并追问「为什么」，看的是思维过程而非知识点罗列。
- 设计三类题：**① 场景决策题**——「AI 生成的代码上线出了事故，你怎么复盘和防复发？」看他是否会问版本、上下文、守卫（AIC-891）；**② 笔试/实操题**——现场写个小工具（如规则合并、门禁引擎），看工程实现与边界处理；**③ 反直觉追问**——「采纳率 99% 一定好吗？」看他能否识别指标博弈（AIC-848）。
- 关键考察点：是否把 AI 当「工具」而非「魔法」（知道它的边界）、是否有质量与风险意识、是否能把技术方案讲成业务价值、是否有沉淀与系统思维。
- 评分要**可观察**：用行为化评分表（「能说出模型/prompt 版本对事故的影响」= 加分），而不是「感觉不错」。面试官自己要知道正确答案的样子。
- 追问钩子：能说出「考判断力而非背工具名 + 用可观察的评分表 + 包括反直觉追问」的候选人，不仅懂 AI 工程还懂如何评估它。

```typescript
type Question = { type: 'scenario'|'coding'|'counterintuitive'; prompt: string;
  signals: string[] }; // signals：回答中应出现的得分信号

const interview: Question[] = [
  { type:'scenario', prompt:'AI 生成代码上线出事故，如何复盘？',
    signals:['问模型/prompt版本','关注上下文缺口','产出可执行守卫','不甩锅AI'] },
  { type:'coding', prompt:'实现一个规则文件合并器（含 glob 匹配）',
    signals:['边界处理','glob转义正确性','可运行代码','复杂度意识'] },
  { type:'counterintuitive', prompt:'采纳率 99% 说明 AI 用得很好吗？',
    signals:['存活率','指标博弈','组合指标','不用于个人考核'] },
];
function score(answers: Record<number, string>) {
  return interview.map((q, i) => ({
    type:q.type,
    hit:q.signals.filter(s => answers[i]?.includes(s)).length,
    total:q.signals.length,
    // 按信号命中而非主观感觉评分
  }));
}
// 面试官用 signals 清单对照候选人回答，评分可观察、可复现
```
