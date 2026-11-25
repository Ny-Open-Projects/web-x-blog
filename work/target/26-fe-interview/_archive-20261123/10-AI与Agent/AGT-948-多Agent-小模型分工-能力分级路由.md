---
title: [948] 多 Agent 系统怎么把简单子任务路由给小模型省钱
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 成本]
type: 面试题
---

## 948：多 Agent 系统怎么把简单子任务路由给小模型省钱

**答**：
- 路由三依据：任务类型（格式转换/抽取用小模型，多步推理用大模型）、历史表现（同一子任务类别在评估集上的小模型通过率）、失败成本（重跑便宜的可以冒险）。
- 级联模式：小模型先跑，校验器（规则或嵌入相似度）判定置信度不足再升级大模型——省下的是「大多数简单任务」的钱。
- 校验器误判是主要风险：小模型产出「看起来对」的错误内容会漏过校验，高危任务白名单强制大模型。
- 追问钩子：路由本身用什么做？——规则优先（便宜且稳定），规则覆盖不了的用轻量分类器，别用大模型做路由（成本倒挂）。

```ts
const TIER = { extract: 'small', format: 'small', plan: 'large', review: 'large' };
async function dispatch(task) {
  if (task.risk === 'high') return runWith(task, 'large');      // 高危直通大模型
  const tier = TIER[task.kind] ?? 'small';
  const out = await runWith(task, tier);
  if (tier === 'small' && (await verifier.check(out)).ok) return out;
  return tier === 'small' ? runWith(task, 'large') : out;       // 级联升级
}
```

