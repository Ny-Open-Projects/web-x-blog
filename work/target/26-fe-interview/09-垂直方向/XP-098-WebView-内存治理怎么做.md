---
title: [XP-098] WebView 内存治理怎么做？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-098：WebView 内存治理怎么做？
**答**：
- 认清规模：单个 WebView 进程常驻 50-150MB，多实例并存是 App OOM 主因之一；治理目标——**实例数上限、单实例瘦身、及时回收**三管齐下。
- 池化管理：WebView 池有上限（低端机 1-2 个，旗舰 3-4 个，联动 XP-073 deviceTier），复用前 `destroy` 旧页资源、清 JS 状态；不可见页面超时（如 30s）自动销毁回收。
- 页面瘦身：离开页面时清理定时器/事件监听/桥回调注册（提供 destroy 生命周期钩子）；大图滚动出屏释放解码（`img.decoding` 与懒加载）；限制同时播放的音视频。
- 泄漏检测：退后台整体内存水位监控 + 页面销毁后进程 RSS 回收率采样，未回收定位到具体容器；JS 侧 heap snapshot 抽样分析。
- 自动降级：内存压力回调（`onTrimMemory`/`didReceiveMemoryWarning`）触发——销毁非活跃容器、清缓存、通知 H5 释放重资源；极端时全局只保留前台一个容器。

```javascript
// container/pool.js —— WebView 池：实例上限 + 内存压力分级回收
const LIMITS = { flagship: 3, mid: 2, lowend: 1 };         // 联动 XP-073 分档
const limit = LIMITS[deviceTier] ?? 2;

class WebViewPool {
  #live = new Map();        // id -> { webview, page, lastActiveAt }
  constructor() {
    // 系统内存压力分级回收
    nativeMemory.onTrimMemory((level) => {
      if (level >= 'RUNNING_MODERATE') this.#reapInactive(30_000);   // 回收 30s 不活跃
      if (level >= 'RUNNING_LOW')      this.#reapInactive(10_000);
      if (level >= 'RUNNING_CRITICAL') this.#keepOnlyForeground();
    });
  }
  acquire(page) {
    if (this.#live.size >= limit) this.#evictOldest();      // 超限淘汰最久未活跃容器
    const wv = this.#recycle() ?? createWebView();
    this.#live.set(page.id, { webview: wv, page, lastActiveAt: Date.now() });
    return wv;
  }
  release(id) {
    const item = this.#live.get(id);
    item.page.emit('destroy');                               // 给页面统一清理钩子
    item.webview.stopLoading(); item.webview.clearState();   // 停加载 清 JS 定时器回调
    this.#live.delete(id);
  }
  #reapInactive(maxIdleMs) {
    const now = Date.now();
    for (const [id, it] of this.#live)
      if (!it.page.isForeground && now - it.lastActiveAt > maxIdleMs) this.release(id);
  }
  #keepOnlyForeground() {
    for (const [id, it] of this.#live)
      if (!it.page.isForeground) this.release(id);           // 极端：只留前台容器
  }
}
// 监控：页面销毁后 5s 采样进程 RSS，回收率 < 60% 的容器标记泄漏并上报 XP-068
```

---

## 十二、Electron 深度实战（099-105）
