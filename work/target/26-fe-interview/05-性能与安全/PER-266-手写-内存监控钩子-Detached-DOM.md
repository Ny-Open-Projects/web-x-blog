---
title: [PER-266] 笔试题：手写"组件卸载后 DOM 是否被释放"的检测器（定期 GC + detached 节点统计）
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-266：手写"组件卸载后 DOM 是否被释放"的检测器（定期 GC + detached 节点统计）

**题目**：实现 `trackDetached(intervalMs = 30000)`：① 用 MutationObserver 记录"从文档移除"的节点（弱引用保存，避免检测器自己制造泄漏）；② 每 intervalMs 检查这些节点是否仍可被 JS 访问到（用 performance.memory 变化不可靠，改用 WeakRef 弱引用判断对象存活）；③ 输出仍存活的 detached 节点数与最近 N 个节点描述；④ 页面 hidden 时停止检查，恢复时重启。

**答**：核心技巧是 WeakRef：如果卸载的组件被泄漏引用持有，WeakRef.deref() 返回对象本身（还活着）；正常 GC 掉了返回 undefined。这是运行时（而非堆快照）检测 detached 泄漏的标准姿势。

```javascript
function trackDetached(intervalMs = 30000) {
  const watch = new Set();                     // WeakRef 集合
  const mo = new MutationObserver((muts) => {
    for (const m of muts) for (const n of m.removedNodes) {
      if (n.nodeType === 1) watch.add(new WeakRef(n));
    }
  });
  mo.observe(document.body, { childList: true, subtree: true });

  function check() {
    if (document.visibilityState !== 'visible') return;
    const alive = [];
    for (const ref of [...watch]) {
      const el = ref.deref();
      if (!el) { watch.delete(ref); continue; }          // 已被 GC，正常
      if (!el.isConnected) {                             // detached 且仍存活 => 疑似泄漏
        alive.push(el.tagName + (el.className ? '.' + String(el.className).split(' ')[0] : ''));
      } else watch.delete(ref);                          // 又挂回去了
    }
    if (alive.length > 20) {                             // 阈值告警
      console.warn(`疑似 detached 泄漏 ${alive.length} 个`, alive.slice(0, 10));
      report({ type: 'detached-leak', count: alive.length, samples: alive.slice(0, 10) });
    }
  }
  const timer = setInterval(check, intervalMs);
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden') clearInterval(timer);
    else { timer && clearInterval(timer); setInterval(check, intervalMs); }
  });
  return { check };
}
// 注意：检测器只用 WeakRef 弱引用，不会阻止 GC——否则检测器自己就是泄漏源
```

**评分点**：
- 用 WeakRef 而非直接引用保存节点（直接引用会让检测器自己制造泄漏，一票否决点）。
- MutationObserver 只记 removedNodes 且过滤 nodeType === 1。
- alive 判定逻辑：deref() 存活 + isConnected 为 false 才算疑似泄漏。
- 定时器随可见性启停；有阈值告警而非每 30s 噪音。
