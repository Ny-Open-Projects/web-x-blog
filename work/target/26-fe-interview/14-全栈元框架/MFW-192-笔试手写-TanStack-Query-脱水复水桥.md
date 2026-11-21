---
title: [MFW-192] 笔试：手写 TanStack Query 风格的脱水复水桥
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-192：笔试：手写 TanStack Query 风格的脱水复水桥
**题目**：实现最小化的 Query 缓存脱水复水：① 服务端 `dehydrate(cache)` 把缓存项序列化为可嵌入 HTML 的 JSON（key 序列化、状态收敛为 `{ data, dataUpdatedAt }`）；② `serialize` 产出防 XSS 的 script 标签内容（转义 `</script`）；③ 客户端 `hydrate(cache, payload)` 把条目写回缓存，且**只写客户端没有的/更新的**（客户端已 invalidated 的条目不覆盖）；④ 进行中的 promise 不能序列化（跳过并标记）。

```ts
type Entry = { data: unknown; dataUpdatedAt: number; invalidated?: boolean };
type Dehydrated = Record<string, { data: unknown; dataUpdatedAt: number }>;

export function dehydrate(cache: Map<string, Entry>): Dehydrated {
  const out: Dehydrated = {};
  for (const [k, e] of cache) {
    if (e.data instanceof Promise) continue; // ④ promise 无法序列化，跳过
    if (e.data instanceof Error) continue;   // 错误态不复水（防客户端卡死在错误）
    out[JSON.stringify(k)] = { data: e.data, dataUpdatedAt: e.dataUpdatedAt }; // ①
  }
  return out;
}

// ② 防 XSS：终结 script 标签的字面量必须转义
export function serialize(payload: Dehydrated): string {
  const json = JSON.stringify(payload)
    .replace(/</g, '\\u003c')
    .replace(/>/g, '\\u003e')
    .replace(/&/g, '\\u0026');
  return `<script>window.__Q_DATA__=${json}</script>`;
}

export function hydrate(cache: Map<string, Entry>, payload: Dehydrated) {
  for (const [k, v] of Object.entries(payload)) {
    const key = JSON.parse(k);
    const local = cache.get(key);
    // ③ 客户端已有且更新（或已主动失效）的不被服务端旧值覆盖
    if (local && (local.invalidated || local.dataUpdatedAt >= v.dataUpdatedAt)) continue;
    cache.set(key, { data: v.data, dataUpdatedAt: v.dataUpdatedAt });
  }
}

// 注入与读取
export const inject = (payload: Dehydrated) => serialize(payload);
export const read = (): Dehydrated => (typeof window !== 'undefined' && window.__Q_DATA__) || {};
```

**评分点**：
1. 复水冲突策略：客户端更新时间更新或已主动 invalidate 的条目不被服务端旧值覆盖——漏掉会回滚用户刚做的操作。
2. promise 与错误态都不脱水：promise 无法序列化，错误态复水会让客户端直接卡在错误缓存上。
3. 序列化必须转义 `<`/`&`，防止 `</script>` 提前闭合标签注入脚本（只转义引号不够）。
4. key 用序列化字符串作对象键（Query 的 key 是数组），能说明数组 key 不能直接当对象键的原因。
5. 提到真实 TanStack Query 的 dehydrate 支持 shouldDehydrateQuery 控制、默认只脱水成功查询。