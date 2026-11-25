---
title: [MFW-802] 笔试：手写 Server Action 事务上下文传播器（渲染期写操作拦截）
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-802：笔试：手写 Server Action 事务上下文传播器（渲染期写操作拦截）

**答**：
- 结论：用 AsyncLocalStorage 把事务对象绑定到「一次 action 调用」，所有写操作必须先取到事务上下文，取不到就抛错——把「渲染只读」从口头约定变成机制。
- 关键：写操作 write() 从 ALS 读当前 tx；Server Action 用 withTx(tx, fn) 显式开启事务；渲染阶段没有上下文，调用 write 直接失败。
- 追问钩子：为什么不能用模块级全局变量存 tx？——并发请求会串台；ALS 按异步调用链隔离，是 Node 请求级上下文的标准解法。

```javascript
const { AsyncLocalStorage } = require('async_hooks');
const als = new AsyncLocalStorage();

function withTx(tx, fn) { return als.run(tx, fn); }
function getTx() {
  const tx = als.getStore();
  if (!tx) throw new Error('写操作必须在 Server Action 事务中');
  return tx;
}
async function write(fn) { return getTx().exec(fn); }   // 受保护写

// Server Action：显式开启事务并把写包进上下文
async function transfer(from, to, amount) {
  const tx = await db.begin();
  try {
    return await withTx(tx, async () => {
      await write(() => db.dec(from, amount));           // ✓ 有 tx
      await write(() => db.inc(to, amount));
      await tx.commit();
    });
  } catch (e) { await tx.rollback(); throw e; }
}

// 自测：渲染阶段直接写 → 抛错（无事务上下文）
try { write(() => db.dec('a', 1)); }
catch (e) { console.log(e.message); }   // 写操作必须在 Server Action 事务中
// 并发隔离：两个 transfer 各跑各的 tx，互不串台
```

**评分点**：
- 用 AsyncLocalStorage 在 await 跨异步边界保持上下文；说明为何模块级变量会导致并发请求串台
- 写操作强制校验事务上下文，渲染期无上下文即抛错——把「渲染只读」机制化
- 事务 begin/commit/rollback 完整包裹，异常路径正确回滚
- 能指出强约束的代价：读操作不应走该校验，否则纯读 RSC 也会被误伤
