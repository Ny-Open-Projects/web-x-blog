---
title: [MFW-084] 笔试：手写一个简化版 useAsyncData
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-084：笔试：手写一个简化版 useAsyncData
**题目**：实现 `useAsyncData(key, fn, options)` 的核心能力：① SSR 阶段执行 fn 并把结果存入 payload；② 客户端复水时按 key 命中则不重复请求；③ 同 key 并发调用去重（共享 pending）；④ 返回 `{ data, error, status, refresh }`；⑤ 支持 `lazy: true`（不阻塞首屏）。

```ts
import { ref, computed } from 'vue';

type Opts = { server?: boolean; lazy?: boolean };

const payload = (globalThis.__NUXT_PAYLOAD__ ??= { data: {} as Record<string, unknown> });
const dedupe = new Map<string, Promise<unknown>>();

function useAsyncData<T>(
  key: string,
  fn: () => Promise<T>,
  opts: Opts = {},
) {
  const data = ref<T | null>(payload.data[key] ?? null);
  const error = ref<unknown>(null);
  const status = ref<'idle' | 'pending' | 'success' | 'error'>('idle');

  async function execute(): Promise<void> {
    if (status.value === 'pending') return; // 防同实例重入
    // 复水：payload 已有该 key 的 SSR 结果，直接用
    if (key in payload.data) {
      data.value = payload.data[key] as T;
      status.value = 'success';
      delete payload.data[key]; // 一次性消费，refresh 可重新请求
      return;
    }
    // 同 key 去重：共享同一个 in-flight Promise
    let p = dedupe.get(key) as Promise<T> | undefined;
    if (!p) {
      status.value = 'pending';
      p = fn().finally(() => dedupe.delete(key));
      dedupe.set(key, p);
      try {
        payload.data[key] = await p;        // SSR 侧写入 payload 供复水
        data.value = payload.data[key] as T;
        status.value = 'success';
      } catch (e) {
        error.value = e;
        status.value = 'error';
      }
    } else {
      try { data.value = await p; status.value = 'success'; } catch (e) { error.value = e; status.value = 'error'; }
    }
  }

  const shouldRun = opts.server === false ? false : true;
  if (shouldRun && !opts.lazy) execute();          // 阻塞式：await 用在 setup 顶层
  else if (shouldRun) execute();                    // lazy：不阻塞，UI 显示 pending

  function refresh() { delete payload.data[key]; return execute(); }

  return { data, error, status, refresh };
}

// SSR 复水入口：客户端启动时把 window.__NUXT__ 注回 payload
if (typeof window !== 'undefined') {
  Object.assign(payload.data, (window as any).__NUXT__?.data ?? {});
}
```

**评分点**：
1. 复水逻辑按 key 查 payload，命中即跳过 fn（这是防双请求的核心）。
2. 模块级 dedupe Map 共享 pending Promise，能说出 finally 时清理。
3. refresh 必须先清 payload 再执行，否则永远读旧值。
4. lazy 语义正确：只是不阻塞导航，仍会发起请求。
5. data/error/status 用响应式 ref 包装，返回可组合的状态对象。
