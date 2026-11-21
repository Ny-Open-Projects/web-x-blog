---
title: [ARC-434] 前端的数据库思维：IndexedDB 端上数据层架构如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-434：IndexedDB 端上数据层架构
**答**:
- 把 IndexedDB 当真数据库设计：库/表规划（按业务域分库，大表按月分 store）、索引设计（查询模式反推索引）、版本迁移（onupgradeneeded 分步迁移脚本化，禁止跳版假设）。
- 数据层封装：统一 DAO 层（业务不直接碰 IDB API）、事务边界（相关操作单事务）、序列化协议（结构化克隆兼容性——不存函数/不可克隆对象）。
- 容量治理：配额探测（navigator.storage.estimate）+ LRU/TTL 清理策略 + 大对象降级（blob 存 OSS，端上存引用）。
- 与服务端同步：版本号/时间戳协议（ARC-056 离线优先延伸），冲突按业务规则；同步队列幂等键防重放。
- 兼容与降级：Safari IDB 的历史坑（事务悬挂/ blob 支持）——封装层统一 try/catch 降级到内存缓存。
```javascript
class DbSchema {
  v3(db, tx, oldV) {                       // 分步迁移：按 oldV 逐版本升级
    if (oldV < 2) db.createObjectStore('goods', { keyPath: 'id' })
      .createIndex('by_category', 'categoryId');
    if (oldV < 3) db.createObjectStore('sync_queue', { keyPath: 'idempotencyKey' });
  }
}
async function capacityGuard() {
  const { usage, quota } = await navigator.storage.estimate();
  if (usage / quota > 0.8) await gcStaleStores({ ttl: 7 * 86400e3 }); // 过期清理
}
```
