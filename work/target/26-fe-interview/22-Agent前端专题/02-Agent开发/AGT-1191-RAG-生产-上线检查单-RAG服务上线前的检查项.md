---
title: [1191] RAG 服务上线前的检查单有哪些必过项
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 上线]
type: 面试题
---

## 1191：RAG 服务上线前的检查单有哪些必过项

**答**：
- 检查单六项：评估达标（核心集准确率/误拒率过红线）、权限正确（抽样验证 ACL 过滤）、降级可用（检索挂了/模型挂了的降级路径演练过）、可观测（分段埋点齐全、告警阈值设定）、溯源可用（引用可点击且指向正确版本）、回滚预案（索引别名回滚 + 配置回滚演练过）。
- 检查单执行方式：CI 自动跑机器可判项，人工确认项出 checklist 表单，全绿才放流量——检查单的价值在「机器可判比例」，全人工的检查单会被跳过。
- 灰度策略默认值：新 RAG 服务先内部用户（100 人）一周，再 5% 外部灰度，指标稳了再全量。
- 追问钩子：检查单里最常被漏的是哪项？——「降级可用」：大家测正常路径不测降级路径，而线上事故恰恰发生在降级时刻；把降级演练做成自动化用例进 CI。

```ts
const checklist = [
  { item: 'eval_pass', auto: () => coreEval.acc > 0.75 },
  { item: 'acl_correct', auto: () => aclProbe.passRate > 0.99 },
  { item: 'degrade_ready', auto: () => chaosSuite('retrieval_down').passed },
  { item: 'observability', auto: () => metrics.complete(['retrieve','rerank','gen']) },
  { item: 'citation_ok', auto: () => citationProbe.ok },
  { item: 'rollback_drilled', human: true },
];
async function goLiveGate() {
  const rs = await Promise.all(checklist.map(c => c.auto ? c.auto() : pending(c)));
  return rs.every(Boolean) ? canary() : blockPending(rs);
}
```

