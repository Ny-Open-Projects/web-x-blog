---
title: [HW-106] 手写带拖拽排序的受控列表——key 稳定性、受控数据流与拖拽落点计算
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-106：手写带拖拽排序的受控列表——key 稳定性、受控数据流与拖拽落点计算
**答**：拖拽排序三要点：① **key 必须稳定且唯一**（用数据 id，绝不用 index——index 在重排后会让 React 复用错误节点的输入状态）；② 受控数据流——拖拽只更新源数组顺序（splice + 不可变更新 HW-099），DOM 顺序交给 React；③ 落点计算——用 dragover 的 clientY 对半比较目标项中线，决定 before/after。

```jsx
import { useState } from 'react';

function SortableList({ items, onReorder }) {
  const [dragId, setDragId] = useState(null);
  const [overId, setOverId] = useState(null);

  function onDrop(e, targetId) {
    e.preventDefault();
    const target = e.currentTarget.getBoundingClientRect();
    const isBefore = e.clientY < target.top + target.height / 2;   // 上半：插前面
    const from = items.findIndex((x) => x.id === dragId);
    let to = items.findIndex((x) => x.id === targetId);
    if (from < to && !isBefore) to -= 1;                            // 先摘后插的偏移修正
    if (from > to && isBefore) to += 1;
    const next = [...items];
    const [moved] = next.splice(from, 1);
    next.splice(to, isBefore && from < to ? to : to, moved);        // 插入
    onReorder(next);
    setDragId(null); setOverId(null);
  }
  return (
    <ul>
      {items.map((item) => (
        <li key={item.id}                                  // 稳定 key：数据 id
            draggable
            onDragStart={() => setDragId(item.id)}
            onDragOver={(e) => { e.preventDefault(); setOverId(item.id); }}
            onDrop={(e) => onDrop(e, item.id)}
            style={{ opacity: dragId === item.id ? 0.4 : 1,
                     outline: overId === item.id ? '2px dashed #09f' : 'none' }}>
          {item.name}
        </li>
      ))}
    </ul>
  );
}
// 反例：key={index} —— 拖拽后 React 按 index 复用节点，输入框内容/状态错位
// 落点修正：splice 摘除后索引偏移（from<to 时 to-1）是最容易写错的地方
```

**评分点**：
- 稳定 key（数据 id）并说清 index key 在重排场景的错误行为。
- 落点半线判定（clientY vs 目标中线）与 splice 偏移修正正确。
- 受控数据流：onReorder 回调更新父数据，DOM 顺序由 React 管理。
- 拖拽视觉反馈（透明度 + 插入指示线）。
