---
title: [WCN-639] 笔试：实现带取消与竞态防护的 effect（支持 onCleanup + epoch + 错误边界）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-639：笔试：实现带取消与竞态防护的 effect（支持 onCleanup + epoch + 错误边界）

**答**：
- 需求：实现 safeEffect(fn)：fn 接收 (signalGet, onCleanup)；每次重跑前清理旧副作用；用 epoch 丢弃过期异步回调；fn 抛错不中断其他 effect 并上报。
- 思路：闭包持 epoch 与 cleanup；run 时 cleanup + epoch++；异步回调校验 epoch；try/catch 包裹 fn。
- 边界：清理函数本身抛错要吞掉；重复 dispose 幂等；错误上报不阻塞。

```javascript
const allEffects = new Set();
export function safeEffect(fn) {
  let epoch = 0, cleanup = null, disposed = false;
  function run() {
    if (disposed) return;
    try { cleanup?.(); } catch (e) { console.warn('cleanup err', e); }
    const cur = ++epoch;
    const onCleanup = f => { cleanup = f; };
    try {
      fn((sig) => sig.get(), onCleanup, () => cur === epoch && !disposed);
    } catch (e) {
      reportError(e); // 错误边界：不影响其他 effect
    }
  }
  allEffects.add(run);
  run();
  return () => {
    if (disposed) return;
    disposed = true;
    try { cleanup?.(); } catch {}
    allEffects.delete(run);
  };
}
function reportError(e) { console.error('[effect]', e); }
```

**评分点**：
- 重跑前先执行旧 cleanup，且清理函数抛错被吞掉。
- epoch/isActive 守卫丢弃过期异步回调（竞态防护）。
- fn 抛错被 try/catch 捕获并上报，不影响其他 effect。
- 返回的 dispose 幂等（重复调用安全）。
