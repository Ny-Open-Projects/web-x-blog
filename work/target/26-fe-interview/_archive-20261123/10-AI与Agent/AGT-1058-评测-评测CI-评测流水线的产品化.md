---
title: [1058] 评测流水线怎么做成团队基础设施
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 评测, 基建]
type: 面试题
---

## 1058：评测流水线怎么做成团队基础设施

**答**：
- 产品化标志：任何人「一条命令跑评测、一份报告看结论、一个门禁挡回归」——CLI（run + compare）、报告站（历史趋势、badcase 浏览）、CI 门禁三件套。
- 报告站的核心功能：版本间对比（指标表 + 每条 badcase 的 diff 视图）、指标时间轴（看漂移）、归因看板（失败分类占比）。
- 所有权与治理：评测体系有 owner（轮值）、评测集变更走 PR、门禁规则变更需评审——没有治理的评测基建三个月就腐烂。
- 追问钩子：怎么推广让团队真用？——把它嵌入既有流程（MR 必过门禁）而不是「倡导使用」；报告自动生成不让人写；跑分成本控制在 5 分钟内。

```bash
# CLI 三件套
evals run --set core --gate        # 跑核心集并卡门禁
evals compare v2.2 v2.3            # 版本对比报告
evals report --since 2026-11-01    # 趋势与 badcase 浏览
```

```ts
// CI 集成：MR 触发
on: pull_request: paths: ['prompts/**', 'agents/**']
steps: [ checkout, evals.run({ set: 'core', gate: true }), evals.comment(diff) ]
```
