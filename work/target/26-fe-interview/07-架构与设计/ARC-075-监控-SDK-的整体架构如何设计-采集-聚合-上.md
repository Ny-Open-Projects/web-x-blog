---
title: [ARC-075] 监控 SDK 的整体架构如何设计（采集/聚合/上报/生命周期）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-075：监控 SDK 的整体架构如何设计（采集/聚合/上报/生命周期）？
**答**：
- 四段式管线：采集层（JS 错误/资源/接口/性能指标）→ 聚合层（采样、去重、合并、节流）→ 上报层（批量、失败重试、sendBeacon）→ 生命周期（init 配置、install 钩子、destroy 清理）。
- 核心原则：SDK 必须"永不伤害宿主"——自身异常静默降级、采集异步化、体积小、避免死循环（错误上报自身报错不再上报）。
- 可扩展性靠插件架构：采集器全是插件，核心只管调度。

```typescript
// 监控 SDK 骨架：插件化管线
interface MonitorPlugin {
  name: string;
  setup(ctx: MonitorContext): void;      // 注册采集钩子
  destroy?(): void;
}
interface MonitorContext {
  config: { dsn: string; sampleRate: number; app: string };
  capture(event: MonitorEvent): void;    // 插件唯一的对外出口
  on(event: 'beforeReport', hook: (e: MonitorEvent) => MonitorEvent | null): void;  // 全局过滤
}

class Monitor {
  private buffer: MonitorEvent[] = [];
  constructor(private ctx: MonitorContext) {}
  install(...plugins: MonitorPlugin[]) { plugins.forEach(p => { try { p.setup(this.ctx); } catch { /* 静默 */ } }); }

  capture = (e: MonitorEvent) => {
    if (Math.random() > this.ctx.config.sampleRate) return;         // 采样
    for (const hook of this.hooks) { e = hook(e); if (!e) return; } // 过滤（含防死循环：report 自身错误丢弃）
    this.buffer.push(e);
    if (this.buffer.length >= 10) this.flush();
  };
  flush = () => {
    const batch = this.buffer.splice(0);
    const body = JSON.stringify(batch);
    navigator.sendBeacon?.(this.ctx.config.dsn, body)               // 页面卸载也不丢
      ?? fetch(this.ctx.config.dsn, { method: 'POST', body, keepalive: true });
  };
}
```
