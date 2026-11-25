---
title: [AIC-612] AI 结对时怎么保护「心流」不被 AI 频繁打断？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-612：AI 结对时怎么保护「心流」不被 AI 频繁打断？

**答**：
- 结论先行：**把 AI 从「同步打断式」改成「异步批处理式」**。IDE 补全每一键都弹建议、Agent 每改一处都要审批，是心流的两大杀手；正确做法是批量收集 AI 输出，在自己节奏点统一处理。
- 补全层面：调高补全延迟、关闭自动 inline 接受，只在主动触发（Tab）时采纳；复杂函数写完后一次性让 AI  review，而不是写一行问一行（AIC-531 防抖与取消）。
- Agent 层面：把「需要人审批」的点收敛到任务边界（开始前确认任务卡、结束后验收），执行中间不打断；用「任务队列」连续跑多个任务，人只在队列空了之后统一 review（AIC-114 / AIC-356 多任务混跑）。
- 节奏设计：番茄钟式——专注时段关掉 AI 通知，休息时段集中处理 AI 产出与 prompt 调整；把「与 AI 对话」本身也当作需要专注的活动，而非后台常驻。
- 追问钩子：为什么「批处理 AI 输出」比「实时交互」更保护心流？——因为人的注意力切换有成本（context switch cost），每次打断后需要数十秒重新进入状态；批处理把 N 次切换压缩成 1 次，省下的是复利。

```typescript
// 批处理式 AI 建议队列：不在生成时打断，攒到检查点统一处理
class SuggestionBatcher {
  private queue: { file: string; line: number; text: string }[] = [];
  private timer: ReturnType<typeof setTimeout> | null = null;

  push(s: { file: string; line: number; text: string }, flushMs = 5000) {
    this.queue.push(s);
    if (this.timer) clearTimeout(this.timer);
    // 攒够一批或用户到检查点才 flush，不实时弹出
    this.timer = setTimeout(() => this.flush(), flushMs);
  }

  flush() {
    // 一次呈现所有建议，人按自己节奏逐条采纳/忽略
    console.log(`[检查点] 共 ${this.queue.length} 条 AI 建议待处理`);
    this.queue.forEach(s => console.log(`${s.file}:${s.line} ${s.text}`));
    this.queue = [];
    this.timer = null;
  }
}
```
