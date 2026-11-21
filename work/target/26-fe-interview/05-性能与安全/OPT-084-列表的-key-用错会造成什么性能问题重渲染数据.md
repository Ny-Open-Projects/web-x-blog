---
title: [OPT-084] 列表的 key 用错会造成什么性能问题？重渲染数据量怎么控制？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-084：列表的 key 用错会造成什么性能问题？重渲染数据量怎么控制？

**答**：
- key 的作用是 diff 时做身份对齐：用 index 做 key，删除/插入会导致后续所有元素"换皮"——组件状态错位 + 不必要的重渲染；用随机 key 更糟，等于每次全量重建。
- 性能上真正昂贵的不是 key 本身，而是"一次 commit 里 diff 的行数 × 每行复杂度"：万行列表全量重渲和虚拟列表只渲可视 20 行差 3 个数量级。
- 控制数据量三件套：**虚拟列表**（只渲可视区）、**行组件 memo + 稳定 props**（改一行只重渲一行）、**分页/无限滚动**减少首屏行数。
- key 取业务唯一 id；确无 id 时用内容哈希，最后才考虑 index（且仅限纯静态无增删列表）。

```jsx
// 一一对应：key 错误案例与"改一行只重渲一行"的列表实现
// 反例 1：index 作 key，插入头部时整列错位重渲
{rows.map((row, i) => <Row key={i} row={row} />)}

// 反例 2：随机 key，每次渲染全量卸载重建（连 state 都丢）
{rows.map((row) => <Row key={Math.random()} row={row} />)}

// 正解：稳定业务 id
{rows.map((row) => <Row key={row.id} row={row} />)}

// 行级 memo：props 浅比较，未变化的行直接跳过 reconcile
const Row = React.memo(function Row({ row, onSelect }) {
  return (
    <li onClick={() => onSelect(row.id)}>
      {row.name} - {row.price}
    </li>
  );
});

// 父组件： onSelect 用 useCallback 保稳定，否则 memo 形同虚设
function GoodsList({ rows }) {
  const handleSelect = useCallback((id) => emit('select', id), []); // 引用稳定
  return <ul>{rows.map((row) => <Row key={row.id} row={row} onSelect={handleSelect} />)}</ul>;
}

// 数据量验证：Profiler 里 diff 的行数应等于"被改的行数"，
// 若整列表都出现在一次 commit 里，先查 key 与 props 引用稳定性
```
