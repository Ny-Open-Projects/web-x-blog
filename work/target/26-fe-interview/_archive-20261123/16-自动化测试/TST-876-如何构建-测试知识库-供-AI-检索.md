---
title: [TST-876] 如何构建「测试知识库」供 AI 检索（历史缺陷/用例模式/领域知识）？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-876：如何构建「测试知识库」供 AI 检索（历史缺陷/用例模式/领域知识）？
**答**：
- 结论：测试知识库要把「隐性经验」显性化、结构化——把历史缺陷、用例模式、领域术语按统一 schema 入库，并随项目演进持续更新。
- 内容组织：缺陷库（现象→根因→ Catapult 测试用例）、用例模式库（参数化/边界表模板）、领域术语表。
- 结构化：每条知识带标签（模块/类型/严重度）与向量，支持 RAG 混合检索（呼应 TST-863）。
- 保鲜机制：用例评审/事故复盘产出的知识自动入库，定期清理过时条目，避免知识库变成垃圾场。
- 追问钩子：知识库里同时存在「旧方案的缺陷」和「新方案已修复」的记录，AI 检索到旧的会误导，如何处理？

```javascript
// 测试知识库条目结构
const kbEntry = {
  id: 'BUG-2025-013',
  type: 'defect', module: 'payment',
  symptom: '优惠券叠加后金额错误',
  rootCause: '折扣计算顺序错误',
  testPattern: '边界表：0/单券/多券/负数',
  tags: ['金额', '回归', 'P1'],
  deprecated: false, // 新方案修复后标记废弃
  updatedAt: '2026-10-01',
};
// 检索时过滤 deprecated:true 的过时条目，避免误导 AI
function retrieveKB(entries) { return entries.filter(e => !e.deprecated); }
console.log(retrieveKB([kbEntry]).length); // 1
```
