---
title: [MFW-674] ISR 批量预渲染：Sku 列表优化
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-674：ISR 批量预渲染

**答**:
- 大量 SKU 的批量预渲染（RBL-599 的 ISR 深化）：1) **批量 API**（批量 revalidate path（Next 的 revalidatePath 数组形式——一次 API 调用批量失效）；2) 分批 revalidate（100 页/批——避免渲染集群打满 RBL-599 流量加权）；3) 预渲染的监控（每批的渲染耗时/失败率——批次的可观测）。
- SKU 列表的特殊性：SKU 数百万 → 无法全量预渲染——「热点 SKU 预渲染 + 长尾 on-demand」（RBL-599 加权策略的 ISR 版）；「热点识别」：RUM 流量/销量排名。
- 批量预渲染的实现：Next 的 revalidatePath 是逐个调（for 循环——N 次 API 调用）vs revalidateTag（一次调失效 N 页——tag 批量 > path 批量）；「tag > path 的批量效率」。
- 追问钩子：为什么「revalidateTag 优于 revalidatePath 循环」在批量场景？——path 循环 = N 次 API 调用（每次一次重生成队列项）；tag = 一次调用失效整类（框架内一次标记 + 后台惰性重生成——按需渲染而非立即全渲染）；「tag 的惰性失效」语义：失效后首次访问才重生成（不需要全部预渲染——访问驱动）——大促场景「改价 10 万 SKU」：tag 失效（一次）+ 首访问按需渲染（用户访问多少渲染多少）比「全量预渲染」更经济。

```typescript
// tag 批量失效（优于 path 循环）
import { revalidateTag } from 'next/cache';
// 改价 10 万 SKU：一次 tag 失效
revalidateTag('products');                               // 惰性：首次访问才重渲染
// 而非 for 循环 revalidatePath（N 次 API）
// for (const sku of skus) revalidatePath(`/p/${sku}`);   ← 10 万次调用！
// 热点预渲染（tag 失效后主动渲染 Top）
async function preheatHotSkus(topSkus: string[]) {
  await Promise.allSettled(
    topSkus.map(sku => fetch(`${origin}/p/${sku}`, { headers: { 'x-preheat': '1' } })));
}
// tag 层级失效（RBL-578）
revalidateTag(`product:${sku}`);                        // 单 SKU 失效
revalidateWithHierarchy('products');                    // 全类失效（含所有 product:*）
```
