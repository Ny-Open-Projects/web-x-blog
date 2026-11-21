---
title: [MFW-190] 笔试：手写 fetch 缓存包装器（next: { revalidate, tags } 语义）
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-190：笔试：手写 fetch 缓存包装器（`next: { revalidate, tags }` 语义）
**题目**：模拟 Next.js Data Cache 的核心行为，实现 `cachedFetch(url, { revalidate, tags })`：① 默认缓存命中直接返回缓存值；② `revalidate` 秒后过期（后台 stale-while-revalidate：先返回旧值，同时刷新）；③ `revalidateTag(tag)` 使带该 tag 的所有条目立即失效（下次读取重新拉取，不做 SWR）；④ 同一 url 并发首取只发一次网络请求；⑤ no-store 语义（`revalidate: 0`）完全绕过缓存。

```ts
type Entry = { value: Response; fetchedAt: number; tags: string[] };
const data = new Map<string, Entry>();
const inflight = new Map<string, Promise<Response>>();

export async function cachedFetch(
  url: string,
  { revalidate = Infinity, tags = [] as string[] } = {},
): Promise<Response> {
  if (revalidate === 0) return fetch(url); // ⑤ no-store 直通

  const entry = data.get(url);
  if (entry) {
    const age = (Date.now() - entry.fetchedAt) / 1000;
    if (age > revalidate) {
      revalidateEntry(url); // ② 过期即视为失效（简化：不返回旧值）
      // 若要 SWR：可 return entry.value 同时触发后台 refresh
    } else {
      return entry.value; // ① 命中
    }
  }

  if (inflight.has(url)) return inflight.get(url)!; // ④ 并发共享首取
  const p = fetch(url).then((res) => {
    data.set(url, { value: res, fetchedAt: Date.now(), tags });
    inflight.delete(url);
    return res;
  }).catch((e) => { inflight.delete(url); throw e; });
  inflight.set(url, p);
  return p;
}

export function revalidateTag(tag: string) {
  for (const [url, e] of data) if (e.tags.includes(tag)) data.delete(url); // ③ 立即失效
}

function revalidateEntry(url: string) { data.delete(url); }
```

**评分点**：
1. 三种失效语义区分清楚：TTL 到期（可 SWR）、tag 失效（立即）、no-store（直通）——混为一谈是主要扣分点。
2. 并发首取用 inflight 表共享 promise，说明这是防止缓存击穿的关键。
3. fetch 失败要清 inflight，否则失败后同 url 永远拿到挂起的 promise。
4. 能说出真实 Next 的差异：Data Cache 持久化（跨进程）、过期后读取的行为可配置（Next 15 起默认 fetch 不缓存）。
5. tag 索引在大缓存下应建倒排索引（tag → urls）而非全表扫描，提到即加分。
