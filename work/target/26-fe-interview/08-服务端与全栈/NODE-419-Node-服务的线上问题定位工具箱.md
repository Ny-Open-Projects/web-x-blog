---
title: [NODE-419] Node 服务的线上问题定位工具箱（不动代码的现场取证）有哪些？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-419：线上问题定位工具箱
**答**:
- 不重启取证的在线工具链：CPU 采样（inspector Profiler 短时采样 NODE-350）、堆快照（NODE-349）、GC 日志（--trace-gc 环境开关）、事件循环延迟实时值、进程指标（ps/uv 的句柄数）。
- 动态日志：运行时开 debug 日志（logger 级别热更 NODE-388）+ 定点埋点开关（特定接口的详细日志临时打开）——不用改代码发版。
- 请求回放：抓取问题请求（带参数摘要）→ 测试环境重放（复现后用调试器）；流量录制回放工具化。
- 进程级工具：node --inspect 桥接（临时端口 + 权限控制）、strace/lsof（系统层：fd 泄漏/网络连接异常）、内存/GC 的 continuous sampling（clinic）。
- 工具箱纪律：线上取证操作审计（谁在何时采样）、采样对性能的影响评估（短时低频）、高危操作（堆 dump）在灰度实例先行。
```javascript
// 在线取证入口（内部运维端口，鉴权）
ops.post('/ops/cpu-profile', async (req, res) => {
  audit(req.user, 'cpu-profile');                                // 取证审计
  const session = startInspector();
  session.post('Profiler.start');
  await delay(req.body.durationMs ?? 5000);
  session.post('Profiler.stop', (e, { profile }) => res.json(profile));
});
```
