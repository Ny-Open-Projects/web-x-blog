---
title: [AGT-499] 笔试题——实现运行时资源泄漏防护（连接/定时器/沙箱的注册与回收）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-499：手写资源泄漏防护：资源注册表、任务结束统一回收、泄漏检测告警

**需求与边界**：
- 输入：任务生命周期（start/end）、资源创建动作；输出：资源守卫。
- 边界要求：① 资源注册（连接/定时器/沙箱/订阅统一登记）；② 任务结束（含异常/取消路径）统一回收；③ 泄漏检测（任务结束仍未释放的资源告警+强制回收）；④ 长任务周期性检查。

**答**：
```javascript
class ResourceGuard {
  constructor({ leakMs = 5 * 60e3 }) {
    this.resources = new Map();               // taskId → Set<handle>
    this.leakMs = leakMs;
    this.sweeper = setInterval(() => this.sweep(), 60e3);
  }
  register(taskId, kind, handle, release) {
    if (!this.resources.has(taskId))
      this.resources.set(taskId, new Set());
    const rec = { kind, handle, release, ts: Date.now() };
    this.resources.get(taskId).add(rec);
    return () => {                            // 手动释放（幂等）
      this.resources.get(taskId)?.delete(rec);
      release();
    };
  }
  // 包装创建动作：定时器/监听/连接自动登记
  guard(taskId, kind) {
    return {
      setTimeout: (fn, ms) => { const t = setTimeout(fn, ms);
        const rel = this.register(taskId, 'timer', t,
          () => clearTimeout(t)); return t; },
      on: (emitter, ev, fn) => { emitter.on(ev, fn);
        return this.register(taskId, 'listener', [emitter, ev],
          () => emitter.off(ev, fn)); },
      open: async (openFn, closeFn) => {
        const c = await openFn();             // 连接/沙箱
        this.register(taskId, kind, c, () => closeFn(c));
        return c; },
    };
  }
  async endTask(taskId) {                     // 任务结束统一回收
    const set = this.resources.get(taskId);
    if (!set) return { released: 0 };
    const n = set.size;
    for (const r of set) { try { r.release(); }
      catch (e) { alert('RELEASE_FAIL', { taskId, kind: r.kind }); } }
    this.resources.delete(taskId);
    return { released: n };
  }
  sweep() {                                   // 泄漏检测
    for (const [taskId, set] of this.resources) {
      for (const r of set)
        if (Date.now() - r.ts > this.leakMs && !this.alive(taskId))
          alert('LEAK_SUSPECTED', { taskId, kind: r.kind,
            age: Date.now() - r.ts });
    }
  }
  alive(taskId) { return this.running.has(taskId); }
  dispose() { clearInterval(this.sweeper); }
}
```

**评分点**:
- 资源注册表统一管理（定时器/监听/连接/沙箱四类），release 幂等。
- endTask 覆盖异常/取消路径统一回收（finally 语义）。
- 泄漏检测 sweep：任务已结束但资源未释放→告警+年龄信息。
- 包装 API（guard）让业务无感接入——治理基建易用性设计。
