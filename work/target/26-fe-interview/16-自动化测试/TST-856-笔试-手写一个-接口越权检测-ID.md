---
title: [TST-856] 笔试：手写一个「接口越权检测」(IDOR 自动化探测)
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-856：笔试：手写一个「接口越权检测」(IDOR 自动化探测)
**答**：
- 需求：实现 detectIDOR(fetch, { selfId, resourceIds, endpoint }) —— 用 A 用户的凭据访问 B 用户的资源 ID，检测是否能读到他人数据。
- 规则：对每个 resourceId 发请求，若返回 200 且响应体含其他用户标识则判为越权；统计越权 ID 列表。
- 边界：请求异常跳过并记录；selfId 自身的资源不算越权；并发控制不超过 limit。

```javascript
async function detectIDOR(fetch, { selfId, resourceIds, endpoint, limit = 3 }) {
  const result = { vulnerable: [], errors: [] };
  const queue = resourceIds.filter(id => id !== selfId);
  // 简易并发控制
  const workers = Array.from({ length: Math.min(limit, queue.length) }, async () => {
    while (queue.length) {
      const id = queue.shift();
      try {
        const res = await fetch(`${endpoint}/${id}`);
        if (res.status === 200) {
          const body = await res.json();
          if (body.ownerId && body.ownerId !== selfId) result.vulnerable.push(id);
        }
      } catch (e) { result.errors.push({ id, message: e.message }); }
    }
  });
  await Promise.all(workers);
  return result;
}
// 期望 vulnerable 为空；若非空说明存在 IDOR 越权漏洞
```
**评分点**：
- 用 A 凭据访问 B 资源并依据响应 ownerId 判定越权，逻辑正确。
- 排除 selfId 自身资源，避免误报。
- 并发控制 limit，异常跳过并记录——工程健壮性。
- 能点出「前端路由隐藏不等于服务端鉴权」这一 IDOR 核心认知。
