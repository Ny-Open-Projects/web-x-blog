---
title: [AIC-616] 和 AI 聊久了，怎么早期发现它开始「幻觉漂移」？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-616：和 AI 聊久了，怎么早期发现它开始「幻觉漂移」？

**答**：
- 结论先行：**幻觉漂移的信号不是「它说错了」，而是「它开始编造不存在的东西并表现得自信」**。早期捕捉靠三根探针：引用校验、一致性校验、现实校验。
- 引用校验：AI 开始提到「项目里有个 `useFetchCache` 工具函数」——但仓库里根本没有。让它给出文件路径，一查便知。这是最早的信号（AIC-029 防幻觉验证）。
- 一致性校验：AI 前一轮说「用 A 方案」，后一轮的代码却按 B 方案写，且不承认改过。让它复述之前的决策，看是否自洽（AIC-586 上下文衰减）。
- 现实校验：让 AI 解释的代码跑一下，或让类型检查过一遍。漂移的 AI 会产出「看起来对但编译不过」的代码——编译错误是最便宜的照妖镜。
- 干预动作：一旦发现漂移，不要试图在会话里纠正（越纠越漂），而是立即「快照当前有效上下文 → 开新会话 → 提供确定性证据（真实文件路径/类型定义）」。
- 追问钩子：为什么「让它给文件路径」比「问它确不确定」更能识别幻觉？——因为「确不确定」的元问题 LLM 会自信地回答「我确定」（它对自己置信度没有可靠校准）；而具体事实（路径、签名）是可证伪的，一验证就露馅。

```typescript
// 幻觉漂移探针：从 AI 回答中抽取它声称的符号，对照真实仓库符号表
function detectHallucination(
  answer: string,
  realSymbols: Set<string>,
): { claimed: string[]; hallucinated: string[]; driftScore: number } {
  // 抽取反引号或驼峰命名的代码符号
  const claimed = [...answer.matchAll(/`([A-Za-z_$][\w$]*)`/g)].map(m => m[1]);
  const unique = [...new Set(claimed)];
  const hallucinated = unique.filter(s => !realSymbols.has(s) && s.length > 4);
  const driftScore = unique.length ? hallucinated.length / unique.length : 0;
  return { claimed: unique, hallucinated, driftScore };
}

const real = new Set(['useState', 'fetchUser', 'formatDate']);
const ans = '我们用 `useFetchCache` 缓存，再调用 `fetchUser` 拿数据';
console.log(detectHallucination(ans, real).hallucinated); // ['useFetchCache']
console.log(detectHallucination(ans, real).driftScore > 0); // true —— 漂移信号
```
