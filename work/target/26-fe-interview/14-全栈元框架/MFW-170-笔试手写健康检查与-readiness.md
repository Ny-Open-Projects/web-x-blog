---
title: [MFW-170] 笔试：手写健康检查端点（liveness 与 readiness 分离）
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-170：笔试：手写健康检查端点（liveness 与 readiness 分离）
**题目**：为 SSR 应用实现两个端点：① `/api/health`（liveness）：进程活着即 200，不检查依赖；② `/api/ready`（readiness）：检查 DB/缓存下游连通，任一不可用返回 503；③ readiness 检查带独立超时（不能被慢 DB 拖死探针）；④ 响应带各依赖耗时明细；⑤ 进程优雅关闭期间 readiness 返回 503（先行摘流）。

```ts
import { pool } from '../lib/db';

// 优雅关闭信号：SIGTERM 时置位，readiness 立即 503 摘流
let shuttingDown = false;
process.on('SIGTERM', () => { shuttingDown = true; });

// 单项依赖检查：带独立超时，绝不互相拖死
async function checkDb(): Promise<{ ok: boolean; ms: number }> {
  const t0 = Date.now();
  try {
    await pool.query('SELECT 1', { signal: AbortSignal.timeout(1500) }); // 1.5s 独立超时
    return { ok: true, ms: Date.now() - t0 };
  } catch {
    return { ok: false, ms: Date.now() - t0 };
  }
}

async function checkCache(): Promise<{ ok: boolean; ms: number }> {
  const t0 = Date.now();
  try {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 1000); // 1s 超时
    const res = await fetch(process.env.CACHE_URL + '/ping', { signal: controller.signal });
    clearTimeout(timer);
    return { ok: res.ok, ms: Date.now() - t0 };
  } catch {
    return { ok: false, ms: Date.now() - t0 };
  }
}

// GET /api/health —— liveness：进程活着就 200
export async function healthHandler(): Promise<Response> {
  return Response.json({ status: 'ok', uptime: process.uptime() });
}

// GET /api/ready —— readiness：下游全绿才 200
export async function readyHandler(): Promise<Response> {
  if (shuttingDown) {
    // 优雅关闭：先摘流（503），让 LB 停止派发，再排空退出
    return Response.json({ status: 'shutting-down' }, { status: 503 });
  }
  const [db, cache] = await Promise.all([checkDb(), checkCache()]); // 并行，不串行叠加
  const details = { db, cache };
  const allOk = db.ok && cache.ok;
  return Response.json(
    { status: allOk ? 'ready' : 'not-ready', details },
    { status: allOk ? 200 : 503, headers: { 'Cache-Control': 'no-store' } }, // 探针响应不缓存
  );
}
```

**评分点**：
1. liveness 与 readiness 语义分离正确：liveness 不查依赖（避免下游抖动触发重启风暴），readiness 查依赖。
2. 每项检查独立超时（AbortController/timeout），并行执行不叠加延迟。
3. SIGTERM 置位 shuttingDown，readiness 先行 503 摘流——优雅关闭闭环。
4. 探针响应 no-store（缓存探针结果是经典事故）。
5. 明细带耗时，排障时能看出哪个依赖慢。
