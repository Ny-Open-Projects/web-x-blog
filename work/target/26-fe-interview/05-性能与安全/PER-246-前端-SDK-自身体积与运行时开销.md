---
title: [PER-246] 监控 SDK 自己会不会拖慢页面？SDK 体积与运行时开销的预算怎么管？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-246：监控 SDK 自己会不会拖慢页面？SDK 体积与运行时开销的预算怎么管？

**答**：
- 会，而且常见：埋点 SDK 全局监听事件做埋点、同步序列化大对象、频繁 sendBeacon、在 handler 里做字符串处理——它自己就是那个 INP 元凶。业界目标：SDK gzip 后 ≤ 15KB，运行时 CPU 占用 < 1%。
- 设计约束：① 体积——按指标拆分包（核心 vitals 3KB + 可选插件懒加载）；② 运行时——所有 handler 被动化、埋点缓冲后批量上报（每 5s 或 20 条）、序列化做长度截断与循环引用保护；③ 观测——SDK 自身耗时上报（自己测自己），并对外暴露 debug 模式。
- 采样兜底：高流量站点默认开启采样（见 PER-243），低流量全量。
- 验收：SDK 上线前用性能基准页（固定交互脚本）跑 before/after 对比，INP/LCP 无显著退化才可发布。

```javascript
// 监控 SDK 的自我开销控制样板
const buffer = [];                        // ① 缓冲批量上报
function track(metric) {
  buffer.push({ ...metric, ts: Date.now() });
  if (buffer.length >= 20) flush();       // 满 20 条或定时触发
}
setInterval(() => buffer.length && flush(), 5000);
function flush() {                        // ② sendBeacon 失败静默丢弃（不做同步 fallback 重试）
  const batch = buffer.splice(0, buffer.length);
  navigator.sendBeacon?.('/rum/batch', JSON.stringify(batch));
}
// ③ 自监控：SDK 各阶段耗时上报
performance.mark('sdk-init-start');
init(); performance.mark('sdk-init-end');
performance.measure('sdk-init', 'sdk-init-start', 'sdk-init-end');
```

**追问**：

1. `sendBeacon` 失败静默丢弃，那关键错误也丢怎么办？ → 错误类走单独通道并允许 localStorage 暂存、下次启动重试，性能类才允许丢，否则线上首错永远丢在卸页那一刻。
2. 每 5s flush 一次，页面关闭时最后一批怎么保证发出？ → 监听 `visibilitychange` 与 `pagehide` 立即 flush，beacon 在卸载期仍可靠；不要用 unload 里同步 XHR 兜底，那会拖慢关闭。
3. 「SDK 自身 CPU < 1%」怎么测才不是自说自话？ → 固定基准页跑 before/after 的长任务与 INP 对比，SDK 自报耗时只能证明它自己那几行，证明不了对页面的真实影响。
