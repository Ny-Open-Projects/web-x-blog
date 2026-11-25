---
title: [R19-380] React19 缓存层设计：cache() 与 fetch 扩展
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 数据流]
type: 面试题
---

## R19-380：React19 缓存层设计：cache() 与 fetch 扩展

**答**：
- cache(fn)：RSC 环境的「请求级记忆化」——同一渲染 pass 内同参数调用共享结果（React 19 开放 client 侧实验）；与 useMemo 区别：cache 跨组件/跨层级共享
- fetch 扩展（Next.js/React 19 语义）：默认缓存 + revalidateTag/Path 失效——「fetch 即缓存」的心智转变与 opt-out（cache: 'no-store'）
- 缓存粒度策略：请求级（cache）、路由级（revalidatePath）、标签级（revalidateTag）——数据依赖图决定失效粒度
- 与客户端缓存的关系：server cache 到 client 后由 React Query/SWR 接管 hydration——两层缓存的交接边界
- 深水点：cache 的参数必须是可序列化比较的（引用相等或值相等）——对象参数每次新建会 miss；「参数稳定」是使用纪律

```javascript
import { cache } from 'react';
const getUser = cache(async (id: string) => {
  return db.user.find(id);          // 同一请求内 id 相同 → 只查一次
});
// RSC 树中多处调用 getUser(id) → 单次 DB 查询
```
