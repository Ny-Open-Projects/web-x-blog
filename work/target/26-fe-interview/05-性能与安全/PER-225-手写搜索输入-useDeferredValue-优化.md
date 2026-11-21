---
title: [PER-225] 笔试题：用 React 手写一个 INP 友好的商品搜索（输入即时、列表延迟、防抖兜底）
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-225：用 React 手写一个 INP 友好的商品搜索（输入即时、列表延迟、防抖兜底）

**题目**：实现一个商品搜索页组件：① 输入框实时受控更新（输入零延迟，保 INP）；② 商品列表用 useDeferredValue 延迟渲染，结果未就绪时展示半透明过渡态；③ 远程搜索用防抖 300ms + 请求竞态丢弃（只认最后一次）；④ 列表渲染超过 1000 条时虚拟化提示（可用简化虚拟滚动）。

**答**：三层策略：本地输入立即渲染（受控 value）；昂贵派生渲染交给 useDeferredValue（React 自动在低优先级渲染）；网络请求防抖 + 竞态丢弃。输入的 INP 由"不联动昂贵渲染"保证。

```jsx
import { useState, useDeferredValue, useEffect, useRef, memo } from 'react';

function ProductSearch({ products }) {
  const [query, setQuery] = useState('');
  const [remote, setRemote] = useState([]);
  const deferredQuery = useDeferredValue(query);
  const isStale = query !== deferredQuery;
  const seq = useRef(0);

  useEffect(() => {                                   // 防抖远程搜索 + 竞态丢弃
    if (!deferredQuery) { setRemote([]); return; }
    const mySeq = ++seq.current;
    const t = setTimeout(async () => {
      const rows = await fetch(`/api/search?q=${encodeURIComponent(deferredQuery)}`).then(r => r.json());
      if (seq.current === mySeq) setRemote(rows);     // 过期响应丢弃
    }, 300);
    return () => clearTimeout(t);
  }, [deferredQuery]);

  const localHits = deferredQuery ? products.filter(p => p.name.includes(deferredQuery)) : products;
  return (
    <>
      <input value={query} onChange={e => setQuery(e.target.value)}    {/* 紧急更新 */}
             aria-label="搜索商品" />
      <div style={{ opacity: isStale ? 0.5 : 1 }}>                     {/* 过渡态 */}
        {localHits.slice(0, 20).map(p => <Row key={p.id} item={p} />)}
        {remote.slice(0, 20).map(p => <Row key={'r' + p.id} item={p} />)}
        {localHits.length > 20 && <p>共 {localHits.length} 条，请输入更精确关键词或启用虚拟列表</p>}
      </div>
    </>
  );
}
const Row = memo(({ item }) => <div className="row">{item.name} ¥{item.price}</div>);
```

**评分点**：
- 输入受控不联动昂贵渲染，deferredQuery 驱动列表（INP 保住输入段）。
- 竞态丢弃实现正确（递增序号比对，只认最后一次请求）。
- 防抖放对对象：防"远程请求"而非防"输入渲染"（防输入会直接伤 INP）。
- 过渡态（opacity/stale 标记）提升感知；大量本地数据有虚拟化预案。
