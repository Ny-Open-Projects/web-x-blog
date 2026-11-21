---
title: [DP-073] 自定义 Hook 为什么是"逻辑复用模式"？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-073：自定义 Hook 为什么是"逻辑复用模式"？
**答**：
- 自定义 Hook = 把"状态 + 副作用 + 派生逻辑"封装成可复用单元，调用方拿到数据与操作函数——复用的是逻辑而非组件结构。
- 与 HOC 对比：无包装层级（调试干净）、无 props 名冲突、按需取用（HOC 是整包注入）。
- 与 Mixin 对比：Hook 返回值显式列出（来源清晰），Mixin 是隐式合并属性（来源不可见，见 DP-081）。
- 设计要点：返回 `[值, 操作]` 或对象、内部可用其他 Hook、副作用成对清理。

```jsx
// 通用逻辑复用：useFetch —— 请求状态机（idle/loading/success/error 即状态模式）
function useFetch(url) {
  const [state, setState] = React.useState({ status: 'idle', data: null, error: null });
  const run = React.useCallback(async (abort = new AbortController()) => {
    setState({ status: 'loading', data: null, error: null });
    try {
      const res = await fetch(url, { signal: abort.signal });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      setState({ status: 'success', data, error: null });
    } catch (e) {
      if (e.name !== 'AbortError') setState({ status: 'error', data: null, error: e });
    }
  }, [url]);
  React.useEffect(() => {                          // url 变化自动重取（观察者）
    const ac = new AbortController();
    run(ac);
    return () => ac.abort();                       // 副作用成对清理
  }, [url]);
  return { ...state, refetch: () => run() };       // 显式返回契约
}
// 复用点1：组件A
function OrderList() {
  const { status, data, error } = useFetch('/api/orders');
  if (status === 'loading') return <Spin />;
  if (status === 'error') return <Error msg={error.message} />;
  return <ul>{data.map((o) => <li key={o.id}>{o.no}</li>)}</ul>;
}
// 复用点2：组件B 用同一个 Hook 取完全不同的资源 —— 逻辑复用而非组件复用
// const { data } = useFetch('/api/users');
// 对比 HOC：没有 withFetch(OrderList) 的包装层，React DevTools 更干净
```
