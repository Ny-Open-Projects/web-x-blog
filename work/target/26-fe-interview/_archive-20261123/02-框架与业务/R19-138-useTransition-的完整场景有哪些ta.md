---
title: [R19-138] useTransition 的完整场景有哪些？tab 切换、搜索、列表过滤分别怎么用？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-138：useTransition 的完整场景有哪些？tab 切换、搜索、列表过滤分别怎么用？
**答**：
- 统一心法：把"高优先级反馈"（输入、tab 高亮）和"低优先级渲染"（重列表）拆开，后者包进 `startTransition`。
- 场景一 tab 切换：立即高亮新 tab，慢面板降级渲染，中间用 isPending 显示骨架。
- 场景二搜索：输入框保持受控即时回显，结果列表用 transition 后的值渲染。
- 场景三列表过滤：上千行筛选不再卡输入，配合 useMemo 让过滤本身也可中断。
- isPending 必须用于 UI 反馈，否则用户感知不到"正在算"。

```jsx
// ConcurrentScenes.jsx —— useTransition 三大场景
import { useTransition, useState, useMemo } from 'react';

function filterItems(items, keyword) {
  if (!keyword) return items;
  return items.filter(i => i.name.toLowerCase().includes(keyword.toLowerCase()));
}

// 场景一：tab 切换 —— 高亮立即响应，慢面板降级
export function TabSwitcher({ tabs }) {
  const [active, setActive] = useState(0);
  const [isPending, startTransition] = useTransition();

  return (
    <div>
      <div role="tablist">
        {tabs.map((tab, i) => (
          <button
            key={tab.id}
            role="tab"
            aria-selected={active === i}
            style={{ fontWeight: active === i ? 'bold' : 'normal' }}
            onClick={() => {
              setActive(i); // 高优先级：立即更新
              startTransition(() => {
                // 若面板状态独立管理，可在此低优先级更新
              });
            }}
          >
            {tab.label}
            {active === i && isPending && <span> loading...</span>}
          </button>
        ))}
      </div>
      <div style={{ opacity: isPending ? 0.5 : 1 }}>{tabs[active].content}</div>
    </div>
  );
}

// 场景二 + 三：搜索框即时回显，结果列表低优先级过滤
export function SearchList({ items }) {
  const [input, setInput] = useState('');
  const [query, setQuery] = useState('');
  const [isPending, startTransition] = useTransition();

  const filtered = useMemo(() => filterItems(items, query), [items, query]);

  return (
    <div>
      <input
        value={input} // 高优先级 state：打字零延迟
        onChange={e => {
          setInput(e.target.value);
          startTransition(() => setQuery(e.target.value)); // 低优先级：重列表
        }}
      />
      {isPending && <p>筛选中...</p>}
      <ul style={{ opacity: isPending ? 0.6 : 1 }}>
        {filtered.map(item => <li key={item.id}>{item.name}</li>)}
      </ul>
    </div>
  );
}
```
