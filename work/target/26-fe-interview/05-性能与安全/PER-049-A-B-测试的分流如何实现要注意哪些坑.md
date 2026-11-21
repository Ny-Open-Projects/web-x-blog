---
title: [PER-049] A/B 测试的分流如何实现？要注意哪些坑？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-049：A/B 测试的分流如何实现？要注意哪些坑？

**答**：
- 分流要求**同一用户始终命中同一分组**：对 `experimentId + userId` 做 hash 取模分桶，结果稳定可复现。
- 命中实验桶后再按比例切 variantA/variantB；对照组 control 必须保留，否则无法归因。
- 坑：分桶因子要固定（不能按天变）、埋点带实验分组字段（曝光时上报）、注意灰度放量时已命中的用户不能被重新分配。
- 平台化方案由服务端下发分组配置，前端 SDK 只负责读配置、上报曝光，分流逻辑不下放前端。

```javascript
// A/B 分流：对 experimentId + userId 做 hash，同一用户永远命中同一分组
function getBucket(userId, experimentId, trafficRatio = 0.2) {
  const key = `${experimentId}:${userId}`;
  let hash = 0;
  for (let i = 0; i < key.length; i++) {
    hash = (hash * 31 + key.charCodeAt(i)) >>> 0; // 32 位无符号 hash
  }
  const slot = (hash % 1000) / 1000; // 映射到 0 ~ 0.999
  if (slot >= trafficRatio) return 'control';    // 未命中实验流量，进对照组
  return slot % 2 < 1 ? 'variantA' : 'variantB'; // 命中后对半切分两个实验组
}

// 曝光时把分组写入埋点，供分析平台做显著性检验
tracker.send({ event: 'ab_expose', group: getBucket(userId, 'new_checkout_2026') });
```
