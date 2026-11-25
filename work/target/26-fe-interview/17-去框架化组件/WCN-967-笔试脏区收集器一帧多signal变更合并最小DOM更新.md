---
title: [WCN-967] 手写脏区收集器：把一帧内多个 signal 变更合并为最小 DOM 更新集合
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-967：手写脏区收集器：把一帧内多个 signal 变更合并为最小 DOM 更新集合

**题目**：实现 `createDirtyCollector(apply)`，返回 `{ mark(signalName, part), flush() }`。要求：① mark 记录「signal 名 → 需要更新的 DOM part 集合」（同一 signal 多次 mark 的 part 去重）；② flush 把本帧所有脏 part 合并成一个数组，去重后一次性调用 `apply(parts)`，然后清空；③ part 形如 `'#id.prop'` 字符串，按字典序排序输出保证稳定；④ flush 在无脏数据时返回空数组且不调用 apply；⑤ 提供 `pending()` 返回当前脏 part 数组（排序后）但不清空。请自足实现并给出可运行示例。

**答**：

```javascript
function createDirtyCollector(apply) {
  const dirty = new Map(); // signal -> Set(parts)
  return {
    mark(signal, part) {
      if (!dirty.has(signal)) dirty.set(signal, new Set());
      dirty.get(signal).add(part);
    },
    pending() {
      const all = new Set();
      for (const parts of dirty.values()) for (const p of parts) all.add(p);
      return [...all].sort();
    },
    flush() {
      const parts = this.pending();
      if (!parts.length) return [];
      apply(parts);          // 一次性批量应用
      dirty.clear();
      return parts;
    },
  };
}
const applied = [];
const c = createDirtyCollector(parts => applied.push(parts));
c.mark('price', '#p1.text'); c.mark('price', '#p1.text'); // 去重
c.mark('stock', '#p2.text'); c.mark('price', '#p1.color');
console.log(c.pending()); // ['#p1.color','#p1.text','#p2.text']（排序）
console.log(c.flush());   // 同上，并调用 apply 一次
console.log(c.flush());   // []（无脏，不调用 apply）
console.log('apply 调用次数:', applied.length); // 1
```

**评分点**：
- mark 按 signal 分组并对同一 signal 的 part 去重。
- flush 合并所有脏 part、全局去重、字典序排序后一次性 apply。
- 无脏数据时不调用 apply 并返回空数组。
- pending 返回排序后的脏 part 且不清空状态。
- 示例可运行、输出正确。
