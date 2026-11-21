---
title: [AIC-138] AI 会加速技术债积累吗？「AI 时代的技术债」有哪些新形态？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-138：AI 会加速技术债积累吗？「AI 时代的技术债」有哪些新形态？
**答**:
- 会，且更快：产出速度翻倍而治理能力没变——code review、测试、文档更新跟不上产出速度，债务在缝隙里堆积。
- 新形态：① prompt 债——为绕过某个问题打的补丁 prompt 无人清理，约束互相矛盾 ② 规则债——规则文件堆积到互相冲突（AIC-006 的规则密度问题）③ 幻觉残留债——AI 编造的注释/命名被后续代码引用成「事实」④ 生成债——无人真正理解的生成代码被持续迭代（理解成本高于重写成本却没人重写）。
- 治理对策：债务预算制度——每个迭代保留 20% 时间做 AI 产出治理（清 prompt、并规则、删幻觉注释）；度量上把「无人认领的生成代码量」作为债指标。
- 结构性对策：AI 产出的高债区限制继续生成（先还债再开发），与人类技术债的处理逻辑一致。
- 追问钩子：能指出「AI 不制造新债类，而是放大既有债的积累速度」并给出治理杠杆，是架构师视角的答案。

```javascript
// 技术债看板的 AI 特有指标
function aiDebtMetrics(repo) {
  return {
    promptDebt: countPatchPrompts(repo.prompts),          // 补丁摞补丁的模板数
    ruleConflicts: detectRuleConflicts(repo.rules),        // 规则互斥数
    orphanGenCode: linesWithoutOwner(repo.aiTracedFiles),  // 无认领生成代码
    budget: '每迭代 20% 时间用于 AI 债治理',
  };
}
```
