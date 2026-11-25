---
title: [HW-150] 手写跨标签页状态同步——BroadcastChannel 广播 + 存储事件兜底 + 冲突合并策略
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-150：手写跨标签页状态同步——BroadcastChannel 广播 + 存储事件兜底 + 冲突合并策略
**答**：多标签页状态一致（登录态/主题/购物车）：BroadcastChannel 主通道（同源实时广播）；storage 事件兜底（老浏览器/BC 不可用场景，storage 变化天然跨标签页）；合并策略——状态带版本号（最后写赢）或按 field 合并（冲突可感知的字段提示用户）。

```javascript
class TabSync {
  constructor(channel, initialState, { merge = 'lww' } = {}) {
    Object.assign(this, { state: initialState, version: 0, merge });
    this.bc = 'BroadcastChannel' in window ? new BroadcastChannel(channel) : null;
    if (this.bc) this.bc.onmessage = (e) => this.#apply(e.data);
    addEventListener('storage', (e) => {                 // 兜底：storage 跨标签页事件
      if (e.key === channel && e.newValue) this.#apply(JSON.parse(e.newValue));
    });
  }
  update(patch) {
    this.version++;
    if (this.merge === 'lww') this.state = { ...this.state, ...patch };   // 最后写赢
    this.#persist();
    this.bc?.postMessage({ version: this.version, patch });
  }
  #apply({ version, patch }) {
    if (version <= this.version) return;                 // 旧版本：忽略（防回退）
    this.version = version;
    this.state = { ...this.state, ...patch };
    this.#persist();
    this.subs?.forEach((f) => f(this.state));
  }
  #persist() { try { localStorage.setItem(this.channel ?? 'tab-sync', JSON.stringify({ version: this.version, patch: this.state })); } catch {} }
  subscribe(fn) { (this.subs ??= new Set()).add(fn); fn(this.state); return () => this.subs.delete(fn); }
}
// 场景：A 标签页退出登录 → B/C 标签页同步清态（PER-360 擦除广播）
// 合并策略：登录态/主题用 lww；购物车数量用 field 级合并（A 加 2 件 B 加 1 件 → 3 件，lww 会丢）
```

**评分点**：
- BroadcastChannel 主通道 + storage 事件兜底的双通道。
- 版本号防回退（旧广播不覆盖新状态）——本题核心。
- lww vs field 级合并的场景区分（购物车数量必须 field 合并）。
- subscribe 模式与持久化兜底。
