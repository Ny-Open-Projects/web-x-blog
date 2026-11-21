---
title: [MFW-198] 笔试：手写 payload 序列化精简器（函数剔除 + 引用去重）
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-198：笔试：手写 payload 序列化精简器（函数剔除 + 引用去重）
**题目**：实现 `preparePayload(obj)`，把服务端状态清洗成可安全注入 HTML 的 payload：① 递归剔除函数、DOM 节点、Symbol 键（不可序列化内容）；② 循环引用不炸（记录已见对象，第二次出现用引用占位符 `$ref`）；③ 数组/对象深拷贝但保持结构；④ Date/Map/Set 转 JSON 安全结构（ISO 字符串 / 数组），标注类型以便客户端还原；⑤ 体积统计：输出清洗前后的 JSON 大小对比。

```ts
type Cleaned = unknown;

export function preparePayload(obj: unknown): { payload: Cleaned; stats: { before: number; after: number } } {
  const seen = new Map<object, string>();
  const stats = { before: sizeOf(obj), after: 0 };
  const payload = clean(obj, seen, '$');
  stats.after = sizeOf(payload);
  return { payload, stats }; // ⑤
}

function clean(v: unknown, seen: Map<object, string>, path: string): Cleaned {
  if (typeof v === 'function' || typeof v === 'symbol') return undefined; // ① 剔除
  if (v instanceof Node) return undefined;                                 // ① DOM
  if (v instanceof Date) return { $type: 'date', value: v.toISOString() }; // ④
  if (v instanceof Map) return { $type: 'map', value: [...v].map(([k, val]) => [String(k), clean(val, seen, path)]) };
  if (v instanceof Set) return { $type: 'set', value: [...v].map((x) => clean(x, seen, path)) };

  if (v && typeof v === 'object') {
    if (seen.has(v)) return { $ref: seen.get(v) }; // ② 循环/重复引用 → 占位
    seen.set(v, path);
    if (Array.isArray(v)) return v.map((x, i) => clean(x, seen, `${path}[${i}]`));
    const out: Record<string, Cleaned> = {};
    for (const [k, val] of Object.entries(v)) { // Object.entries 自动跳过 Symbol 键
      const c = clean(val, seen, `${path}.${k}`);
      if (c !== undefined) out[k] = c;
    }
    return out;
  }
  return v;
}

function sizeOf(v: unknown) {
  try { return JSON.stringify(v)?.length ?? 0; } catch { return -1; } // 循环引用可能炸，保护
}
```

**评分点**：
1. 循环引用用路径占位符（`$ref`）而非直接 JSON.stringify（会抛 Converting circular structure to JSON）。
2. 函数/DOM/Symbol 的剔除属于「静默丢弃」：能主动说明风险——服务端渲染用的函数被剔除后，客户端还原可能行为不一致。
3. Date/Map/Set 用类型标注包装（`$type`）而不是直接转字符串，保证客户端能识别并还原类型。
4. Object.entries 天然跳过 Symbol 键，用 Object.keys 需要额外说明；能指出这点是加分。
5. 输出前后体积统计，体现「payload 精简可度量」的工程意识（Nuxt DevTools payload 面板同理）。