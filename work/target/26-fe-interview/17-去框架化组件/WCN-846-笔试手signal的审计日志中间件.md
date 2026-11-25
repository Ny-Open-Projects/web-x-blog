---
title: [WCN-846] 笔试：手写 signal 的「审计日志」中间件（写操作记录 + 回放）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-846：笔试：手写 signal 的「审计日志」中间件（写操作记录 + 回放）

**题目**：实现 `withAudit(signalFactory, { capacity = 50, sample = 1 })`，返回一个增强的 signal 工厂，其创建的 signal 带审计能力。要求：① 每次 set 记录一条 `{ key, oldValue, newValue, timestamp, source, stack }` 到环形缓冲（容量 capacity，超出丢弃最旧）；② `sample`（0~1）控制采样率，未命中不记但仍更新值；③ signal 额外暴露 `getLog()` 返回日志副本、`replay(fn)` 按顺序用每条 newValue 调用 fn（回放）、`clearLog()`；④ 用 `new Error().stack` 捕获调用栈做「谁写的」归因；⑤ 写操作本身不能因日志失败而中断（try/catch）。边界：初始值不记日志；回放不改原 signal 值。

**答**：

```javascript
function withAudit(signalFactory, { capacity = 50, sample = 1 } = {}) {
  return function audited(key, initial) {
    const s = signalFactory(initial);
    const log = [];
    const rawSet = s.set.bind(s);
    s.set = (v, source = 'unknown') => {
      const old = s.get();
      try {
        if (Math.random() <= sample) {
          log.push({ key, oldValue: old, newValue: v, timestamp: Date.now(),
            source, stack: new Error().stack?.split('\n').slice(2, 5).join('\n') });
          if (log.length > capacity) log.shift();          // 环形缓冲
        }
      } catch { /* 日志失败不影响主流程 */ }
      rawSet(v);
    };
    s.getLog = () => log.slice();                          // 返回副本，防外部篡改
    s.replay = (fn) => log.forEach(e => fn(e.newValue, e)); // 回放不改原值
    s.clearLog = () => { log.length = 0; };
    return s;
  };
}

// 搭配最小 signal 工厂使用
const base = (init) => { let v = init; return { get: () => v, set(n) { v = n; } }; };
const audited = withAudit(base, { capacity: 3 });
const cart = audited('cartCount', 0);
cart.set(1, 'addBtn'); cart.set(2, 'api');
console.log(cart.getLog().map(e => `${e.key}:${e.oldValue}->${e.newValue} by ${e.source}`));
cart.replay(v => console.log('回放:', v));
```

**评分点**：
- 环形缓冲用 shift 控容量，避免内存无限增长（边界）。
- 采样只影响记录、不影响 set 主流程；日志 try/catch 隔离（健壮性）。
- getLog 返回副本、replay 不改原值（封装性）。
- 调用栈归因 + source 标注，能回答「谁写的」（业务价值）。
