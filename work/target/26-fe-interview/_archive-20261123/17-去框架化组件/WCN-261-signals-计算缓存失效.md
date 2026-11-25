---
title: [WCN-261] computed 的缓存失效粒度（版本号 vs 脏标记）性能对比？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-261：computed 的缓存失效粒度（版本号 vs 脏标记）性能对比？
**答**：
- 版本号：全局 epoch，读取时比对依赖版本——O(依赖数) 验证，无栈依赖问题。
- 脏标记：写时传播 dirty——写入开销大（传播广）读取便宜。
- 混合：写时只标「直接订阅者」dirty，读取时惰性传播（Preact Signals 折中）。
- 选择依据：写多读少用惰性（传播窄），读多用版本验证。

```javascript
// 惰性传播：写只标直接订阅者
function set(sig, v) {
  sig.value = v; sig.epoch = ++globalEpoch;
  for (const s of sig.subs) s.dirty = true;    // 只标一层
}
// computed 读取时验证依赖版本，必要时向上传播
r
```
