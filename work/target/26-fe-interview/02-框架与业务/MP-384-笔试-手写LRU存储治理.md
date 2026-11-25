---
title: [MP-384] 笔试：手写 LRU 存储（10MB 容量治理）
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 笔试题, 存储]
type: 笔试题
---

## MP-384：笔试：手写 LRU 存储

**答**：实现 `SafeStorage`：① 分域 key（cfg:/cache:/user: 前缀）——cache 域可淘汰、user 域保护；② 写入前容量检查（getStorageInfoSync currentSize 接近 9MB → 淘汰 cache 域最旧）；③ LRU 元数据（每个 cache key 的 lastTouch 时间——独立索引 key 存储）；④ 写失败兜底（QuotaExceeded → 激进清理一半再重试一次）；⑤ 大对象拒存（>500KB 提示走文件系统）。写出实现。

```javascript
const LIMIT = 9 * 1024;         // KB (总量 10MB, 留 1MB 余量)
const idxKey = 'cache:lru-index';

export const SafeStorage = {
  set(key, value) {
    const size = JSON.stringify(value).length / 1024;
    if (size > 500) throw new Error('too large, use FileSystem');   // 大对象拒存
    this._evictIfNeeded(size);
    try {
      wx.setStorageSync(key, value);
      this._touch(key, size);
    } catch (e) {                                     // 超限: 激进清理
      this._evictAggressive();
      wx.setStorageSync(key, value);
      this._touch(key, size);
    }
  },
  _evictIfNeeded(incoming) {
    const info = wx.getStorageInfoSync();
    if (info.currentSize + incoming < LIMIT) return;
    const index = this._getIndex();
    const cacheKeys = Object.keys(index).filter((k) => k.startsWith('cache:'))
      .sort((a, b) => index[a] - index[b]);           // 最旧先淘汰
    for (const k of cacheKeys) {
      if (wx.getStorageInfoSync().currentSize + incoming < LIMIT) break;
      wx.removeStorageSync(k); delete index[k];
    }
    wx.setStorageSync(idxKey, index);
  },
  _evictAggressive() {
    const info = wx.getStorageInfoSync();
    const index = this._getIndex();
    Object.keys(index).filter((k) => k.startsWith('cache:')).slice(0, Math.ceil(info.keys.length / 2))
      .forEach((k) => { wx.removeStorageSync(k); delete index[k]; });
    wx.setStorageSync(idxKey, index);
  },
  _touch(key, size) {
    const index = this._getIndex();
    index[key] = Date.now();
    wx.setStorageSync(idxKey, index);
  },
  _getIndex() { return wx.getStorageSync(idxKey) || {}; },
};
// user:/cfg: 前缀永不淘汰; cache: LRU
```

**评分点**：
- 分域淘汰策略（cache 可淘汰 / user 保护）
- LRU 独立索引 key（lastTouch 时间戳）
- QuotaExceeded 的两级兜底（预防性 + 激进）
- 大对象拒存引导文件系统（能力分级）
