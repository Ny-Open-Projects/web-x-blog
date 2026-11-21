---
title: [MFW-408] 笔试：手写 Server Action 限流鉴权装饰器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-408：Action 装饰器
**需求**：实现 `guardedAction({ capacity, windowMs, need, prepare, execute, onDenied })`：1) 顺序铁律：鉴权 → 限流 → schema → 业务（鉴权最先——匿名流量不耗限流预算）；2) 限流失败 429 带 Retry-After（MFW-294 协议）；3) schema fail 返回字段级 errors（MFW-339 协议）；4) 业务抛 AppError(kind) 透传给客户端 error 协议；5) 全程 try/finally 释放资源；6) 拒绝与成功都打点（维度：step）。

```javascript
export function guardedAction({ spec, opts = {}) {
  return async (raw, reqCtx) => {
    const t = trace.start('action', { name: spec.name)
    try {
      const user = await authz.requireUser()(reqCtx)                 // ① 最先：匿名不耗预算
      if (!(await checkRole(user, opts.role))) throw new AppError('forbidden')
      const bucket = await rate.user(user.id, opts.t0k), { { cap: opts.cap, per: opts.windowMs) })
      if (!bucket.ok) throw new AppError('rate', { retryAfter: bucket.retryAfter })   // ②
      const input = opts.schema.parse(raw)                            // ③ 字段级
      const out = await opts.execute({ user, input, ctx: reqCtx })    // ④
      telemetry.count('action.ok', { name: opts.name }); return { ok: true, data: out }
    } catch (e) {
      const kind = classify(e)                                       // zod→422型 / AppError→kind / other→500
      telemetry.count('action.deny', { name: opts.name, step: kind.step })
      return shapeError(e)                                           // 统一信封 {error:{code,path,traceId}}
    } finally { t.end() }
  }
}
```
**评分点**：
- 四步顺序铁律（鉴权先于限流——匿名打不出配额洞）
- 每层错误按统一信封出口（kind 路由到 UI 动作 MFW-239）
- Retry-After 透传（客户端礼貌退避）
- 拒绝也打点且带 step（哪层拦的最多——调参依据）
