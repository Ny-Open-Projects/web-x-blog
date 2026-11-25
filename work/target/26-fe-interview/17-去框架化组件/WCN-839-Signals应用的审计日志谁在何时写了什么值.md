---
title: [WCN-839] Signals 应用的「审计日志」：谁在何时写了什么值，怎么做？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-839：Signals 应用的「审计日志」：谁在何时写了什么值，怎么做？

**答**：
- 结论先行：审计日志是「给 signal 写操作加一层可观测中间件」——在 set 入口拦截，记录 `{key, oldValue, newValue, source, timestamp, stack}`，用于调试"值为什么变了"与事后追责。
- 实现方式：封装 `createAuditedSignal`，在 set 时先写日志再更新；通过 `new Error().stack` 捕获调用栈定位「谁写的」；生产环境可采样或只记关键 signal，避免开销。
- 结构化信息：给每次写标注 source（用户操作/网络回调/定时器）与 actor（哪个模块/用户），便于聚合分析；配合「因果链」把 effect 触发的下游写也串起来。
- 与调试工具结合：审计日志是「时间旅行调试」的基础——有完整写序列就能回放状态；但要注意敏感值脱敏（别把密码记进日志）。
- 边界与成本：高频写（拖拽每帧）不能全量记，要采样/去重/合帧；日志存储有上限（环形缓冲），避免内存膨胀。
- 追问钩子：面试官会问「审计会不会影响性能」——答：开发态全量、生产态按需开启 + 采样 + 环形缓冲，把开销控制到可接受；关键是设计成可插拔中间件，不用时零成本。

```javascript
import { signal } from '@preact/signals-core';
function audited(key, initial, { sample = 1 } = {}) {
  const s = signal(initial);
  const log = [];                         // 环形缓冲（简化为数组）
  const rawSet = s.set.bind(s);
  s.set = (v, meta = {}) => {
    const old = s.value;
    if (Math.random() <= sample) {
      log.push({ key, old, value: v, source: meta.source || 'unknown',
        at: Date.now(), stack: new Error().stack?.split('\n')[2] });
      if (log.length > 100) log.shift();  // 上限，防膨胀
    }
    rawSet(v);
  };
  s.auditLog = log;
  return s;
}
const cart = audited('cartCount', 0);
cart.set(3, { source: 'add-to-cart' });
console.log(cart.auditLog); // 谁/何时/从旧值到新值
```
