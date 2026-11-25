---
title: [1023] Agent 的合规审计（等保/数据出境/行业规范）怎么映射到工程实现
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 合规]
type: 面试题
---

## 1023：Agent 的合规审计（等保/数据出境/行业规范）怎么映射到工程实现

**答**：
- 合规要求翻译成工程动作：日志留存时限（如 180 天）→ 审计存储策略；数据出境评估 → 模型 API 区域选择与数据驻留承诺；内容安全 → 输出审查规则库与备案。
- 审计留痕「三可」：可追溯（全链路 trace）、可证明（哈希链/时间戳，防抵赖）、可导出（监管检查时能按主体/时间导出完整记录）。
- 数据分级映射：检索索引按密级打标，不同级数据走不同的模型 API（高密级走本地部署模型），这是「数据不出域」的落地方式。
- 追问钩子：合规审查最先问什么？——「数据流向图」：哪类数据进、存哪、出哪、给谁看；先把这张图画清楚，缺的才是要补的工程。

```ts
const compliance = {
  retention: { audit: 180, trace: 90 },                 // 留存时限
  dataResidency: { pii: 'cn-local-model', public: 'cloud-api' }, // 分级路由
  export: (subject, range) => auditStore.exportBySubject(subject, range),
};
function routeModel(dataClass) {
  return compliance.dataResidency[dataClass];           // 高密级不出域
}
```
