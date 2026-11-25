---
title: [AIC-682] 企业级 AI 编码平台应该分哪几层？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-682：企业级 AI 编码平台应该分哪几层？

**答**：
- 结论先行：**分四层——「基础设施层（模型/算力）→ 网关层（路由/鉴权/计量）→ 能力层（补全/审查/Agent）→ 场景层（IDE/CI/门户）」**。分层让「换模型不换能力、换 IDE 不换后端」。
- 各层职责：1) **基础设施层**：多模型接入（云/本地/多厂商）、算力调度、模型评测——对上提供统一的模型调用接口（AIC-250 本地模型 / AIC-267 模型替换）；2) **网关层**：统一鉴权、配额计量、审计日志、智能路由（隐私分级 AIC-637 / 成本路由 AIC-246）——所有 AI 调用的单一入口（AIC-118 网关职责）；3) **能力层**：把模型包装成可复用能力——代码补全、审查、测试生成、Agent 编排、知识检索——能力可组合（AIC-358 Agent 技能）；4) **场景层**：各入口（IDE 插件、CI 门禁、开发者门户）消费能力——同一能力在不同场景复用。
- 分层的价值：1) **解耦**：换模型只动基础设施层；2) **收敛**：鉴权/审计在网关统一，不散落各处；3) **复用**：能力被多场景共享，避免重复建设。
- 追问钩子：为什么「网关层」必须独立而不是塞进各 IDE 插件？——因为鉴权/计量/审计是「必须一致」的横切关注点；塞进各插件会导致口径不一、审计遗漏、密钥散落——独立成网关才能做到「单一入口、统一策略」，这是平台化的核心。

```typescript
// 分层架构的依赖方向：上层依赖下层接口，不依赖具体实现
interface ModelProvider { complete(prompt: string, opts?: any): Promise<string> }

class Gateway {
  constructor(private provider: ModelProvider, private audit: (e: any) => void) {}
  async call(prompt: string, user: string) {
    // 统一鉴权/计量/审计
    this.audit({ user, promptLen: prompt.length, ts: Date.now() });
    return this.provider.complete(prompt);
  }
}

// 能力层：消费网关，提供可复用能力
class CodeReviewCapability {
  constructor(private gw: Gateway) {}
  async review(diff: string, user: string) {
    return this.gw.call(`审查以下代码变更：
${diff}`, user);
  }
}

// 换模型只需换 provider，上层无感
const gateway = new Gateway({ complete: async p => `reviewed(${p.length})` }, console.log);
const review = new CodeReviewCapability(gateway);
review.review('diff content', 'alice').then(r => console.log(r.startsWith('reviewed'))); // true
```
