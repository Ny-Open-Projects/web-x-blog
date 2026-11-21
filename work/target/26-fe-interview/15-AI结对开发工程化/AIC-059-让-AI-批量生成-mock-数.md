---
title: [AIC-059] 让 AI 批量生成 mock 数据的规范是什么？为什么不能「随机糊一堆」？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-059：让 AI 批量生成 mock 数据的规范是什么？为什么不能「随机糊一堆」？
**答**：
- mock 要「像真的」才能暴露 bug：长度跨界的字符串、null 字段、空数组、时区奇怪的日期、超长中文文案——真实世界的脏数据才是前端崩溃主因。
- 规范：以类型定义为 schema 生成，每个字段标注「正常值 + 边界值」两套；固定 seed 保证可复现；敏感字段用假名（Fake Name Generator 类规则），禁止真实用户数据进 mock。
- 分层：基础 fixture（手写核心对象，稳定）+ AI 批量变体（从 fixture 变异生成边界场景），AI 负责枚举「脏数据清单」人负责确认。
- 用途匹配：E2E 用稳定 fixture，单测用边界变体，演示环境用「像真的」数据——不同场景不要共用一套。
- 追问钩子：把「脏数据清单」沉淀成团队资产，比 mock 本身更值钱（呼应 AIC-184 笔试题）。

```javascript
// 边界值变异规则表（AI 枚举、代码执行）
const mutators = {
  string: v => ['', ' '.repeat(2000), '<script>alert(1)</script>', 'emoji😀'.repeat(100), v],
  number: v => [0, -1, Number.MAX_SAFE_INTEGER, NaN, v],
  array: v => [[], v, Array(1000).fill(v[0] ?? null)],
  nullable: v => [null, undefined, v],
};
function edgeCases(fixture) {
  return Object.entries(fixture).flatMap(([k, v]) =>
    (mutators[Array.isArray(v) ? 'array' : typeof v] ?? mutators.nullable)(v).map(val => ({ ...fixture, [k]: val })));
}
```
