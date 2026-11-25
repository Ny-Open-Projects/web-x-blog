---
title: [1116] 笔试手写：实现 乐观操作 pending 超时守卫
date: 2026-11-22
categories: [状态管理新范式]
tags: [前端面试, 笔试题, 乐观更新]
type: 笔试题
---

## 1116：笔试手写：实现 乐观操作 pending 超时守卫

**答**：实现 createPendingGuard({ timeoutMs, onExpire })。begin(opId) 登记 pending 操作；resolve(opId) 正常完成移除；超时未 resolve 的 op 触发 onExpire(opId)（提示用户确认状态）并移除。guard.stats() 输出 pending 数与最老 pending 年龄。重复 begin 同 id 报错。

```js
function createPendingGuard({ timeoutMs, onExpire }) {
  const pend = new Map(); // opId -> { timer, startedAt }
  return {
    begin(opId) {
      if (pend.has(opId)) throw new Error(`duplicate pending: ${opId}`);
      const timer = setTimeout(() => {
        pend.delete(opId);
        onExpire?.(opId); // 超时：乐观态悬挂，需人工对账
      }, timeoutMs);
      pend.set(opId, { timer, startedAt: Date.now() });
    },
    resolve(opId) {
      const p = pend.get(opId);
      if (!p) return false;
      clearTimeout(p.timer);
      pend.delete(opId);
      return true;
    },
    stats(now = Date.now()) {
      let oldest = 0;
      pend.forEach(p => { oldest = Math.max(oldest, now - p.startedAt); });
      return { pending: pend.size, oldestMs: oldest };
    },
  };
}
```

**评分点**：
- begin/resolve 的定时器配对（泄漏 = 定时器未清）
- 重复 begin 抛错（幂等性问题提前暴露）
- stats 输出最老 pending（监控挂起积压）
- 能讨论：onExpire 后的处置——乐观 UI 回滚还是保持并提示（取决于操作可否安全重试）
