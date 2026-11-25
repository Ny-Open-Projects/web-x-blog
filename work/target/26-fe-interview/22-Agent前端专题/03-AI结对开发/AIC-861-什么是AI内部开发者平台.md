---
title: [AIC-861] 什么是「AI 内部开发者平台」（AI-IDP），和工具集合有什么区别？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-861：什么是「AI 内部开发者平台」（AI-IDP），和工具集合有什么区别？
**答**：
- 工具集合是「我们买了 Copilot、接了 GPT API、有个 prompt 文档」——各自为政、重复建设、体验割裂。AI-IDP 是**把 AI 能力做成可被自助消费的平台产品**：统一入口、统一 SDK、统一治理、可观测、可自助接入。
- 核心特征：**自助服务**（团队不用找平台团队排期就能接入）、**标准化抽象**（模型/Prompt/工具统一接口）、**分层治理**（平台团队管底座，业务团队管自己的 prompt 与评测）、**可度量的价值**（平台化收益有数据）。
- 关键组件：模型网关、能力注册表、统一 SDK、评测平台、血缘与可观测、权限与配额、自助门户与文档。
- 平台 vs 项目的区别：平台有**多消费者**和**长期演进**，需要产品思维（用户是谁、痛点是什么、如何度量成功），而不是一次性交付。
- 追问钩子：能说出「平台的核心不是技术栈而是自助服务 + 多消费者 + 产品化运营」的候选人，理解平台化的组织属性。

```typescript
// AI-IDP 的最小骨架：统一入口 + 自助接入 + 治理
type Capability = 'chat' | 'embed' | 'evaluate' | 'search';

class AIIDP {
  constructor(private adapters: Map<string, any>,
              private registry: Map<Capability, string>) {}

  // 业务团队只需声明能力与租户，平台负责选型、配额、血缘
  async use(cap: Capability, input: any, tenant: string) {
    const modelId = this.registry.get(cap);
    if (!modelId) throw new Error(`capability not available: ${cap}`);
    const adapter = this.adapters.get(modelId);
    // 真实实现中此处串联配额(AIC-813)、血缘(AIC-810)、评测(AIC-821)
    return adapter.run(input, { tenant, modelId, cap });
  }
  // 自助接入：业务注册自己的 prompt 模板与评测集
  registerCapability(cap: Capability, modelId: string) {
    this.registry.set(cap, modelId);
  }
}
const idp = new AIIDP(new Map(), new Map());
idp.registerCapability('chat', 'gpt-x');
// 业务团队调用 idp.use('chat', ...) 即可，无需关心底层模型
```
