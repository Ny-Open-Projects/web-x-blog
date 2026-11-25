---
title: [912] 权限变化时缓存怎么治理
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, TanStack Query, 权限]
type: 面试题
---

## 912：权限变化时缓存怎么治理

**答**：
- 权限与缓存的耦合点：角色降级/登出后旧权限时代的缓存还在（内存可读、devtools 可见）——治理：登出 queryClient.clear()、角色变更失效权限敏感域（['admin'] 域全失效）、敏感数据在服务端层裁剪。
- 前置过滤优于后置清理：queryFn 层按权限过滤（服务端才是权限真相），前端缓存只存「当前用户有权看」的——权限变化后 invalidate 让服务端重新过滤，前端数据本身已按权限裁剪。
- 权限态作为 QueryKey 一部分：['user', 'detail', id, role]——角色变化自动切换缓存空间（旧角色缓存 gc 回收），避免同 key 不同权限的数据互踩。
- 追问钩子：为什么不能只靠前端 hide？——前端隐藏是 UI 层，缓存里的完整数据在内存可被扒（devtools/内存 dump）；权限必须在服务端数据层裁剪。

```ts
const role = useAuth(s => s.role);
const q = useQuery({
  queryKey: ['admin', 'users', role],           // 角色入 Key：缓存空间隔离
  queryFn: () => fetchAdminUsers(),             // 服务端按 token 权限裁剪
  enabled: role !== 'guest',
});
logout: () => { auth.clear(); queryClient.clear(); }
```

