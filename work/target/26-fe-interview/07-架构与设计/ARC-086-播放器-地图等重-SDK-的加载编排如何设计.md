---
title: [ARC-086] 播放器/地图等重 SDK 的加载编排如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-086：播放器/地图等重 SDK 的加载编排如何设计？
**答**：
- 问题：重 SDK（>1MB）+ 单例约束 + 竞态（多组件同时触发加载）。解法：Loader 编排器——单飞加载、全局单例、加载队列、超时与失败重试。
- 编排策略：路由预取（进入相关页面前 prefetch）、idle 预加载、交互触发即加载 + 骨架占位。
- 卸载纪律：页面级组件销毁不销毁全局单例（重建成本高），但要在 idle 时回收未使用的实例（LRU）。

```typescript
// 重 SDK 加载编排器：单飞 + 单例 + 超时 + 预取
class HeavySdkLoader<T> {
  private loading: Promise<T> | null = null;
  private instance: T | null = null;
  constructor(
    private load: () => Promise<T>,
    private opts: { timeout: number; init?: (i: T) => void } = { timeout: 15000 },
  ) {}
  get(): Promise<T> {
    if (this.instance) return Promise.resolve(this.instance);       // 单例复用
    this.loading ??= Promise.race([
      this.load().then(i => { this.opts.init?.(i); this.instance = i; this.loading = null; return i; }),
      new Promise<never>((_, rej) => setTimeout(() => { this.loading = null; rej(new Error('SDK 加载超时')); }, this.opts.timeout)),
    ]);
    return this.loading;                                            // 单飞：并发调用共享同一 Promise
  }
  preload() { this.get().catch(() => {}); }                          // 静默预取：失败不影响主流程
}
const mapLoader = new HeavySdkLoader(() => import(/* webpackChunkName: "amap" */ '@amap/amap-jsapi-loader').then(l => l.default({})));
router.beforeEach(to => { if (to.meta.usesMap) mapLoader.preload(); }); // 路由级预取
// 组件内：const AMap = await mapLoader.get(); 并发 10 个组件也只加载一次
```
