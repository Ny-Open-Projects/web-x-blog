---
title: [NODE-466] Node 服务的句柄/定时器/监听器泄漏防护如何工程化？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-466：句柄与监听器泄漏防护工程化
**答**:
- 泄漏面：定时器未清、监听器未移除（EventEmitter MaxListeners 警告）、流未关闭（fd 泄漏）、子进程未回收、全局 Map 增长（NODE-349 的工程化预防——不只靠事后排查）。
- 防护设施：资源管理器封装（acquire/release 配对 API：openTimeout 返回句柄对象，destroy 统一清理；未配对在进程退出时告警清单）、lint 规则（setInterval/setTimeout 必须保存引用 + 注明清理点——人工 review 辅助）、运行时巡检（定时对比句柄数趋势：lsof fd 数/GC 后对象数，增长告警）。
- 测试集成：泄漏回归测试（跑 N 次操作 → 断言句柄/监听器计数回落到基线——CI 内存测试 NODE-349）、压力后快照对比。
- 常见模式修复：请求级资源用 ALS 生命周期统一清理（NODE-421/422：请求结束统一 abort/destroy）、常驻定时器注册表（可列举/可测试）。
- 生产兜底：定期滚动重启（低峰期，防未知泄漏累积——兜底不是不修）。
```javascript
// 资源管理器：配对与泄漏检测
const tracker = new ResourceTracker();
function trackedTimeout(fn, ms, label) {
  const t = setTimeout(fn, ms);
  tracker.add('timer', label, () => clearTimeout(t));
  return () => { clearTimeout(t); tracker.release(label); };
}
setInterval(() => { const leaked = tracker.snapshot();          // 巡检
  if (leaked.count > baseline * 2) alert('疑似泄漏', leaked.top); }, 60e3);
```
