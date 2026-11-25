---
title: [V3-161] 接口数据的多级缓存策略如何实现（内存 + sessionStorage 两级）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-161：接口数据的多级缓存策略如何实现（内存 + sessionStorage 两级）？
**答**：
- 两级定位：内存 Map 承担高频读（刷新即失效），sessionStorage 承担跨页面跳转的存活（标签页关闭才失效）。
- 统一封装 CacheItem：{ value, expireAt }，读取时先查内存、未命中查 storage、过期即删并回源请求。
- 序列化注意：sessionStorage 只存字符串，响应里的 Date/Map 要约定降级策略，日期存 ISO 字符串。
- 使用方无感：useCachedRequest 与普通 useRequest 同签名，只是命中缓存时不发请求。

```typescript
// src/composables/useCachedRequest.ts —— 两级缓存 + 过期回源
import { ref, onMounted, type Ref } from "vue";
interface CacheItem<T> {
  value: T;
  expireAt: number;
}

const memoryCache = new Map<string, CacheItem<unknown>>(); // L1：内存

function readThrough<T>(key: string): T | null {
  // L1 内存
  const hit = memoryCache.get(key) as CacheItem<T> | undefined;
  if (hit && hit.expireAt > Date.now()) return hit.value;
  memoryCache.delete(key);

  // L2 sessionStorage
  try {
    const raw = sessionStorage.getItem(`cache:${key}`);
    if (raw) {
      const item = JSON.parse(raw) as CacheItem<T>;
      if (item.expireAt > Date.now()) {
        memoryCache.set(key, item); // 回填 L1
        return item.value;
      }
      sessionStorage.removeItem(`cache:${key}`);
    }
  } catch { /* 存储满或 JSON 损坏，静默回源 */ }
  return null;
}

function writeThrough<T>(key: string, value: T, ttlMs: number) {
  const item: CacheItem<T> = { value, expireAt: Date.now() + ttlMs };
  memoryCache.set(key, item);
  try {
    sessionStorage.setItem(`cache:${key}`, JSON.stringify(item));
  } catch { /* 超配额忽略，L1 仍有效 */ }
}

export function useCachedRequest<T>(url: string, ttlMs = 60_000) {
  const data = ref<T | null>(null);
  const loading = ref(false);
  const fromCache = ref(false);

  async function fetchIt() {
    loading.value = true;
    fromCache.value = false;
    data.value = await fetch(url).then((r) => r.json() as Promise<T>);
    writeThrough(url, data.value, ttlMs);
    loading.value = false;
  }

  onMounted(async () => {
    const cached = readThrough<T>(url);
    if (cached !== null) {
      data.value = cached;
      fromCache.value = true; // 命中：不发请求
      return;
    }
    await fetchIt();
  });

  return { data, loading, fromCache, refresh: fetchIt };
}

// 用法：字典类数据适合长 TTL（5 分钟），列表数据短 TTL（30 秒）
// const { data, fromCache } = useCachedRequest<Dict[]>("/api/dicts", 5 * 60_000);
```
