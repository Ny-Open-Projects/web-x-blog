---
title: [AIC-336] 改一个公共 API 签名，如何让 AI 评估全链路影响？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-336：改一个公共 API 签名，如何让 AI 评估全链路影响？
**答**：
- 静态影响面：类型系统 + 调用图分析找出所有调用点，AI 补充动态调用（字符串引用/反射式调用）。
- 语义影响：AI 分析每个调用点的使用意图，判断「行为是否被改变」而非只看编译过不过。
- 分级输出：编译期可见的破坏 / 编译期不可见的语义变化（后者更危险）。
- 迁移建议：每类调用点给适配代码与分批迁移顺序。

```javascript
async function apiImpact(fn: Fn) {
  const callers = await allCallers(fn);           // 类型系统调用图
  const semantic = await Promise.all(callers.map(c => intent(c))); // 每处使用意图
  return {
    compileBreak: callers.filter(needsTypeChange),
    silentChange: semantic.filter(s => s.dependentOnOldBehavior), // 最危险
    migrate: plan(callers, semantic),
  };
}
r
```
