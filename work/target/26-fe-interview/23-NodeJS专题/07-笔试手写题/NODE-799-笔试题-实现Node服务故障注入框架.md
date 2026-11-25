---
title: [NODE-799] 笔试题——实现 Node 服务故障注入框架（延迟/错误/资源）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-799：手写故障注入

**需求与边界**：
- 需求：故障注入框架（SCN-OPS-281）——① 注入类型（延迟/错误率/超时/连接拒绝——按下游声明）；② 注入范围（按百分比流量——灰度标记联动，SCN-NODE-670）；③ 自动清理（注入窗口结束恢复现场——SCN-OPS-281 纪律）；④ 观察指标声明（注入生效验证——SCN-OPS-281 可观测性）。
- 边界：① 注入器的开关安全（紧急停止——一键清除全部注入）；② 注入的生效验证（延迟注入后 P99 上升——验证生效）；③ 注入与压测标记共存（压测流量单独注入——SCN-NODE-717 隔离）。

**答**：
```javascript
class FaultInjector {
  constructor() { this.active = new Map(); }           // 注入 → { config, expireAt }
  inject({ target, type, value, pct = 100, windowMs = 60_000, observe }) {
    const cfg = { type, value, pct, expireAt: Date.now() + windowMs, observe };
    this.active.set(target, cfg);
    scheduleCleanup(cfg);                              // 自动清理（SCN-OPS-281）
  }
  wrap(call, target) {                                 // 调用包装：注入生效点
    const cfg = this.active.get(target);
    if (!cfg || Math.random() * 100 > cfg.pct) return call();
    if (cfg.type === 'latency') return sleep(cfg.value).then(call);
    if (cfg.type === 'error') return Promise.reject(new Error('INJECTED'));
    if (cfg.type === 'timeout') return Promise.race([call(), sleep(cfg.value)]);
    if (cfg.type === 'reject') return Promise.reject(new Error('CONN_REFUSED'));
  }
  emergencyStop() { this.active.clear(); }             // 紧急停止（一键清除）
  verify() {                                           // 注入生效验证（SCN-OPS-281）
    return this.active.size ? metrics.check(cfg.observe) : { noop: true };
  }
}
// 用法：注入 DB 延迟 500ms 100% 流量 60s，观察 P99 上升
injector.inject({ target: 'db', type: 'latency', value: 500, windowMs: 60_000,
  observe: { metric: 'p99', expect: '> +500ms' } });
```

**评分点**:
- 四类注入（延迟/错误/超时/拒绝）+ 百分比流量控制。
- 自动清理（窗口结束恢复现场——SCN-OPS-281 纪律）。
- 生效验证（observe 声明——注入失效的演练无效）。
- 紧急停止（一键清除——演练失控兜底）。
