---
title: [AGT-486] 笔试题——实现会话服务容灾（主备切换+降级链+数据不丢）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-486：手写容灾：会话双写、主备切换、降级只读模式、数据核对

**需求与边界**：
- 输入：主备存储、健康探测；输出：容灾管理器。
- 边界要求：① 会话双写（主成功才算写成功，备异步追）；② 主故障自动切备（切换事件告警）；③ 双写不一致核对任务（定期 diff 修复）；④ 极端降级：只读模式（保数据不保写入）。

**答**：
```javascript
class SessionHA {
  constructor({ primary, replica, probe }) {
    this.primary = primary; this.replica = replica;
    this.state = 'primary'; this.queue = [];      // 切换期间积压写
    probe.onDown('primary', () => this.failover());
  }
  async append(convId, msg) {
    if (this.state === 'readonly')
      return { degraded: true, queued: true,
        note: '系统维护中，您的消息已暂存' };    // 极端降级：暂存
    const r = await this.primary.append(convId, msg);
    // 备异步追（不阻塞主写）
    this.replica.append(convId, msg)
      .catch(e => this.replLog.push({ convId, msg, e }));
    return r;
  }
  async failover() {
    this.state = 'replica';                      // 主→备
    alert('FAILOVER', { to: 'replica' });
    await this.flushPending();                   // 积压写追到备
    scheduleReconcile();                         // 数据核对任务
  }
  async reconcile() {                             // 主备 diff 修复
    const diffs = await diffStores(this.primary, this.replica);
    for (const d of diffs)
      await this.replica[d.action](d);            // 以主为准修复备
    return { fixed: diffs.length };
  }
  async flushPending() {
    while (this.queue.length)
      await this.replica.append(...this.queue.shift());
  }
  // 恢复：主修复后反向同步备→主，切回 primary。
}
```

**评分点**:
- 主写成功才算写成功、备异步追（延迟与一致性平衡）。
- 故障切换事件告警+积压写 flush。
- 主备 diff 核对修复任务（最终一致性保障）。
- 极端降级只读暂存模式（数据不丢优先于写入可用）。
