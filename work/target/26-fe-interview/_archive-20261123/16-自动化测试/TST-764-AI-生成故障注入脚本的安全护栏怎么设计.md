---
title: [TST-764] AI 生成故障注入脚本的安全护栏怎么设计
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-764：AI 生成故障注入脚本的安全护栏怎么设计

**答**：
- 结论：AI 生成的注入脚本不可直接执行，必须过「静态白名单校验 + 沙箱预演 + 人工审批」三道护栏。
- 静态校验：禁止危险操作（删库、改生产配置、外联未知域名），只允许白名单 API 与资源范围。
- 沙箱预演在隔离环境跑一遍，对比爆炸半径是否符合声明；审批时展示「将影响什么」的可读摘要。
- 追问钩子：AI 生成了白名单内的操作但组合起来很危险，如何发现？

```javascript
// 注入脚本静态白名单校验
const ALLOWED = new Set(['delay', 'errorRate', 'dropDom']);
const DANGEROUS = /rm\s+-rf|DROP\s+TABLE|fetch\(|XMLHttpRequest/;
function vetScript(script, declaredOps) {
  if (DANGEROUS.test(script)) return { ok: false, why: '危险操作' };
  const ops = [...script.matchAll(/(delay|errorRate|dropDom|throw)/g)].map(m => m[1]);
  const unknown = ops.filter(o => !ALLOWED.has(o));
  if (unknown.length) return { ok: false, why: '未授权操作: ' + unknown.join(',') };
  return { ok: ops.every(o => declaredOps.includes(o)), why: '声明外操作' };
}
console.log(vetScript('inject.delay(500)', ['delay'])); // ok:true
```
