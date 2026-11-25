---
title: [MFW-620] 渲染模式选择决策树：SSG/ISR/SSR/Edge 的路由级决策
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-620：渲染模式选择决策树

**答**:
- 路由级决策树：1) 内容个性化？→ SSR/PPR（无缓存）；2) 内容可缓存 × 变更频率？→ 变更秒级 = ISR 短 TTL 或 on-demand；分钟级 = ISR；小时级 = SSG；3) 数据量？→ 百万页 = 按需（fallback）+ 热点预渲染；4) SEO 关键？→ 静态化优先（SSG/ISR——首包完整）；5) 用户态占比？→ 高 = PPR（壳静态+洞动态）；低 = 全静态 + client fetch 用户态。
- 混合策略的现实：一个应用的路由是「频谱」——首页 SSG、商品 ISR、购物车 SSR、搜索 PPR——「路由级渲染决策」是元框架架构的核心输出（RBL-620 的决策树落到每条路由）。
- 决策的成本矩阵：SSG（构建成本/CDN 成本/更新延迟）、ISR（重生成成本）、SSR（每请求成本）、Edge（区域 RTT）——「成本模型」（RBL-934）的渲染维度。
- 追问钩子：为什么「路由级渲染决策」要文档化（决策记录）而不是「每个开发者随手定」？——渲染模式是「成本与体验的架构决策」（每请求渲染 = 持续成本 vs 静态 = 更新延迟）；随手定 = 同类页面不同模式（成本不可预测——路由画像审计 RBL-561 的漂移）；决策记录（ADR per 路由/类路由）让模式选择可复审、可迁移（升级时的行为基线 RBL-576）——决策的「文档化」是可维护性的最低要求（RBL-671 ADR）。

```typescript
// 路由级渲染决策
type RenderMode = 'ssg' | 'isr' | 'ssr' | 'edge' | 'ppr';
function decideRenderMode(page: PageProfile): RenderMode {
  if (page.personalization > 0.5) return page.criticalLCP ? 'ppr' : 'ssr';
  if (!page.cacheable) return 'ssr';
  if (page.changeFreqSec <= 5) return 'ssr';             // 秒级变更：实时
  if (page.changeFreqSec <= 600) return 'isr';           // 分钟级：ISR
  if (page.entityCount > 100_000) return 'isr-on-demand'; // 百万级：按需 + 热点
  return 'ssg';                                          // 小时级变更：全静态
}
// 每路由记录决策（ADR）
// routes.adr.md
// | route | mode | 理由 | 变更频率 | 个性化 |
// | / | ssg | 首页稳定 | 24h | 无 |
// | /p/[id] | isr 60s | 价格分钟级 | 60s | 无 |
// | /cart | ssr | 每用户 | 实时 | 100% |
// | /search | ppr | 壳静态+结果动态 | 实时 | 部分 |
```
