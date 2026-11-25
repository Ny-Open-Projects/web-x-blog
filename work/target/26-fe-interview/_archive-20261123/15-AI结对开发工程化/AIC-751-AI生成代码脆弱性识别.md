---
title: [AIC-751] 如何识别 AI 生成代码的脆弱性（边界与异常路径覆盖）
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-751：如何识别 AI 生成代码的脆弱性（边界与异常路径覆盖）

**答**：
- 结论先行：脆弱性 = 代码在 happy path 正确但边界/异常路径崩溃；AI 尤其容易「只写主流程」，识别靠「边界清单驱动审查」——把空值、超限、并发、网络失败等边界逐项代入验证。
- 常见脆弱点：1) 空数组/null 未处理；2) 数值溢出/精度；3) 异步竞态（重复点击、并发请求）；4) 外部依赖失败无降级；5) 超长输入导致卡顿。
- 手法：让 AI 生成代码时同时输出「边界处理清单」，审查时对照清单逐条确认是否真的实现（而非只在注释里写「处理了」）。
- 追问钩子：为什么「注释说处理了」不等于真处理了？——AI 常在注释里声明边界但代码漏实现，必须以可执行代码或测试为准。

```javascript
// 边界清单驱动审查
const EDGE_CASES = ['null', 'empty', 'negative', 'huge', 'concurrent'];
function auditFragility(fn, cases) {
  return cases.map(c => {
    try { fn(c); return { case: c, ok: true }; }
    catch (e) { return { case: c, ok: false, error: e.message }; }
  });
}
const parseQty = v => v.trim().toUpperCase(); // 脆弱：v 为 null 时崩溃
console.log(auditFragility(parseQty, EDGE_CASES).filter(r => !r.ok).map(r => r.case));
// ['null', 'negative', ...] —— 暴露未防护的边界
```
