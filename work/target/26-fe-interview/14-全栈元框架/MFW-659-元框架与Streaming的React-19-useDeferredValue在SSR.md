---
title: [MFW-659] useDeferredValue 在 SSR 的行为
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-659：useDeferredValue SSR 行为

**答**:
- useDeferredValue 在 SSR 的语义：SSR 渲染时**不用 defer**（直接渲染传入值——服务端无交互优先级）——deferred 的语义只在 client 水合后生效；「SSR 渲染的值 = 最新值」而 client 首渲染也用最新值（无旧值可 defer）——水合后交互时才 defer。
- 与 RSC 流式的交互：deferred value 是「client 侧的渲染优先级」——SSR 数据流式（RBL-520）+ client 交互的 defer（输入时旧 UI 保持、新值后台渲染）——两者是不同阶段的优化（初始渲染流式 vs 交互更新 defer）。
- SSR 期间的搜索场景：搜索页 SSR 用 URL 中的 query（服务端搜索）——client 交互输入 → deferred query → 防抖后的 fetch——「URL 驱动（SSR）× 输入驱动（client）」的双态。
- 追问钩子：为什么「useDeferredValue 在 SSR 不 defer」不是 bug 而是正确行为？——SSR 只有「一次渲染」（无交互优先级可言——defer 的价值是「让旧 UI 保持可交互」而 SSR 时没有旧 UI）；SSR 的优化维度是「流式/缓存」（RBL-520）；client 水合后 defer 才有意义（有旧 UI 可保持）——defer 的语义边界 = 交互开始（水合完成）；理解每个 hook 的 SSR/client 语义差异是 RSC 架构的必修课。

```tsx
// SSR + client 双态搜索
'use client';
function SearchBox({ initialQuery }: { initialQuery: string }) {
  const [query, setQuery] = useState(initialQuery);
  const deferredQuery = useDeferredValue(query);         // SSR: 直接用 query（无 defer）
  // client 水合后：输入时 deferredQuery 滞后（旧结果保持渲染）
  const results = useMemo(() => filterItems(deferredQuery), [deferredQuery]);
  return (
    <>
      <input value={query} onChange={(e) => setQuery(e.target.value)} />
      <Results items={results} />
      {/* isStale 指示：deferredQuery !== query 时显示加载态 */}
      {deferredQuery !== query && <span>搜索中…</span>}
    </>
  );
}
// SSR 首屏：initialQuery 渲染（URL 驱动 RBL-653）
// client 输入：deferredQuery 滞后 → 旧结果保持可交互（INP 优化 RBL-640）
```
