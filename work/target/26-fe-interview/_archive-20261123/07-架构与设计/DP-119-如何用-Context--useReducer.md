---
title: [DP-119] 如何用 Context + useReducer 实现一个 mini 状态机？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-119：如何用 Context + useReducer 实现一个 mini 状态机？（高频）
**答**：
- 本质：Context（Provider 模式，DP-072）负责把状态与 dispatch 注入子树，useReducer 负责合法转移——合起来就是一个轻量"局部状态机"。
- 适用边界：中小型共享状态（主题、购物车、向导流程）；跨页共享或需要中间件时升级 Zustand/Redux（DP-084）。
- 性能要点：state 与 dispatch 分两个 Context，消费动作的组件不因状态变化重渲染。

```jsx
const StateCtx = createContext(null);
const DispatchCtx = createContext(null);
// 状态机：向导流程的合法转移集中在 reducer
function wizardReducer(state, action) {
  const next = { idle: { start: 'step1' }, step1: { next: 'step2', back: 'idle' },
                 step2: { next: 'confirm', back: 'step1' }, confirm: { submit: 'done' } }[state.phase];
  if (action.type === 'goto' && next?.[action.event] === undefined && action.event !== 'reset')
    throw new Error(`非法转移 ${state.phase} + ${action.event}`);
  if (action.type === 'reset') return { phase: 'idle', payload: null };
  return { phase: next[action.event], payload: action.payload ?? state.payload };
}
export function WizardProvider({ children }) {
  const [state, dispatch] = useReducer(wizardReducer, { phase: 'idle', payload: null });
  return (
    <DispatchCtx.Provider value={dispatch}>
      <StateCtx.Provider value={state}>{children}</StateCtx.Provider>
    </DispatchCtx.Provider>
  );
}
export const useWizard = () => useContext(StateCtx);       // 读状态
export const useWizardDispatch = () => useContext(DispatchCtx); // 只派发：状态变了不重渲染动作按钮
function WizardSteps() {
  const { phase } = useWizard();
  const dispatch = useWizardDispatch();
  return <button onClick={() => dispatch({ type: 'goto', event: 'start' })}>开始 {phase}</button>;
}
```
