---
title: [OPT-087] useTransition 怎么在搜索页落地？和防抖的区别是什么？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-087：useTransition 怎么在搜索页落地？和防抖的区别是什么？

**答**：
- `useTransition` 把状态更新标记为**可中断的过渡更新**：输入保持同步响应（urgent），列表重算被让位给输入渲染，卡顿感直接消失，比防抖少 200ms+ 感知延迟。
- 典型组合：输入框 value 同步更新（urgent）→ 过渡态更新列表数据（`startTransition` 内 setData）→ 过渡期展示旧列表 + isPending 提示。
- 与防抖互补：防抖减少"更新次数"，useTransition 保证"每次更新不阻塞输入"；两者可以叠加（数据来自接口时仍要防抖减少请求）。
- 同场景的兄弟 API：`useDeferredValue(value)` 直接给值做延迟副本，列表组件改动更少。

```jsx
// 一一对应：搜索页 useTransition 落地（输入即时、列表过渡）
function SearchPage() {
  const [input, setInput] = useState('');       // urgent：输入框随时响应
  const [query, setQuery] = useState('');       // transition：列表用它
  const [isPending, startTransition] = useTransition();

  const handleChange = (e) => {
    const v = e.target.value;
    setInput(v);                                // 同步更新，打字零延迟
    startTransition(() => {
      setQuery(v);                              // 可中断：输入渲染优先，列表让位
      // 若列表数据来自接口，这里仍建议 debounce 后 fetch，避免请求风暴
    });
  };

  return (
    <>
      <input value={input} onChange={handleChange} />
      {/* 过渡期间保留旧列表 + 轻量提示，不显示全屏 loading */}
      <div className={isPending ? 'list pending' : 'list'}>
        <HugeList filter={query} />
      </div>
    </>
  );
}

// 等价简化：useDeferredValue 适合"只想延迟一个值"的场合
function DeferredVariant({ keyword }) {
  const deferredKeyword = useDeferredValue(keyword); // 内部自动过渡
  const isStale = keyword !== deferredKeyword;       // 过渡未完成时旧值仍在渲染
  return <HugeList filter={deferredKeyword} className={isStale ? 'stale' : ''} />;
}

// 收益量化：Profiler 录制连续输入，
// 修复前输入帧 200ms+（被列表重算阻塞），修复后输入帧 <16ms
```
