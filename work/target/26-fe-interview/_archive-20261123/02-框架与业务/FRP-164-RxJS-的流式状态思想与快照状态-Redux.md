---
title: [FRP-164] RxJS 的"流式状态"思想与"快照状态"（Redux/useState）的本质差异是什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-164：RxJS 的"流式状态"思想与"快照状态"（Redux/useState）的本质差异是什么？

**答**：
- 快照状态：状态是**某个时刻的值**，更新即整体替换，订阅者拿"当前快照"；适合表单、CRUD、UI 配置。
- 流式状态：状态是**随时间推移的事件序列**（Observable），订阅者拿到的是"时间上的变化过程"，可以用算子（debounceTime/distinctUntilChanged/switchMap）对"变化本身"编程。
- 流式的杀手锏是**取消与竞态的原生表达**：`switchMap` 自动取消上一次未完成请求——快照状态里需要手写 AbortController/序号比对。
- 前端实践的折中：连续事件流（输入/滚动/拖拽）用 RxJS 组合后"落"成快照状态给 React/Vue 消费——两层各取所长。

```javascript
// 简化实现，帮助理解流式状态对竞态的表达力
// —— 快照状态方案：搜索要手动处理竞态 ——
function useSearchSnapshot() {
  const [results, setResults] = useState([]);
  const seqRef = useRef(0);
  const timerRef = useRef(null);
  function onQuery(q) {
    clearTimeout(timerRef.current);                       // 手写 debounce
    timerRef.current = setTimeout(async () => {
      const seq = ++seqRef.current;                       // 手写序号防乱序
      const r = await api(q);
      if (seq === seqRef.current) setResults(r);          // 手写过期丢弃
    }, 300);
  }
  return { results, onQuery };  // 三个手动机制：防抖、序号、条件 setState
}

// —— 流式状态方案：同样的逻辑用算子组合 ——
function searchStream() {
  return fromEvent(inputEl, 'input').pipe(
    map(e => e.target.value),
    distinctUntilChanged(),          // 相同输入不请求
    debounceTime(300),               // 防抖
    switchMap(q => from(api(q))),    // 关键：新请求到来自动取消上一次订阅（竞态消失）
    catchError(() => EMPTY)
  );
}
searchStream().subscribe(setResults);
// switchMap 语义 = "只要最新的" —— 快照方案里的 seq/abort 全部被算子替代

// —— 折中落地：流落快照 ——
function useObservable(observable$) {
  const [value, setValue] = useState(null);
  useEffect(() => {
    const sub = observable$.subscribe(setValue);  // 流式内部
    return () => sub.unsubscribe();               // 快照消费（React 友好）
  }, []);
  return value;   // 组件只关心最新值，流的复杂性被封装在 observable$ 构造处
}
```
