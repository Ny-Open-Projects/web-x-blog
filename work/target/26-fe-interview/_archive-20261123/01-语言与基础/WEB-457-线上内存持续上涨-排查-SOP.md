---
title: [WEB-457] 线上内存持续上涨的排查 SOP
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-457：线上内存持续上涨的排查 SOP

**答**：
- 先定性：用户报的「卡」是真内存泄漏还是单纯页面大？看 Chrome 任务管理器/Performance monitor 的 JS heap 是否「只涨不跌」
- 复现路径：锁定操作序列（如反复切换路由、上传大文件后返回），泄漏几乎都跟着固定操作链
- 三快照法：Heap snapshot 在「操作前/操作 10 次/操作 20 次」各拍一张，对比按 constructor 聚合，看哪类对象数量线性增长
- 定位引用链：选中增长对象看 Retainers，常见元凶：未清理的定时器/监听器、闭包捕获的大数组、被缓存 API 结果持有
- 上线兜底：`performance.memory` 采样上报 + 页面驻留时长与 heap 的曲线，超阈值时自动 reload 兜底并告警

```javascript
// 线上内存监控采样
setInterval(() => {
  const m = performance.memory;
  report({ used: m.usedJSHeapSize, limit: m.jsHeapSizeLimit, t: Date.now() });
}, 30000);
```
