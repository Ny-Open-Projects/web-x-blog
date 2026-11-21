---
title: [WCN-306] React Compiler 的失效场景与团队约束？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-306：React Compiler 的失效场景与团队约束？
**答**：
- 失效场景：违反纯函数（渲染期写外部状态）/hooks 规则/条件 hooks——memo 被跳过（静默回退普通渲染）。
- 兜底：eslint-plugin-react-compiler 编译规则检查进 CI。
- 不可优化组件显式标记（"use no memo"）——边界声明。
- 收益度量：React Profiler 中重渲染次数 before/after 对比（ Compiler on/off 双跑）。

```javascript
// 显式逃逸
function Legacy({ data }) {
  \"use no memo\";      // 该组件跳过 Compiler
  return <Chart data={data} />;
}
r
```
