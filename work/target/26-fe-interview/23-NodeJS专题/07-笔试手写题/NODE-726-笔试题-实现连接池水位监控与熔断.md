---
title: [NODE-726] 笔试题——实现连接池水位监控与耗尽熔断？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 笔试题
---

## NODE-726：手写连接池监控

**需求与边界**：
- 需求：连接池（SCN-NODE-639）——① 水位遥测（using/waiting/acquired——SCN-NODE-639 监控）；② 耗尽熔断（waiting 超阈值 → 临时切换「快速失败」模式——自动降级，SCN-NODE-690）；③ 泄漏检测（借出 >30s 未还——标记泄漏 + 堆栈记录）。
- 边界：① 借出栈跟踪（acquire 时 captureStack——泄漏定位到代码行）；② 熔断恢复（水位回落自动恢复正常模式）；③ 泄漏告警去重（同一调用点一次）。

**答**：
```javascript
class MonitoredPool {
  constructor(pool) { this.pool = pool; this.leased = new Map(); }
  async acquire(stack = captureStack()) {
    const conn = await this.pool.acquire();
    this.leased.set(conn, { since: Date.now(), stack });   // 借出跟踪（泄漏定位）
    if (this.waiting > threshold) breaker.open('POOL_EXHAUSTED');   // 耗尽熔断
    return conn;
  }
  release(conn) {
    this.leased.delete(conn); this.pool.release(conn);
    if (breaker.isOpen && this.waiting === 0) breaker.close();   // 水位回落恢复
  }
  leakCheck() {                                        // 定期：借出 >30s 未还
    for (const [conn, l] of this.leased)
      if (Date.now() - l.since > 30_000 && !dedup(l.stack))
        alert({ type: 'CONN_LEAK', heldMs: Date.now() - l.since,
          stack: l.stack });                          // 堆栈定位（SCN-NODE-639 finally 归还漏点）
  }
}
setInterval(() => pool.leakCheck(), 10_000);
```

**评分点**:
- 水位遥测 + 耗尽熔断自动降级（SCN-NODE-690 降级标记）。
- 借出栈跟踪（泄漏定位到代码行——不只在结果上猜）。
- 泄漏告警去重（同一调用点一次——告警风暴防御）。
- 水位回落自动恢复（熔断双向——SCN-NODE-669 half-open 语义）。
