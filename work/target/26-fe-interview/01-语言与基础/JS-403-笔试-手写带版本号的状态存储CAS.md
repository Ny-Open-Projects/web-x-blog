---
title: [JS-403] 笔试：手写带版本号的状态存储（乐观锁 CAS）
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 笔试题, 并发]
type: 笔试题
---

## JS-403：笔试：手写带版本号的状态存储

**答**：实现 `VersionedStore<T>`：① get() 返回 `{ value, version }`；② `update(expectedVersion, updater)`：版本一致才提交（CAS），不一致返回 `{ ok: false, current }`；③ update 支持异步 updater（await 期间版本可能被别人改——提交前再校验）；④ 订阅：`subscribe(fn)` 通知每次成功更新（带新版本）；⑤ history 最近 5 个版本可回滚。写出实现。

```javascript
class VersionedStore {
  #v = 0; #value; #subs = new Set(); #history = [];
  constructor(initial) { this.#value = initial; }
  get() { return { value: this.#value, version: this.#v }; }
  async update(expectedVersion, updater) {
    // 异步 updater 前先占位校验
    if (expectedVersion !== this.#v) return { ok: false, current: this.get() };
    const snapshot = this.#value;
    const next = await updater(snapshot);            // 异步计算
    // 提交前二次校验(期间可能有并发更新)
    if (expectedVersion !== this.#v) return { ok: false, current: this.get() };
    this.#history.push({ value: this.#value, version: this.#v });
    if (this.#history.length > 5) this.#history.shift();
    this.#value = next; this.#v++;
    this.#subs.forEach(fn => fn(this.get()));
    return { ok: true, current: this.get() };
  }
  subscribe(fn) { this.#subs.add(fn); return () => this.#subs.delete(fn); }
  rollback() {
    const last = this.#history.pop();
    if (!last) return { ok: false };
    this.#value = last.value; this.#v++;
    this.#subs.forEach(fn => fn(this.get()));
    return { ok: true, current: this.get() };
  }
}
// 用法: 编辑器协同的本地乐观锁
const doc = new VersionedStore('# title');
const { version } = doc.get();
const r = await doc.update(version, (v) => v + '\n新内容');
if (!r.ok) console.warn('被别人改了', r.current);
```

**评分点**：
- CAS 双重校验（进入时 + 异步 updater 提交前），防 await 窗口竞态
- 版本单调递增（回滚也 +1，不回退版本号）
- 订阅通知带完整 {value, version}
- history 容量上限与回滚语义
