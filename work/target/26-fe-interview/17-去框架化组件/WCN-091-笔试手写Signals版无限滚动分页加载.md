---
title: [WCN-091] 笔试：手写 Signals 版无限滚动分页（cursor 翻页 + 去重）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-091：笔试：手写 Signals 版无限滚动分页

**题目**：① `cursor` signal（下一页游标，null 表示无更多）；② `items` signal 累积列表；③ `loadMore()` 请求 `{ items, nextCursor }` 并合并（按 id 去重）；④ `loading` signal 防并发；⑤ IntersectionObserver 哨兵进入视口自动 loadMore；⑥ 返回 `destroy`。

**答**：

```javascript
import { createSignal, effect, untrack } from './mini.js';

export function createPagedFeed(loader, sentinel) {
  const [items, setItems] = createSignal([]);
  const [cursor, setCursor] = createSignal('__start__');
  const [loading, setLoading] = createSignal(false);
  let seq = 0;

  async function loadMore() {
    if (loading() || cursor() === null) return;   // 去重 + 终止
    setLoading(true);
    const my = ++seq;
    try {
      const res = await loader(cursor(), items().at(-1)?.id);
      if (my !== seq) return;                     // 过期响应丢弃
      const seen = new Set(untrack(items).map((i) => i.id)); // 快照去重
      setItems([...untrack(items), ...res.items.filter((i) => !seen.has(i.id))]);
      setCursor(res.nextCursor);                  // null = 没有更多
    } finally {
      setLoading(false);
    }
  }

  const io = new IntersectionObserver((ents) => {
    if (ents.some((e) => e.isIntersecting)) loadMore();
  }, { rootMargin: '400px' });
  io.observe(sentinel);

  return {
    items, cursor, loading,
    destroy() { io.disconnect(); seq++; },
  };
}
// 渲染：effect(() => renderList(items()))；cursor() === null 时显示"没有更多了"
```

**评分点**：
- loading 门禁 + cursor 终止态双守卫；哨兵 IO 提前量。
- seq 丢弃过期响应；untrack 快照读取（items 在异步回调里读需快照）。
- id 去重合并（分页重叠容错）。
- destroy 里 seq++ 使进行中请求作废。
