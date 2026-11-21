---
title: [R19-028] useTransition 解决什么问题？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-028：useTransition 解决什么问题？
**答**：
- 把某些 state 更新标记为"过渡更新"（低优先级），让输入等高优先级更新可以打断它。
- 典型场景：搜索框输入实时响应，但根据输入过滤大列表很重，希望列表更新可中断、不卡输入。
- isPending 表示过渡更新还没渲染完，可以用来展示加载态。
- startTransition 里必须同步调用 setState，且该 Hook 只能在组件内部使用（模块级用独立的 startTransition 函数）。

```jsx
function SearchBox() {
  const [query, setQuery] = useState('');
  const [list, setList] = useState([]);
  const [isPending, startTransition] = useTransition();

  function handleChange(e) {
    // 高优先级：输入框立即更新，打字不卡
    setQuery(e.target.value);
    // 低优先级：重过滤可被下一次输入打断
    startTransition(() => {
      setList(filterHugeList(e.target.value));
    });
  }

  return (
    <>
      <input value={query} onChange={handleChange} />
      {isPending ? <p>过滤中...</p> : <ul>{list.map((i) => <li key={i}>{i}</li>)}</ul>}
    </>
  );
}
```
