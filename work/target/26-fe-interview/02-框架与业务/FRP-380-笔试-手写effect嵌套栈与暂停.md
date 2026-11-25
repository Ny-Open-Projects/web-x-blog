---
title: [FRP-380] 笔试：手写 effect 嵌套栈与暂停（Activity 语义）
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## FRP-380：笔试：手写 effect 暂停

**答**：扩展 effect 支持 Activity 语义：① `effect(fn)` 返回 { pause, resume, stop }；② pause：停止订阅（清 deps）——期间依赖变化不触发；③ resume：重跑一次（重新收集依赖——暂停期间依赖集合可能变化）；④ stop：永久停止（不可 resume）；⑤ 嵌套：父 effect pause 不影响子 effect 独立控制（栈结构）；⑥ cleanup 语义（每次 run 前跑上次的清理）。写出实现。

```javascript
function createEffect(fn, { name = 'effect' } = {}) {
  let deps = new Set(), disposed = false, paused = false, cleanup = null;
  const e = {
    name, get paused() { return paused; },
    run() {
      if (disposed || paused) return;
      cleanup?.();                                    // 上次清理
      cleanupEffectDeps(e);                           // 清旧依赖
      stack.push(active); active = e;
      try { cleanup = fn(); }                         // 新依赖收集 + 新清理
      finally { active = stack.pop(); }
    },
    pause() { paused = true; cleanupEffectDeps(e); cleanup?.(); cleanup = null; },  // 摘依赖
    resume() { if (disposed) return; paused = false; e.run(); },  // 重跑重收集
    stop() { disposed = true; cleanupEffectDeps(e); cleanup?.(); cleanup = null; },
  };
  e.run();
  return e;
}
function cleanupEffectDeps(e) { for (const subs of e.deps) subs.delete(e); e.deps.clear(); }

// 用法: Activity 隐藏
const e = createEffect(() => subscribeTicker(render));
panel.hidden ? e.pause() : e.resume();   // 隐藏: 停订阅(依赖变化不触发); 显示: 重跑
// 语义对照: React Activity hidden = pause (不卸载, effect 挂起)
```

**评分点**：
- pause = 摘依赖（不触发但状态保留）
- resume = 重跑重收集（暂停期间依赖变化能重新连上）
- cleanup 在 run 前/ pause 时执行的一致性
- 嵌套栈（active 指针）与父子的独立控制
