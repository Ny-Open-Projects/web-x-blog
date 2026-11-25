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
    if (!navigator.sendBeacon?.(this.ctx.config.dsn, body))          // sendBeacon 失败返回 false，需显式回退
      fetch(this.ctx.config.dsn, { method: 'POST', body, keepalive: true });   // 页面卸载也不丢
  };
}
```

**追问**：

1. sendBeacon 有 64KB 上限且不能自定义 header，批量超了怎么办？ → 按体积切批并压缩，超限降级 fetch 加 keepalive，仍失败就落本地缓存下次补发，不能静默丢弃。
2. SDK 自己抛错把宿主搞白屏，怎么保证永不伤害宿主？ → 所有入口包 try/catch，全局 error 监听里先判断是否来自 SDK 栈并直接忽略，初始化异步执行，避免在宿主主流程里同步跑逻辑。
3. 采样率 10% 时错误总数怎么还原，低频的严重错误会不会被采没？ → 错误类事件全量不采样，性能类按采样上报 sampleRate 供后端加权还原，致命等级单独走全量通道。
