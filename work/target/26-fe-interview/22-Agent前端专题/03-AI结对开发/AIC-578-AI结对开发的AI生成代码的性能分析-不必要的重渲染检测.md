---
title: [AIC-578] AI 生成代码的不必要重渲染检测
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-578：AI 代码的重渲染检测

**答**:
- AI 生成 React 代码的重渲染问题：1) **不必要的 re-render**（AI 生成的组件没有 memo/useMemo/useCallback——父组件 re-render 时子组件全部 re-render；2) **useCallback 缺失**（传递给子组件的函数引用不稳定——每渲染新建函数引用 → 子组件 memo 失效 RBL-682）；3) **state 提升**（AI 把 state 放在过高层级——多个无关组件 re-render（state 应该放最小共用父级）；4) **大列表无虚拟化**（1000 条列表全部渲染——AI 不知道要虚拟化 RBL-579）。
- AI 重渲染的检测：1) **静态分析**（组件中使用 state 但没有 memo/useMemo → warn；传递函数 props 但没有 useCallback → warn；2) **运行时检测**（React DevTools Profiler——re-render 次数统计；3) **AI 的修复**：AI 检测到重渲染问题 → 自动添加 memo/useCallback/useMemo（AI 修复自己生成的问题——闭环 RBL-566）。
- 追问钩子：为什么「AI 生成的 React 代码」比「人写的」更容易有不必要的 re-render？——AI 生成 = "一次性输出完整组件"（没有逐步优化的过程——人在写代码时会逐步意识到性能问题并优化；AI 一次性生成不做性能考虑）；「AI 的性能盲区」= LLM 的训练数据中"好代码"与"能运行的代码"混合（AI 倾向生成"能运行的"而非"最优的"——性能优化需要额外的 prompt RBL-506 的性能维度）；解法：性能 lint（RBL-566 规则）+ AI 自修复（RBL-566 闭环）+ 人审性能（RBL-532 检查点）。

```tsx
// AI 生成的性能问题检测
interface RenderIssue { component: string; issue: string; fix: string; }
function detectRenderIssues(component: { name: string; hasMemo: boolean; hasUseCallback: boolean;
  props: { name: string; type: 'fn'|'obj'|'primitive' }[]; childCount: number }) {
  const issues: RenderIssue[] = [];
  if (!component.hasMemo && component.childCount > 3)
    issues.push({ component: component.name, issue: 'no-memo',
      fix: '添加 React.memo 包裹' });
  if (!component.hasUseCallback && component.props.some(p => p.type === 'fn'))
    issues.push({ component: component.name, issue: 'no-usecallback',
      fix: '函数 props 用 useCallback 包裹' });
  if (component.props.some(p => p.type === 'obj' && !component.hasUseCallback))
    issues.push({ component: component.name, issue: 'unstable-obj-props',
      fix: '对象 props 用 useMemo 包裹' });
  return issues;
}
// AI 自修复
const issues = detectRenderIssues({ name: 'ProductList', hasMemo: false,
  hasUseCallback: false, props: [{ name: 'onClick', type: 'fn' }],
  childCount: 10 });
// → AI 自动修复：包裹 memo + useCallback
```
