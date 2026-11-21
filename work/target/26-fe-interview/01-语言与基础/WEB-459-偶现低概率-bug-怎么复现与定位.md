---
title: [WEB-459] 偶现（低概率）bug 怎么复现与定位
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-459：偶现（低概率）bug 怎么复现与定位

**答**：
- 第一步不是复现，是收证：确认版本/环境/用户特征（机型、网络、灰度桶），从报障工单里找共性
- 建立黑盒录制：接 rrweb/录屏 SDK，用户报障时回放操作流，比口头描述快一个数量级
- 增强日志：把上报从「只有 error」升级为「error + 最近 N 条行为事件 + 关键状态快照」，偶现问题本质是状态机竞态，状态序列比堆栈有用
- 复现技巧：用 Chaos 手段放大概率——CPU 4x throttle、Slow 3G、随机延迟注入异步链路；竞态类问题压测并发就能稳定复现
- 闭环：修完后保留「问题指纹」（特征码/堆栈哈希）做监控哨兵，同类再犯立刻告警

```javascript
// 报障时携带最近行为序列
const trail = [];
const wrap = (type) => addEventListener(type, e => trail.push({ t: Date.now(), type, x: e.target?.id }), true);
['click','input','visibilitychange'].forEach(wrap);
window.onerror = (msg) => report({ msg, trail: trail.slice(-30) });
```
