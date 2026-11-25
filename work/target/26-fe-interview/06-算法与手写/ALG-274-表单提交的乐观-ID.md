---
title: [ALG-274] 乐观 ID 与服务端 ID 对账：本地临时 id（client-uuid）→ 服务端真实 id 的映射与引用重写？
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---
## ALG-274：乐观 ID 与服务端 ID 对账：本地临时 id（client-uuid）→ 服务端真实 id 的映射与引用重写？
**答**：离线创建任务（本地 uuid），恢复同步后服务端分配真实 id——本地所有引用（子任务 parent、附件关联）要从临时 id 重写到真实 id；同步期间双 id 共存（未同步项仍用临时 id）。

**思路**：映射表 Map<clientId, serverId>；解析函数 resolve(id)：映射命中返回真实 id，未命中返回原 id（未同步项）；同步成功时遍历本地数据重写引用。

```javascript
class IdMapper {
  #map = new Map();                                       // clientId -> serverId
  register(clientId, serverId) { this.#map.set(clientId, serverId); }
  resolve(id) { return this.#map.get(id) ?? id; }         // 未同步项：原样返回
  rewriteAll(items) {                                     // 同步完成后：全量重写引用
    return items.map((item) => ({
      ...item,
      id: this.resolve(item.id),
      parentId: item.parentId ? this.resolve(item.parentId) : null,   // 引用字段重写
      attachments: item.attachments?.map((a) => ({ ...a, id: this.resolve(a.id) })),
    }));
  }
}
// 离线创建：task { id: 'c-uuid-1', parentId: 'c-uuid-0' }（双临时 id）
// 同步：server 分配 t-101/t-100 → register('c-uuid-0','t-100'), register('c-uuid-1','t-101')
// 重写：rewriteAll → { id: 't-101', parentId: 't-100' }（引用链完整）
// 双 id 共存窗口：未同步项仍用临时 id（resolve 原样返回）—— 已同步与未同步混合渲染正确
// 服务端配合：请求带 client_id → 响应回带映射（对账幂等，重放不重复创建，PER-384）
```

**评分点**：
- 映射表 + resolve 的双 id 共存语义——本题核心。
- rewriteAll 引用字段重写（parentId/attachments 递归引用链）。
- 服务端 client_id 回传映射的对账幂等。
- 未同步项 resolve 原样返回（混合状态正确渲染）。
