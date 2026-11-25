---
title: [FRP-387] 笔试：手写 renderless 组件（跨框架逻辑内核 + 插槽协议）
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## FRP-387：笔试：手写 renderless 组件

**答**：实现一个 renderless 逻辑内核（组合下拉框 Combobox）：① `createCombobox({ items, filter })`：返回 { open, activeIndex, query, actions: { open/close/navigate/select } }——纯状态机（订阅通知）；② 键盘协议（↑↓ 移动/Enter 选择/Esc 关闭）在内核；③ aria 状态导出（expanded/activedescendant 的 id 计算）——框架层绑定的语义就绪；④ React 壳与 Vue 壳各 ~15 行消费；⑤ 边界：items 动态变化时 activeIndex 钳制。写出实现与两壳消费。

```javascript
export function createCombobox({ items: getItems, filter = (q, i) => i.label.includes(q) }) {
  let open = false, activeIndex = -1, query = '';
  const subs = new Set();
  const notify = () => subs.forEach((f) => f(snapshot()));
  const items = () => getItems().filter((i) => filter(query, i));

  const actions = {
    open() { open = true; activeIndex = items().length ? 0 : -1; notify(); },
    close() { open = false; activeIndex = -1; notify(); },
    navigate(dir) { if (!open) return actions.open();
      const n = items().length;
      activeIndex = ((activeIndex + dir) % n + n) % n;   // 循环钳制
      notify(); },
    select() { const item = items()[activeIndex];
      if (item) { query = item.label; actions.close(); onSelect?.(item); } },
    setQuery(q) { query = q; activeIndex = items().length ? 0 : -1; notify(); },
    onKey(e) {
      const map = { ArrowDown: () => actions.navigate(1), ArrowUp: () => actions.navigate(-1),
        Enter: () => actions.select(), Escape: () => actions.close() };
      map[e.key]?.(); e.preventDefault?.();
    },
  };
  function snapshot() {
    return { open, activeIndex, query, aria: { expanded: open, activeId: `opt-${activeIndex}` } };
  }
  let onSelect;
  return { ...actions, items, sub(fn) { subs.add(fn); return () => subs.delete(fn); }, snapshot,
    onSelect(fn) { onSelect = fn; } };
}
// React 壳: const cb = useSyncExternalStoreKernel(createCombobox); input onKeyDown={cb.onKey} aria-expanded={cb.aria.expanded}
// Vue 壳:   customRef 绑定 snapshot; 同样消费 aria 状态
// aria 语义就绪 → 壳层零逻辑, 只渲染
```

**评分点**：
- 内核状态机（开合/导航/选择）与键盘协议内聚
- aria 状态导出（框架层绑定就绪，语义与实现分离）
- 循环钳制与动态 items 的 activeIndex 防越界
- 双壳各 ~15 行的「逻辑单源」验证
