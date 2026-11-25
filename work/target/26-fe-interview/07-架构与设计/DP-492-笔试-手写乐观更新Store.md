---
title: [DP-492] 笔试：手写乐观更新 Store
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 笔试题, 设计模式]
type: 笔试题
---

## DP-492：笔试：手写乐观更新

**答**：实现乐观更新内核 `OptimisticStore`：① mutate(key, serverFn, optimistic)：乐观值立即入视图 → 请求 → 成功写真实值 / 失败回滚；② 连续乐观操作叠加：pending 队列按序 reducer 应用（基于最新真实值）；③ 精确回滚：只回滚失败的那条（其余 pending 保持）；④ 版本仲裁：服务端 rev 单调——旧响应不覆盖；⑤ snapshot()：{ view, real, pendingCount } 双态导出（调试乐观 UI）。写出实现。

```javascript
class OptimisticStore {
  #real = {}; #rev = 0; #pending = []; #subs = new Set();
  #view() { return this.#pending.reduce((acc, p) => ({ ...acc, ...p.patch(acc) }), this.#real); }
  #notify() { this.#subs.forEach((f) => f({ view: this.#view(), real: this.#real, pending: this.#pending.length })); }
  sub(fn) { this.#subs.add(fn); return () => this.#subs.delete(fn); }

  async mutate(key, serverFn, optimistic) {
    const id = crypto.randomUUID();
    this.#pending.push({ id, key, patch: optimistic, ts: Date.now() });
    this.#notify();                                    // 乐观立即生效
    try {
      const r = await serverFn();
      if (r.rev <= this.#rev) throw new Error('stale response');   // 版本仲裁
      this.#rev = r.rev;
      this.#real = { ...this.#real, ...r.data };
    } finally {
      const i = this.#pending.findIndex((p) => p.id === id);
      if (i >= 0) this.#pending.splice(i, 1);          // 只移除自己
      this.#notify();                                  // 真实值落地或该条回滚
    }
  }
}
// UI 只消费 view; 调试看 snapshot 区分 view/real
```

**评分点**：
- 乐观视图 = 真实值 + pending 队列叠加（语义正确）
- 精确回滚（只移除失败条目——其余 pending 保持）
- rev 版本仲裁（旧响应不覆盖新乐观值）
- view/real 双态导出（乐观 UI 调试的关键）
