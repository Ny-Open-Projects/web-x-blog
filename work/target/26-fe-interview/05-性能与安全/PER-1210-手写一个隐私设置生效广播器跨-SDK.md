---
title: [PER-1210] 手写一个隐私设置生效广播器：跨 SDK 协调
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1210：手写一个隐私设置生效广播器：跨 SDK 协调

**答**：
- 需求：实现 PrivacyBus。sdk 注册（name, hooks: { onGrant, onWithdraw }）；apply(consent) 遍历各 SDK：consent[bucket] 为 true 调 onGrant 否则 onWithdraw（未实现的 hook 跳过并记录 missing）；变更事件去重（同 consent 快照不重复广播）；rollback() 回滚到上一快照（调用反向 hook）。
- 边界：SDK 注册时立即同步当前快照；hook 抛错隔离（不影响其他 SDK）并记录；快照相同判定用 JSON 相等。
- 评分点：去重广播；hook 隔离；注册即同步；rollback

```javascript
class PrivacyBus {
  constructor() { this.sdks = new Map(); this.history = []; }
  register(name, hooks) {
    this.sdks.set(name, { hooks, missing: [] });
    if (this.current) this.#applyOne(name, hooks, this.current);
  }
  apply(consent) {
    const snap = JSON.stringify(consent);
    if (this.history[0]?.snap === snap) return;    // 去重
    this.history.unshift({ snap, consent });
    for (const [name, s] of this.sdks) this.#applyOne(name, s.hooks, consent);
    this.current = consent;
  }
  #applyOne(name, hooks, consent) {
    for (const [bucket, on] of Object.entries(consent)) {
      const hook = on ? hooks.onGrant : hooks.onWithdraw;
      if (!hook) { report({ type: 'hook-missing', sdk: name, bucket }); continue; }
      try { hook(bucket); } catch (e) {
        report({ type: 'hook-error', sdk: name, bucket, msg: e.message });
      }
    }
  }
  rollback() {
    if (this.history.length < 2) return;
    this.apply(this.history[1].consent);           // 回到上一快照
  }
}
```
