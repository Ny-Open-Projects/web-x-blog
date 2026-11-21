---
title: [PER-810] RN 图片缓存策略：原生缓存层级、URL 稳定性与预加载如何配合
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-810：RN 图片缓存策略：原生缓存层级、URL 稳定性与预加载如何配合

**答**：
- RN 图片链路：JS 声明 source → Native ImageLoader 解码 → 三级缓存（内存 LRU、磁盘、网络）；磁盘缓存以 URL（含 query）为 key——URL 带时间戳/随机参数会打爆缓存。
- URL 稳定性是第一原则：缩略参数（?w=200）归一化到固定档位集合，同一图固定同 URL 才能命中磁盘。
- 预加载：Image.prefetch 提前下网络层（落磁盘缓存），进入页面时直接命中磁盘省一次网络；大列表预加载可视区 +2 行。
- 内存控制：iOS/Android 的解码后位图缓存有限额，超限 LRU 逐出；大图必须给 resize 策略（Image 组件按目标尺寸下载缩略档，避免解码 4000px 原图）。

```javascript
// 图片预加载与缓存命中率保障
const normalizeUrl = (u) => {                 // URL 归一化保缓存 key 稳定
  const { base, q } = parseUrl(u);
  q.w = clampToTier(q.w, [200, 400, 800]);    // 宽度归一到档位
  delete q.t; delete q._t;                    // 去时间戳等随机参数
  return buildUrl(base, q);
};
function preloadVisible(list, idx, ahead = 2) {
  for (let i = idx; i <= Math.min(idx + ahead, list.length - 1); i++)
    Image.prefetch(normalizeUrl(list[i].cover));    // 落磁盘缓存
}
// 失败兜底：prefetch 失败不阻塞主流程，进入页面走正常加载链路
Image.prefetch(url).catch(e => report('prefetch-fail', { url, msg: String(e) }));
```
