---
title: [AGT-538] 手写会话同步：oplog 追加、rev 幂等、跨端提示、409 冲突重放？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-538：手写会话同步：oplog 追加、rev 幂等、跨端提示、409 冲突重放

**需求与边界**：
- 输入：本地会话状态 + WS 推送的 op 流（append/update/delete，带 rev/deviceId）与 API 的 ifMatch 乐观锁。
- 边界要求：① rev ≤ 本地 rev 的事件幂等丢弃；② 他端 append 触发提示不静默；③ 删除等写操作 409 时刷新后重放；④ op 应用必须幂等（同一 op 重复应用结果不变）。

**答**：
```javascript
class SessionSync {
  constructor(session, myDevice) {
    this.s = session; this.rev = session.rev;
    this.myDevice = myDevice; this.pending = [];
  }
  onRemote({ rev, deviceId, op }) {
    if (rev <= this.rev) return;                    // 幂等：过期事件
    this.rev = rev;
    this.apply(op);
    if (op.type === 'append' && deviceId !== this.myDevice)
      ui.banner('另一设备上有一条新消息');            // 跨端提示
  }
  apply(op) {                                       // 幂等应用
    if (op.type === 'append') {
      if (!this.s.messages.some(m => m.id === op.msg.id))
        this.s.messages.push(op.msg);               // 已存在则跳过
    } else if (op.type === 'update') {
      const m = this.s.messages.find(m => m.id === op.msg.id);
      if (m && m.rev < op.msg.rev) Object.assign(m, op.msg);
    } else if (op.type === 'delete') {
      this.s.messages = this.s.messages.filter(m => m.id !== op.id);
    }
  }
  async mutate(fn) {                                // 本地写：乐观锁
    const nextRev = this.rev + 1;
    try { await api.patch(this.s.id, { ifMatch: this.rev, op: fn.op() });
      this.rev = nextRev;
    } catch (e) {
      if (e.status === 409) { await this.refresh(); this.mutate(fn); } // 重放
      else throw e;
    }
  }
  async refresh() { const s = await api.get(this.s.id);
    this.s = s; this.rev = s.rev; }
}
```

**评分点**:
- rev 单调判重保证事件幂等；apply 对 append/update 各自幂等（存在检查/rev 比较）。
- 跨端 append 用提示而非静默合并（多端体验关键）。
- 409 冲突走 refresh + 重放（乐观锁标准姿势），写操作带 ifMatch。

