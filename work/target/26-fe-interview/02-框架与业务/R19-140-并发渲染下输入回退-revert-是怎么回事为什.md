---
title: [R19-140] 并发渲染下输入"回退"（revert）是怎么回事？为什么输入框有时会"倒退"？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-140：并发渲染下输入"回退"（revert）是怎么回事？为什么输入框有时会"倒退"？
**答**：
- transition 可被中断、可被丢弃：如果高优先级更新插队并重新渲染，被中断的 transition 不会"完成一半"，而是整体放弃。
- 错误模式：把输入框 value 绑到了**低优先级 state** 上，打字很快时 transition 一直被打断，value 显示的是被丢弃那轮的值，看起来像"回退"。
- 正确模式：输入用高优先级 state 即时回显；低优先级 state 只喂给重计算部分（上一题的双 state 模式）。
- 另一种"回退"是自动批处理下读快照：setState 后立即读 state 是旧值——这是快照语义不是 bug，需要最新值就用函数式更新或 ref。

```jsx
// RevertDemo.jsx —— 并发下的输入回退：错误写法 vs 正确写法
import { useState, useTransition, useDeferredValue } from 'react';

// 错误写法：value 绑在 transition 里的 state 上 —— 快速打字会"倒退"
function BadInput() {
  const [value, setValue] = useState('');
  const [, startTransition] = useTransition();
  return (
    <input
      value={value}
      onChange={e => {
        startTransition(() => setValue(e.target.value)); // value 更新可被丢弃
      }}
    />
  );
}

// 正确写法：双 state，显示与计算分离
function GoodInput({ items }) {
  const [text, setText] = useState('');        // 高优先级：显示层
  const [query, setQuery] = useState('');      // 低优先级：计算层
  const [isPending, startTransition] = useTransition();
  const deferredQuery = useDeferredValue(query);

  const filtered = items.filter(i =>
    i.name.toLowerCase().includes(deferredQuery.toLowerCase())
  );

  return (
    <>
      <input
        value={text} // 永远即时回显，绝不回退
        onChange={e => {
          setText(e.target.value);
          startTransition(() => setQuery(e.target.value));
        }}
      />
      {isPending && <span>计算中...</span>}
      <ul>{filtered.map(i => <li key={i.id}>{i.name}</li>)}</ul>
    </>
  );
}

// 记忆点：transition 是"尽力而为"的调度建议，不是"保证执行"的承诺
// 任何会被用户直接看到的反馈，都不能放进 transition
```
