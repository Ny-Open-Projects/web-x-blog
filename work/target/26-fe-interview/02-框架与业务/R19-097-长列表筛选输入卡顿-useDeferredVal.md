---
title: [R19-097] 长列表筛选输入卡顿，useDeferredValue 怎么用？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-097：长列表筛选输入卡顿，useDeferredValue 怎么用？
**答**：
- 病因：输入框 onChange 触发的状态更新同步驱动了昂贵的列表过滤渲染，键盘响应被阻塞。
- useDeferredValue 让输入框保持高优先级（实时回显），列表消费的 deferred 值以低优先级渲染，可被中断。
- `keyword !== deferredKeyword` 可以判断列表是否处于过期状态，用来展示"计算中"提示。
- 与防抖的区别：防抖是延迟触发（等待期间什么都不显示），deferredValue 是立即用旧结果渲染、新结果就绪后替换。

```jsx
// SearchPage.tsx —— 输入即时响应，列表低优先级渲染
import { memo, useDeferredValue, useState } from 'react';

const ExpensiveList = memo(function ExpensiveList({ keyword }) {
  // 大数据量过滤 + 排序，模拟耗时渲染
  const result = filterAndSort(bigData, keyword);
  return result.map(item => <div key={item.id}>{item.title}</div>);
});

function SearchPage() {
  const [keyword, setKeyword] = useState('');
  // 输入框高优先级实时更新；列表拿到的 deferred 值低优先级渲染
  const deferredKeyword = useDeferredValue(keyword);
  const isStale = keyword !== deferredKeyword;   // 过期期间展示提示

  return (
    <>
      <input value={keyword} onChange={e => setKeyword(e.target.value)} />
      {isStale && <span>计算中...</span>}
      <ExpensiveList keyword={deferredKeyword} />
    </>
  );
}
```
