---
title: [FRP-197] 手写防重提交 hook：loading 锁 + 幂等键的实现？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-197：手写防重提交 hook：loading 锁 + 幂等键的实现？

**答**：
- 防重提交的两层保障：**loading 锁**（进行中禁止再次触发，UI 同步禁用按钮）与**幂等键**（请求体带唯一 key，服务端对同 key 去重——网络重试/双击穿透时不会重复下单）。
- 幂等键生成：`crypto.randomUUID()` 或时间戳+随机数，**同一次提交动作共享一个 key**（重试沿用、重新提交换新）。
- 锁的释放时机：请求 settle（成功或失败都释放）；失败后允许重试但换新幂等键（或按业务沿用）。
- 结合 AbortController：防重提交 hook 可以在组件卸载时取消请求，但对"已发出且服务端可能处理"的请求，幂等键才是最终防线。

```javascript
// 简化实现，帮助理解防重提交
import { useRef, useState, useCallback } from 'react';

function useSubmit(submitFn, { idempotent = true } = {}) {
  const [loading, setLoading] = useState(false);
  const idempotencyKeyRef = useRef(null);

  const run = useCallback(async (...args) => {
    if (loading) return { ok: false, reason: 'pending' };   // 1. 锁：进行中拒绝
    setLoading(true);
    // 2. 幂等键：本次提交动作生成，重试沿用
    if (idempotencyKeyRef.current == null) {
      idempotencyKeyRef.current = crypto.randomUUID?.() ?? `${Date.now()}-${Math.random()}`;
    }
    try {
      const result = await submitFn(...args, {
        'Idempotency-Key': idempotencyKeyRef.current,       // 3. 服务端按 key 去重
      });
      idempotencyKeyRef.current = null;                     // 成功：key 使命完成
      return { ok: true, result };
    } catch (e) {
      // 失败：保留 key？业务决定——网络超时不确定服务端是否处理，重试沿用 key 最安全
      return { ok: false, error: e };
    } finally {
      setLoading(false);                                    // 4. settle：锁释放
    }
  }, [loading, submitFn]);

  return { run, loading };
}

// 表单层组合：
// function OrderForm() {
//   const { run, loading } = useSubmit(createOrder);
//   return (
//     <button disabled={loading} onClick={() => run(payload)}>
//       {loading ? '提交中...' : '提交订单'}
//     </button>
//   );
// }
// async function createOrder(body, headers) {
//   const res = await fetch('/api/order', { method: 'POST', headers, body: JSON.stringify(body) });
//   if (!res.ok) throw new Error('提交失败');
//   return res.json();
// }

// 双击攻击面分析：
// 双击瞬间：第二次 run 被 loading 锁拦截（React 批处理下 loading 已更新）✓
// 极端情况（loading 状态尚未生效的渲染间隙）+ 用户重试：
//   服务端拿到同一 Idempotency-Key -> 返回第一次的结果，不重复建单 —— 幂等键兜底 ✓
```
