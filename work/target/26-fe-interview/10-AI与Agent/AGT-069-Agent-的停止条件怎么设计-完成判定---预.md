---
title: [AGT-069] Agent 的停止条件怎么设计（完成判定 / 预算控制 / 循环检测）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-069：Agent 的停止条件怎么设计（完成判定 / 预算控制 / 循环检测）？
**答**：
- 必须有三重刹车：完成判定（模型声明 final 或用工具校验目标达成）、预算控制（步数/token/钱任一超限即停）、循环检测（重复动作签名命中即停）。
- 完成判定不能只信模型嘴上说完成：关键任务用工具校验（测试通过、目标字段非空）。
- 预算超限的退出要体面：输出「已完成的部分 + 未完成原因」，而不是裸报错。
- 循环检测：滑动窗口记录最近 N 步 `(tool, argsHash)` 签名，同签名重复出现即强制重规划或终止。

```typescript
import { z } from 'zod';

interface Budget { maxSteps: number; maxTokens: number; maxCostCents: number }
interface StopCheck { stop: boolean; reason?: string }

class StopController {
  private stepSignatures: string[] = [];
  private usedTokens = 0;
  private usedCostCents = 0;

  constructor(private budget: Budget) {}

  onStep(tool: string, args: unknown, usage: { tokens: number; costCents: number }): StopCheck {
    this.usedTokens += usage.tokens;
    this.usedCostCents += usage.costCents;
    // 循环检测：最近 6 步内同签名出现 3 次视为打转
    const sig = `${tool}|${stableHash(JSON.stringify(args))}`;
    this.stepSignatures.push(sig);
    const recent = this.stepSignatures.slice(-6);
    if (recent.filter((s) => s === sig).length >= 3) return { stop: true, reason: '检测到循环执行' };
    if (this.stepSignatures.length >= this.budget.maxSteps) return { stop: true, reason: '步数预算耗尽' };
    if (this.usedTokens >= this.budget.maxTokens) return { stop: true, reason: 'token 预算耗尽' };
    if (this.usedCostCents >= this.budget.maxCostCents) return { stop: true, reason: '成本预算耗尽' };
    return { stop: false };
  }

  gracefulExit(reason: string, partialResults: unknown) {
    return { completed: false, reason, partialResults }; // 带着已完成部分体面退出
  }
}
```
