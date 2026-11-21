---
title: [WEB-403] Memory 面板的 Three Snapshot 怎么用？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-403：Memory 面板的 Three Snapshot 怎么用？
**答**：
- 快照1（基线）→ 操作复现泄漏场景 → 快照2 → 再操作一次 → 快照3；对比 2 与 3 之间增长的对象（Delta）才是泄漏嫌疑。
- 关注：Detached DOM（已从树上摘下仍被引用）、增长率稳定的闭包/数组、String 大量重复（缓存未清理）。
- 技巧：用 Retainers 链找到"谁引用着它"，从引用链根部断开；Allocation instrumentation on timeline 直接看分配栈更直接。

```javascript
// 三快照对比操作
// 1. shot1 → open modal 2. shot2 → close+open again 3. shot3
// Delta 上升: Detached HTMLDivElement × N → 找 Retainer: timer/闭包
const fix = () => { clearInterval(timer); el = null; listener.remove(); };
console.log('Detached 节点数随操作递增 = 典型泄漏');
```
