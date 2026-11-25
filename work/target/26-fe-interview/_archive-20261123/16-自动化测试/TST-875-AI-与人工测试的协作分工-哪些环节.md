---
title: [TST-875] AI 与人工测试的协作分工：哪些环节坚决不交给 AI？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-875：AI 与人工测试的协作分工：哪些环节坚决不交给 AI？
**答**：
- 结论：AI 擅长「量大、模式化、可验证」的活（生成样板用例、归因、自愈），人负责「需要判断、同理心、责任」的活（测试策略、探索性、发布决策）。
- 交给 AI：重复用例生成、失败聚类归因、定位器自愈、数据造数、快照初判。
- 留给人：测试策略与优先级、业务价值判断、探索性测试、安全/合规红线判定、发布 go/no-go。
- 原则：AI 产出必须可验证 + 人可追责；凡是需要「为结果负责」的决策，责任主体必须是人。
- 追问钩子：AI 自愈了一个定位器但没有记录，半年后用例跑偏了没人知道——这暴露了协作中哪个缺失？

```javascript
// 协作分工矩阵
const division = {
  aiOwns: ['样板用例生成', '失败聚类', '定位器自愈', '造数', '快照初判'],
  humanOwns: ['测试策略', '价值判断', '探索性测试', '合规红线', '发布决策'],
  principle: 'AI 产出可验证、人可追责；决策责任不外包',
};
function shouldDelegate(task) {
  return division.aiOwns.some(t => task.includes(t));
}
console.log(shouldDelegate('失败聚类'), shouldDelegate('发布决策')); // true false
```
