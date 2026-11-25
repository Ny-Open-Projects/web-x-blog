---
title: [WCN-255] computed 抛错时依赖图如何传播与恢复？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-255：computed 抛错时依赖图如何传播与恢复？
**答**：
- 错误沿依赖链上抛到 effect；effect 层决定处理（try/catch/错误信号）。
- 错误状态缓存：出错的 computed 记录 error，下次读取重算（可重试）——不是永久失败。
- 部分失败：链路中某分支出错不影响独立分支（每个 computed 独立缓存错误）。
- 恢复：写入新值触发重算，错误态自动清除——订阅者收到恢复后的值。

```javascript
class Computed {
  value = undefined; error = null;
  recompute() {
    try { this.value = this.fn(); this.error = null; }
    catch (e) { this.error = e; throw e; }   // 上抛给订阅 effect
  }
}
// 订阅侧：effect(() => { try { show(data.value); } catch { showError(); } })
r
```
