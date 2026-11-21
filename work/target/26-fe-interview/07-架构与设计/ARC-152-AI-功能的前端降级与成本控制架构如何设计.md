---
title: [ARC-152] AI 功能的前端降级与成本控制架构如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-152：AI 功能的前端降级与成本控制架构如何设计？
**答**：
- 降级链路设计：AI 能力必须有"非 AI 的可接受替代"——AI 摘要失败退规则摘要（首句+关键词），退无可退则隐藏入口（不显示报错卡片）；每个 AI 功能定义 degradation ladder 并写进设计文档。
- 成本控制四板斧：模型分层（简单任务小模型）、缓存（相同输入 hash 命中直接返回）、用户配额（按用户分层限制次数）、会话截断（上下文裁剪策略），前端负责配额提示与"输入引导"（控制输入长度）。
- 体验预算：AI 接口超时即放弃（如 8s），转降级；流式场景设置首 token 超时（2s）——用户对"转圈"的容忍远低于对"降级结果"的容忍。
- 开关与灰度：AI 功能独立 feature flag，支持按用户比例/租户关闭，成本超预算可一键熔断（熔断是成本失控的最后防线）。

```typescript
// AI 功能降级与成本控制（前端编排层）
type SummaryResult = { source: 'ai'; text: string } | { source: 'rules'; text: string } | { source: 'none' };

async function renderSummary(order: Order, ui: SummaryUI): Promise<SummaryResult> {
  if (!featureFlag.enabled('ai-summary', order.userId)) return { source: 'none' };  // 一键熔断
  if (exceededQuota(order.userId)) {                        // 用户配额：展示引导而非报错
    ui.showQuotaHint(); return { source: 'rules', text: ruleSummary(order) };
  }
  try {
    const res = await withTimeout(
      api.ai.summarize({ input: truncate(order, 4000) }),   // 上下文裁剪控制成本
      { overall: 8000, firstToken: 2000 },                  // 首 token 超时提前放弃
    );
    return { source: 'ai', text: res.text };
  } catch (e) {
    track('ai_degrade', { feature: 'summary', reason: e.code });
    // 降级阶梯：AI 失败 → 规则摘要（用户几乎无感），永远不显示报错卡片
    return { source: 'rules', text: ruleSummary(order) };
  }
}
// 成本监控闭环：每调用上报 { feature, model, tokens, cacheHit, degraded }
// 成本看板按 feature 聚合，预算超 80% 告警，超 100% 自动触发 featureFlag 熔断
```

---

## 十八、数据与安全专项（ARC-153 ~ ARC-159）
