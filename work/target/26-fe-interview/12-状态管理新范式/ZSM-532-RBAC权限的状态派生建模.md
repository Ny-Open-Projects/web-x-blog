---
title: [ZSM-532] RBAC 权限状态怎么从「角色」派生成「可用操作」
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-532：RBAC 权限状态怎么从「角色」派生成「可用操作」

**答**：
- 权限状态只存「事实」：`roles: string[]` + `permissions: Set<string>`（服务端下发的资源级权限点）。组件消费的「能不能做 X」全部派生，不单独存布尔——存布尔就会出现「角色变了权限没跟着变」的不一致。
- 派生层两级：`can(action, resource)` 纯函数（查 permissions + roles 映射），以及业务级规则（如「仅创建者可编辑」需要 `ownerId` 参与比较）。规则集中在一个 auth 模块，禁止组件里散落 `role === 'admin'` 判断。
- 权限变更传播：角色/权限点放 store，登录/切换租户时一次性 set，所有订阅派生值的组件自动更新——这就是「权限也是状态」的意义。
- 缓存注意：派生函数返回布尔是标量，天然稳定引用；返回「可操作列表」时记得 useShallow。路由守卫也是同一派生：`can('view', route)` 不过就重定向 403 页。
- 追问钩子：权限下发的时机差异——SSR 里在服务端读 session 先算好 permissions 注入初始状态，客户端首帧就有权限结果，不会闪「先显示再隐藏」。

```javascript
// 权限矩阵：角色 → 操作集
const ROLE_MATRIX = {
  admin: ['view', 'edit', 'delete', 'invite'],
  editor: ['view', 'edit'],
  viewer: ['view'],
}

const useAuth = create((set) => ({
  roles: ['viewer'],
  permissions: new Set(),          // 资源级权限点（超出角色的特例）
  ownerId: null,
  userId: null,
  hydrate: ({ roles, permissions, userId, ownerId }) =>
    set({ roles, permissions: new Set(permissions), userId, ownerId }),
}))

// 派生：can(action, resource) 集中决策
function useCan() {
  const roles = useAuth((s) => s.roles)
  const perms = useAuth((s) => s.permissions)
  const userId = useAuth((s) => s.userId)
  return (action, resource = {}) => {
    const allowed = roles.some((r) => ROLE_MATRIX[r]?.includes(action))
      || perms.has(`${action}:${resource.type ?? '*'}`)
    // 业务规则：仅创建者可编辑
    if (action === 'edit' && resource.ownerId != null) {
      return allowed && resource.ownerId === userId
    }
    return allowed
  }
}

// 组件消费
function DocActions({ doc }) {
  const can = useCan()
  return can('edit', { type: 'doc', ownerId: doc.ownerId }) ? <EditBtn /> : null
}
```
