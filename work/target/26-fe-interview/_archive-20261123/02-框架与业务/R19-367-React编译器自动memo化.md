---
title: [R19-367] React Compiler：自动 memo 化的原理与边界
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 编译器]
type: 面试题
---

## R19-367：React Compiler：自动 memo 化的原理与边界

**答**：
- React Compiler（原 Forget）：编译期静态分析组件/hook——自动插入 useMemo/useCallback/memo 等价物（内部低级表示），消除手动 memo 心智
- 依赖判定：编译器分析「读过的变量集合」自动生成依赖数组；对 mutation（改 props 对象）生成警告——「破坏可缓存性」的代码会被降级为不优化
- 覆盖边界：能分析组件作用域内的数据流；外部突变（第三方库改对象）、运行时 monkey-patch 无法追踪——这类代码手动标注/改造
- 与现有 memo 的关系：手写 useMemo 仍生效（编译器尊重已有优化）；重复优化无收益但无害——迁移期可共存
- 收益度量：交互前后的渲染次数对比（React Profiler）——「输入打字不再触发整列表重渲」的量化；编译产物体积增加（每组件多 memo 代码）要评估

```jsx
// 编译前(手写优化)
const rows = useMemo(() => data.filter(f), [data, f]);
// 编译后(自动): 编译器注入等价缓存, 依赖自动推导
// 开启: babel-plugin-react-compiler, ESLint 插件检查可优化性
```
