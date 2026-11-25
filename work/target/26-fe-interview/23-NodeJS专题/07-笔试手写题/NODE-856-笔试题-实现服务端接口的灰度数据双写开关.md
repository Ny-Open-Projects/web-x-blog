---
title: [NODE-856] 笔试题——实现灰度数据双写开关（expand 阶段控制）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-856：手写双写开关

**需求与边界**：
- 需求：双写开关（SCN-OPS-331 expand）——① 双写开关（配置中心热更——SCN-NODE-663）；② 双写失败语义（旧列成功新列失败——容错策略：新列失败不阻断旧列——主从优先级）；③ 一致性监测（SCN-NODE-793 漂移检测联动）；④ 收敛后关闭双写（contract 阶段——SCN-OPS-331）。
- 边界：① 双写的性能开销（双写延迟——异步双写，SCN-NODE-653 outbox）；② 双写失败的重试队列（SCN-NODE-733）；③ 开关的状态机（off→dual→new-only——三阶段）。

**答**：
```javascript
class DualWriteSwitch {
  async write(entity, data) {
    const mode = config.get(`dualwrite:${entity}`);    // off/dual/new-only（SCN-OPS-331 三阶段）
    await db.old.write(entity, data);                  // 旧列总是写（主）
    if (mode === 'dual') {
      try { await db.new.write(entity, data); }        // 新列（SCN-OPS-331 expand）
      catch (e) { await retryQueue.add(entity, data); }   // 新列失败重试队列（不阻断主——主从优先级）
    }
    if (mode === 'new-only') await db.new.write(entity, data);   // contract 后只写新
  }
}
// 一致性监测联动（SCN-NODE-793）
driftMonitor.on('drift', ({ table, rate }) => {
  if (rate > 0.001) config.set(`dualwrite:${table}`, 'dual-only-verify');   // 漂移 → 暂停切换
});
```

**评分点**:
- 三阶段开关（off/dual/new-only——SCN-OPS-331）。
- 主从优先级（旧列失败阻断、新列失败重试——SCN-OPS-331 主数据语义）。
- 一致性监测联动（漂移暂停切换——SCN-NODE-793）。
- 热更开关（SCN-NODE-663）。
