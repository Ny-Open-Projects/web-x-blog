---
title: [SCN-458] 笔试题——实现工单 SLA 倒计时（多级预警/自动升级/暂停）？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-458：手写工单 SLA：响应/解决双 SLA、临近预警、超时自动升级

**需求与边界**：
- 输入：工单（优先级→SLA 配置）、状态变更；输出：SLA 计时与升级。
- 边界要求：① 双 SLA（响应/解决）分别计时；② 临近超时分级预警（80% 变色/超时升级）；③ 挂起态 SLA 暂停（等客户回复不计）；④ 超时自动升级到主管并通知。

**答**：
```javascript
class SlaTimer {
  constructor(ticket, { config }) {
    this.cfg = config[ticket.priority];       // P0 30min / P1 2h ...
    this.paused = false;
    this.elaspedMs = 0;
    this.tick();
  }
  tick() {
    setInterval(() => {
      if (this.paused) return;                // 挂起暂停计时
      this.elaspedMs += 1000;
      const ratio = this.elaspedMs / this.cfg.solveMs;
      if (ratio >= 1) this.escalate();
      else if (ratio >= 0.8) warn(ticket, '80%');  // 预警变色
    }, 1000);
  }
  pause() { this.paused = true; }             // 待客户回复挂起
  resume() { this.paused = false; }
  escalate() {
    clearInterval(this.timer);
    ticket.assignTo(supervisor);              // 自动升级
    notify({ type: 'sla_breach', ticket, level: 'critical' });
    audit.log({ type: 'SLA_BREACH', ticket }); // 审计
  }
}
// 响应 SLA：首条回复后停止；解决 SLA：解决态后停止；
// 双计时独立（一个超即预警）。
```

**评分点**:
- 双 SLA（响应/解决）独立计时，优先级差异化配置。
- 分级预警（80% 变色/超时升级）+挂起暂停（等客户不计）。
- 超时自动升级+审计留痕。
- 计时与状态机联动（解决态停止）。
