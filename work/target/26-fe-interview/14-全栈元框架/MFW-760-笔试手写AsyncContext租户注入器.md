---
title: [MFW-760] 笔试：手写 AsyncContext 租户注入
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-760：笔试：手写 AsyncContext 租户注入

**答**：实现 `createTenantContext({ resolveTenant, onMissing })`。resolveTenant: `(host) => string | null`。返回 `{ run<T>(host, fn): Promise<T>`, `getTenant(): string`, `requireTenant(): string` }`。规则：1) run：ALS.run 包裹（fn 执行期间上下文有效——异步传播：fn 内的 await 链都可获取）；2) getTenant：返回当前租户（null = 无上下文）；requireTenant：无上下文 → 抛错（强制租户——安全边界：DB 查询必须有租户）；3) resolveTenant 失败 → onMissing 回调（记录/拒绝——RBL-519 多租户安全）；4) **并发隔离**：两个 run 并发（不同租户——各自上下文互不污染 RBL-657）。边界：run 嵌套（内层覆盖外层——ALS 嵌套语义）；fn 同步（ALS 同步也有效——run 返回值透传）。

```javascript
import { AsyncLocalStorage } from 'async_hooks';
function createTenantContext({ resolveTenant, onMissing = () => {} } = {}) {
  const als = new AsyncLocalStorage();
  return {
    async run(host, fn) {
      const tenant = resolveTenant?.(host);
      if (!tenant) {
        onMissing({ host });
        throw new Error(`Unknown tenant: ${host}`);
      }
      return als.run({ tenant }, fn);                    // ALS 上下文包裹
    },
    getTenant() { return als.getStore()?.tenant ?? null; },
    requireTenant() {
      const t = als.getStore()?.tenant;
      if (!t) throw new Error('tenant 上下文缺失——DB 查询必须有租户');
      return t;
    },
  };
}

// 自测
const hostMap = { 'a.app.com': 'tenant-a', 'b.app.com': 'tenant-b' };
const ctx = createTenantContext({ resolveTenant: (h) => hostMap[h] ?? null });

// 正常传播
const r1 = await ctx.run('a.app.com', async () => {
  await sleep(5);                                        // 异步链
  return ctx.getTenant();                                // 上下文传播到 await 后
});
console.log(r1 === 'tenant-a');

// 并发隔离
const [rA, rB] = await Promise.all([
  ctx.run('a.app.com', async () => { await sleep(10); return ctx.getTenant(); }),
  ctx.run('b.app.com', async () => { await sleep(5); return ctx.getTenant(); }),
]);
console.log(rA === 'tenant-a' && rB === 'tenant-b');     // 互不污染

// requireTenant 无上下文 → 抛错
let e; try { ctx.requireTenant(); } catch (x) { e = x; }
console.log(/上下文缺失/.test(e.message));

// run 内 requireTenant
const r2 = await ctx.run('b.app.com', () => ctx.requireTenant());
console.log(r2 === 'tenant-b');

// 未知 host → onMissing + 抛错
const missing = [];
const ctx2 = createTenantContext({
  resolveTenant: () => null,
  onMissing: (info) => missing.push(info),
});
e = null; try { await ctx2.run('unknown.com', async () => {}); } catch (x) { e = x; }
console.log(/Unknown tenant/.test(e.message) && missing.length === 1);
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
```

**评分点**：
- ALS 的异步传播（await 链中上下文有效）；并发隔离（不同 host 的 run 互不污染）
- requireTenant 的安全边界（无上下文 = 抛错——DB 查询强制租户）；onMissing 回调（审计）
- 边界（嵌套/同步 fn/未知 host）；ALS 嵌套语义
- 能说清「ALS 的隐式传播消除手动传参的遗漏风险——db 查询/缓存/日志从 context 取租户」属于加分
