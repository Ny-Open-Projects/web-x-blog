---
title: [H5-362] 浏览器存储配额：estimate、persist 与清理策略
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 存储]
type: 面试题
---

## H5-362：浏览器存储配额：estimate、persist 与清理策略

**答**：
- 配额机制：现代浏览器按「站点占磁盘总量的比例」给配额（Chrome 约磁盘 60%~80% 分配，单源上限动态），超配额写操作抛 QuotaExceededError——localStorage/IDB/Caches 都计入
- navigator.storage.estimate() 读取 usage/quota，写入前对大缓存做预算检查；usage 细分由 performane.storage 不提供，需自行分账（每类缓存记 key 前缀统计）
- persist() 申请持久化：防止浏览器在磁盘压力下自动清掉你的数据（eviction 机制按 LRU 清非持久站点）；PWA/重要离线应用必须申请
- 清理策略：缓存分层（核心数据 protect、媒体缓存可弃），LRU + TTL 双约束，达到水位主动清理而不是等浏览器清理
- 写失败的统一处理：QuotaExceededError 降级（丢最旧数据重试 / 放弃持久化只留内存）必须封装在存储层，业务无感

```javascript
async function ensureSpace(needBytes) {
  const { usage, quota } = await navigator.storage.estimate();
  if (quota - usage < needBytes) {
    await evictLRU(needBytes);                 // 主动清理可弃缓存
    await navigator.storage.persist();          // 申请持久化
    if ((await navigator.storage.estimate()).quota - usage < needBytes)
      throw new QuotaExceeded();                // 仍不足: 业务降级
  }
}
```
