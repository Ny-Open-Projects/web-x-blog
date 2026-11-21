---
title: [OPT-138] 列表 diff 性能优化中 key 的正确姿势与分页合并策略是什么？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-138：列表 diff 性能优化中 key 的正确姿势与分页合并策略是什么？

**答**：
- key 三不要：不要用数组下标（插入/删除时后面全部错位 diff）、不要用随机数（每次渲染全量重建 DOM）、不要用会变化的字段。
- key 要稳定且唯一：业务 id 最优；复合 id `orderId-skuId` 次之。key 稳定 = 框架能命中节点复用，diff 从 O(n²) 退化问题回到 O(n)。
- 分页合并：加载下一页时用 `concat` 追加而不是"用新数组整体替换 state"，替换会让 diff 认为全部节点可能变化；追加时旧节点 key 不变，直接跳过。
- 在头部插入新数据的场景（信息流"最新"刷新），用倒序 key 设计或保留旧数据区间 key，避免下标漂移。

```javascript
// 一一对应：key 稳定性 + 分页 concat 合并的 diff 优化
// 反例：state = setState(newList) 整体替换 + key={index}
// 正例实现：
function mergePaged(oldItems, newItems, mode = 'append') {
  if (mode === 'append') {
    // 追加：旧元素引用原样保留，React diff 时同 key 节点直接复用
    return [...oldItems, ...newItems];
  }
  if (mode === 'prepend') {  // 信息流插入"更新的数据"到头部
    const oldIds = new Set(oldItems.map(i => i.id));
    const fresh = newItems.filter(i => !oldIds.has(i.id)); // 去重防 key 冲突
    return [...fresh, ...oldItems];  // 旧数据 key 不变，DOM 节点整体下移但不重建
  }
  return newItems; // 仅翻页替换模式才整体换
}

// 组件侧：key 用稳定业务 id
function Feed({ items }) {
  return (
    <ul>
      {items.map(item => (
        <li key={item.id}>           {/* id 稳定：插入删除不影响其他节点复用 */}
          <FeedCard item={item} />   {/* 配合 React.memo，item 引用不变则跳过 */}
        </li>
      ))}
    </ul>
  );
}
```
