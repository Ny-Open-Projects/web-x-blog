---
title: [MFW-579] RSC 下的无限滚动：游标加载与虚拟化的适配
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-579：RSC 下的无限滚动

**答**:
- 无限滚动的三种形态在 RSC 下的适配：1) **RSC 游标流**（fetchMore 用 server action 返回 Flight patch——新 items 直接进组件树（无需 client 状态管理）；2) **route handler + client 状态**（useInfiniteQuery 风格——数据进 client store RBL-547）；3) **SSR 首屏 + client 增量**（首屏 RSC、后续 client fetch——混合）。
- 虚拟化与 RSC 的配合：RSC 渲染的列表是「已有数据的树」——虚拟化在 client（窗口外不渲染 DOM——树还在 payload 里）；「payload 全量 vs 虚拟化渲染」：万条数据全量 payload = 传输爆炸——游标分页（每页 20 条 Flight patch——增量传输 RBL-560）。
- 滚动位置的恢复（返回列表页）：Router Cache 的 payload 含已加载页（state 保存在组件树——RSC patch 保留滚动——返回导航 payload 缓存命中 RBL-511）。
- 追问钩子：为什么「RSC + 游标流」比「client useInfiniteQuery」更适合内容型无限滚动？——RSC 流：数据即树（无 client 状态同步/缓存失效自动/RSC 可服务端聚合）；client query：灵活（client 侧过滤/排序）但状态管理复杂（缓存失效手动）；「数据展示型」用 RSC 流（server 权威）、「交互编辑型」用 client 状态（client 权威）——数据的权威归属决定数据流形态（RBL-547 的滚动版）。

```tsx
// RSC 游标流的无限滚动
// app/list/page.tsx
export default async function List({ searchParams }) {
  const cursor = searchParams.cursor;
  const { items, nextCursor } = await getItems(cursor);  // SSR 首屏
  return (
    <>
      <ListItems items={items} />
      {nextCursor && <LoadMore cursor={nextCursor} />}
    </>
  );
}
// LoadMore：server action 返回 Flight patch
'use client';
function LoadMore({ cursor }) {
  const [items, setItems] = useState([]);                // patch 追加
  const ref = useRef();
  useEffect(() => observer(ref, () => loadMore()), []);
  async function loadMore() {
    // 调 server action：返回 RSC 格式的新 items
    const more = await fetchItemsAction(cursor);         // 返回序列化数据
    setItems(prev => [...prev, ...more.items]);
  }
  return <div ref={ref}>{items.map(render)}</div>;       // 虚拟化包裹可选
}
// 虚拟化：payload 全量但 DOM 窗口化
// 万条全量 payload 是反模式 → 游标每页 20 条增量
```
