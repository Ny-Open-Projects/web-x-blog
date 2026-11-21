---
title: [DP-275] 源码识别：Apollo Client 源码中的规范化缓存与失效？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-275：源码识别：Apollo Client 源码中的规范化缓存与失效？
**答**:
- 备忘录（规范化缓存）：响应按 __typename:id 拆成实体表（User:1 → {...}），查询结果存"引用"——多查询共享实体，改一处全链路更新（ARC-054 normalizr 同款思想）。
- 观察者：watchQuery 订阅，实体变更 → 受影响查询失效重发——失效传播靠"实体 → 查询"反向索引。
- 策略：fetchPolicy（cache-first/network-only/no-cache）与分页 merge 函数是两个策略注入点。
- 识别要点：能说清"为什么需要 normalization"——列表页与详情页的同一 User 更新后两处同步。

```javascript
// Apollo 缓存规范化（源码级简化）
class InMemoryCache {
  entities = new Map();            // 'User:1' → 数据
  refs = new Map();                // 'User:1' → Set<watching query>
  write(queryResult) {             // 规范化写入
    walk(queryResult, (obj) => {
      const id = `${obj.__typename}:${obj.id}`;
      this.entities.set(id, { ...this.entities.get(id), ...obj });
    });
  }
  read(query) {                    // 读：引用解包
    return walk(query, (ref) => this.entities.get(ref.__ref));
  }
  modifyEntity(id, patch) {
    this.entities.set(id, { ...this.entities.get(id), ...patch });
    this.refs.get(id)?.forEach(q => q.notifyChanged());   // 反向索引通知所有受影响查询
  }
}
// fetchPolicy 策略：cache-first（命中不请求）/ network-only（绕过缓存）/ cache-and-network（先缓存后台刷）
```
