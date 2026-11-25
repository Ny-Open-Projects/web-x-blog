---
title: [WCN-559] Svelte 5 的「运行时信号 + 编译期粒度」混合：编译器如何决定何时用 signal、何时直写 DOM？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-559：Svelte 5 的「运行时信号 + 编译期粒度」混合：编译器如何决定何时用 signal、何时直写 DOM？

**答**：
- 结论：编译器分析表达式是否「可静态定向更新」——简单的单变量绑定生成直写 DOM，复杂的派生/多处引用生成信号。
- 直写 DOM（如 textContent = count）最省，但只适合表达式单一、更新点明确的情况。
- 需要跨节点共享、派生计算、条件依赖时，编译成 signal + effect 更灵活。
- 追问：为何不全部用信号？（答：信号有订阅/调度开销，简单绑定直写更快）

```javascript
function chooseStrategy(expr) {
  const refs = collectRefs(expr);                       // 引用的响应式变量
  if (refs.length === 1 && expr.kind === 'simpleMember' && !expr.needsDerive)
    return { mode: 'direct-dom', code: `el.textContent = ${expr.code}` };
  return { mode: 'signal-effect', code: `effect(() => el.textContent = ${expr.code})` };
}
// {count}           -> direct-dom
// {a + b} / 多处引用 -> signal-effect

// 简单绑定直写 DOM，复杂派生走信号，兼顾性能与灵活
if (chooseStrategy('{count}').mode === 'direct-dom') genDirect();
```
