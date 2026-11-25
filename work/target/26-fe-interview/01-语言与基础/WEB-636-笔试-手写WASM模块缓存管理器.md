---
title: [WEB-636] 笔试：手写 WASM 模块缓存管理器（IndexedDB）
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, WebAssembly]
type: 笔试题
---

## WEB-636：笔试：手写 WASM 模块缓存管理器

**答**：实现 `WasmModuleCache`：① `get(url, version)`：命中缓存（url+version key）直接返回 Module；未命中下载编译后写缓存；② 并发防抖：同一 key 同时多个请求只触发一次编译（in-flight promise 复用）；③ 缓存上限：Module 数量超过 maxEntries（默认 10）时按 LRU 淘汰；④ 缓存读取失败（IDB 损坏/结构化克隆不支持）静默降级网络编译；⑤ `clear()` 清空。写出核心实现。

```javascript
class WasmModuleCache {
  constructor(store, maxEntries = 10) {
    this.store = store; this.max = maxEntries;
    this.inflight = new Map();
    this.order = []; // LRU: 最近使用在尾
  }
  async get(url, version) {
    const key = `${url}@${version}`;
    // 1) in-flight 复用
    if (this.inflight.has(key)) return this.inflight.get(key);
    // 2) IDB 命中
    try {
      const hit = await this.store.get(key);
      if (hit) { this._touch(key); return hit; }
    } catch {} // IDB 损坏静默降级
    // 3) 下载+编译
    const p = (async () => {
      const mod = await WebAssembly.compileStreaming(fetch(`${url}?v=${version}`))
        .catch(async () => WebAssembly.compile(await (await fetch(`${url}?v=${version}`)).arrayBuffer()));
      try { await this.store.set(key, mod); this._touch(key); await this._evict(); } catch {}
      return mod;
    })();
    const final = p.finally(() => this.inflight.delete(key)); // 失败也清，保证该 key 之后可重试
    this.inflight.set(key, final);
    return final;
  }
  _touch(key) {
    this.order = this.order.filter(k => k !== key);
    this.order.push(key);
  }
  async _evict() {
    while (this.order.length > this.max) {
      const old = this.order.shift();
      try { await this.store.del(old); } catch {}
    }
  }
  clear() { this.order = []; return this.store.clear(); }
}
```

**评分点**：
- in-flight promise 复用，防同 key 并发重复编译
- LRU 淘汰基于访问顺序数组，上限可配
- IDB 异常静默降级网络编译，主流程不中断
- key 绑定 version 防缓存脏模块

## 变体与延伸（补充）

**变体与延伸**：

1. 为什么缓存 Module 而不是 Instance？ → Module 是编译后的不可变产物可共享，Instance 带可变线性内存与全局状态，缓存 Instance 会让不同调用方串状态。
2. 往 IndexedDB 存 WebAssembly.Module 依赖什么前提？ → 依赖引擎对 Module 的结构化克隆支持，不支持时 set 会抛错，需降级为只缓存字节流再本地编译。
3. LRU 用数组 filter 重建有什么性能问题？ → 每次 _touch 都 O(n) 重建数组，条目多或命中频繁时开销明显，应改用 Map 的 delete+set 保序或双向链表。
