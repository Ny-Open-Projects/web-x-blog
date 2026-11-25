---
title: [AGT-338] 代码执行 Agent——数据分析类任务的 Agent 怎么做？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-338：数据分析 Agent（写代码跑数据出结论）怎么设计？

**答**:
- 执行循环：理解需求→生成分析计划（用哪些数据/什么方法）→写代码（沙箱执行 AGT-284）→检查结果（合理性校验：数量级/分布是否符合常识）→修正迭代→结论（数字全部来自代码输出，AGT-267）——"写码-执行-验证"循环是数据分析 Agent 的核心。
- 数据上下文：先给 schema/样例（不塞全量数据），Agent 用代码探索（df.head/describe）——大数据不进上下文，进沙箱；敏感数据脱敏或私有化沙箱。
- 结论严谨性：相关性≠因果的表述纪律（LLM 报告倾向过度归因——prompt 强制区分"相关"与"因果"，样本量/置信区间标注）；异常结果（如转化率 300%）触发怀疑而不是接受——数据分析 Agent 最危险的是"自信地给出错误统计"。
- 复现性：代码+数据版本+随机种子全留痕（AGT-289 审计），结论可一键复现——分析结论的可复现是团队信任的基础。

```javascript
async function dataAgent(question, dataset) {
  const plan = await llm(`分析计划`, { question, schema });
  for (let i = 0; i < 5; i++) {
    const code = await llm(`生成分析代码`, { plan, schema });
    const result = await sandbox.run(code, { data: dataset.ref });
    if (plausible(result))                       // 合理性校验
      return report(result, { citeCode: true,
        note: '区分相关与因果，标注样本量' });
    plan.refine(result);                         // 修正迭代
  }
  return '无法得到可靠结论';
}
```
