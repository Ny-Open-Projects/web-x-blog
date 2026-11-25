---
title: [PER-365] 监控 SDK 的插件化架构设计：核心小、插件懒加载、插件间通信与故障隔离？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-365：监控 SDK 的插件化架构设计：核心小、插件懒加载、插件间通信与故障隔离？

**答**：
- 架构分层：核心（vitals 采集 + 队列上报 + 生命周期，gzip ≤ 5KB）+ 插件（LoAF 归因、资源拆解、错误采集、行为埋点、自定义指标）按需加载。核心暴露 hooks（onEvent/subscribe），插件注册消费，彼此不直接依赖。
- 懒加载策略：插件随核心一起发但延迟初始化（idle 时 init），或独立 chunk 按配置拉取；插件配置由服务端下发（开关+采样率，无需发版调整采集面）。
- 故障隔离：每个插件 init/回调包 try-catch，插件挂了不影响核心与其他插件（监控 SDK 自己崩溃是最恶劣故障）；插件超时 watchdog（init 超过 3s 强制禁用并上报）。
- 插件间通信：事件总线（核心发 'vital'/'error'/'resource' 事件，插件订阅）——松耦合让插件可独立测试与移除。
- 度量：核心体积、各插件体积、init 耗时、插件错误率——SDK 自身的可观测（PER-246）。

```javascript
// 插件化核心骨架
class MonitorCore {
  constructor() { this.hooks = new Map(); this.plugins = new Set(); }
  on(name, fn) { (this.hooks.get(name) ?? this.hooks.set(name, []).get(name)).push(fn); return () => this.off(name, fn); }
  emit(name, payload) { for (const fn of this.hooks.get(name) || []) { try { fn(payload); } catch (e) { console.error(`[plugin] ${name}`, e); this.report?.({ type: 'plugin-error', hook: name, msg: String(e) }); } } }
  use(plugin, { lazy = true } = {}) {
    const init = () => { try { plugin.setup(this); this.plugins.add(plugin.name); }
      catch (e) { this.emit('internal-error', { plugin: plugin.name, error: e }); } };
    lazy ? (window.requestIdleCallback || setTimeout)(init, { timeout: 3000 }) : init();
  }
}
// 插件示例：LoAF 归因插件
const loafPlugin = { name: 'loaf', setup(core) {
  new PerformanceObserver((l) => core.emit('long-frame', l.getEntries())).observe({ type: 'long-animation-frame', buffered: true });
} };
// 核心队列插件消费事件后批量上报；插件独立、可按配置移除 —— 核心永不因插件崩溃
```
