---
title: [NODE-672] 内存泄漏定位（heap 快照对比）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-672：内存泄漏怎么定位？
**答**：
- 确认泄漏：heapUsed 随时间单调增长且 GC 后不回落（多轮 GC 后基线抬升——真泄漏）；区分堆内 vs 堆外（Buffer——rss 涨 heapUsed 平，SCN-NODE-635 三指标）。
- 快照对比法：load 前后两份 heap snapshot → diff 增长对象 → retained size 排序 → 持有链（retainers）定位到代码——对比对象数量增长（不只 size——数量增长是泄漏特征）。
- 常见 Node 泄漏源：全局 Map/数组无清理（缓存无上限）、事件监听器未移除（listener 泄漏——MaxListeners 警告）、闭包捕获大对象、定时器未清理、模块级缓存（SCN-BLD-253 同源）。
- 生产取证：kill -USR2 触发 heapdump（摘流实例——SCN-NODE-671）+ 快照文件下载分析（Chrome DevTools 加载）。
- 追问钩子：为什么「GC 后不回落」比「heapUsed 涨」更准——正常服务的 heapUsed 有涨有落（GC 周期）；强制 full GC（global.gc with --expose-gc）后基线不回落 = 存在「GC 无法回收的存活引用」——这才是泄漏的定义；只看增长曲线会误判「工作集大」为泄漏。

```javascript
// 泄漏确认：强制 GC 后基线
if (global.gc) { global.gc(); global.gc();
  telemetry.push({ heapAfterFullGC: process.memoryUsage().heapUsed });   // 多次采样基线不降 = 泄漏
}
// 快照对比
process.kill(process.pid, 'USR2');                     // heapdump
// 常见泄漏自查
listenerCount(process, 'myEvent') > 20 && warn('listener 泄漏？');
```
