---
title: [AIC-058] 存量 JS 项目用 AI 批量补 TypeScript 类型的策略是什么？any 满天飞怎么办？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-058：存量 JS 项目用 AI 批量补 TypeScript 类型的策略是什么？any 满天飞怎么办？
**答**：
- 分层策略：先「数据模型层」（API 响应、store 结构、公共 props）后「边角函数」——模型类型是类型系统的地基，从使用频率最高的接口对象开始。
- 事实源原则：类型从真实数据推导——让 AI 读接口返回的 JSON 样例/后端 proto/数据库 schema 来定类型，而不是看变量名猜。
- any 治理：把 any→unknown + 类型收窄作为迁移步骤而不是一步到位猜类型；lint 用 `no-explicit-any` 渐进开启（warn→error 按目录灰度）。
- 批量推进：改一个文件 → `tsc --noEmit` 增量 → 通过才提交；AI 产出里新增的 `as` 断言要重点审查（它是「骗编译器」的捷径）。
- 追问钩子：评估迁移收益看「类型错误拦截数」——迁移后 tsc 抓到过多少真实 bug，这是向上汇报的弹药。

```javascript
// 从 JSON 样例推导 TS 类型（喂给 AI 的事实源）
function jsonToTSSchema(sample, name = 'T') {
  const t = (v) => {
    if (v === null) return 'null';
    if (Array.isArray(v)) return v.length ? `Array<${t(v[0])}>` : 'unknown[]';
    if (typeof v === 'object') {
      return `{ ${Object.entries(v).map(([k, val]) => `${k}: ${t(val)}`).join('; ')} }`;
    }
    return typeof v;
  };
  return `interface ${name} ${t(sample)}`;
}
```
