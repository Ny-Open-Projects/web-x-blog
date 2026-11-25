---
title: [AIC-089] 「意图与实现分离」在 AI 结对开发里指什么？为什么它是控制 AI 产出的关键设计？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-089：「意图与实现分离」在 AI 结对开发里指什么？为什么它是控制 AI 产出的关键设计？
**答**：
- 意图：业务想要什么（验收标准、行为约束）；实现：怎么达成（具体代码）。分离即「人负责意图，AI 负责实现，用可验证的契约连接」。
- 契约形式：测试用例、类型签名、接口文档、状态机转移表（AIC-072）——AI 的实现必须在契约内，契约外的 diff 一律不接受。
- 为什么关键：AI 最常见的问题不是「做不出」而是「做出别的」（夹带重构、自作主张的默认值）；契约把「像不像」的争论变成「过没过」的判定。
- 实践载体：任务模板里意图段写验收标准，产出后先跑契约验证（测试/类型检查）再人工看 diff——顺序不能反，先看代码会被实现细节带偏。
- 追问钩子：契约本身的生成也可以交给 AI（先让它起草测试），但契约的批准权永远在人——这是「意图主权」。

```javascript
// 意图契约：验收即卡尺
const contract = {
  behavior: [
    '输入空数组返回 []',
    '相同 id 的项后者覆盖前者',
    '请求失败时抛出 ApiError 且带 status',
  ],
  forbidden: ['不修改导出签名', '不引入新依赖'],
};
function validateAgainstContract(diff, testResults) {
  const contractTests = testResults.filter(t => t.from === 'contract');
  return contractTests.every(t => t.pass) && !diff.touches(['exports', 'package.json']);
}
```
