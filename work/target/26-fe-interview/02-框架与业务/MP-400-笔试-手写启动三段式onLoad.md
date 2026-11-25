---
title: [MP-400] 笔试：手写启动三段式 onLoad（缓存→预取→刷新）
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 笔试题, 性能]
type: 笔试题
---

## MP-400：笔试：手写三段式启动

**答**：实现首页三段式启动：① 段 1：缓存渲染（storage 上次数据——立即 setData，带 staleAt 标记 UI 显示「内容可能过期」）；② 段 2：并行预取（wx.login 与 home 接口同时发——登录与数据不串行）；③ 段 3：新数据到达 → diff 渲染（只 setData 变化字段——路径 patch）+ 缓存更新；④ 骨架兜底（无缓存时 initialRenderingCache/骨架组件）；⑤ 各段耗时打点（缓存命中/网络等待/diff 渲染分别计时）。写出实现。

```javascript
Page({
  async onLoad() {
    this._t0 = Date.now();
    // 段1: 缓存立即渲染
    const cached = wx.getStorageSync('home:data');
    if (cached) {
      this.setData({ ...cached, stale: Date.now() - cached.at > 5 * 60_000 });
      this._cacheMs = Date.now() - this._t0;
    }
    // 段2: 登录与数据并行(不串行)
    const [_, fresh] = await Promise.all([
      ensureLogin(),
      api.home({ cachedAt: cached?.at }),            // 服务端可增量(304 语义)
    ]);
    const netMs = Date.now() - this._t0;
    // 段3: diff 渲染 + 缓存更新
    const patch = cached ? diffToPatch(cached.data ?? cached, fresh) : fresh;
    this.setData({ ...patch, stale: false });
    wx.setStorageSync('home:data', { ...fresh, at: Date.now() });
    // 打点: 各段拆解
    beacon({ type: 'boot', cacheMs: this._cacheMs ?? 0, totalMs: netMs,
      usedCache: !!cached, diffKeys: Object.keys(patch).length });
  },
});
// 骨架兜底: page.json initialRenderingCache: 'static' + 无缓存时 WXML 骨架块
// 收益: 缓存命中 → 首屏 0 网络等待; diff 渲染 → setData 最小化
```

**评分点**：
- 三段语义清晰（缓存先渲染/并行预取/diff 更新）
- login 与数据并行（不串行——启动链路的关键优化）
- diffToPatch 复用（只 setData 变化字段）
- stale 标记的 UX 诚实性 + 各段打点归因
