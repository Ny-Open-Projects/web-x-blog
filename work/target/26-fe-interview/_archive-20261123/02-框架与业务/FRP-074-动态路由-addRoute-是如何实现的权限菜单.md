---
title: [FRP-074] 动态路由 addRoute 是如何实现的？权限菜单场景怎么落地？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-074：动态路由 addRoute 是如何实现的？权限菜单场景怎么落地？

**答**：
- matcher 的 `addRoute(record)`：编译 path 后把 matcher record **插入 matchers 集合**（含评分重排），后续 resolve 立即生效——不需要重启或刷新，这就是"动态添加路由"的全部原理。
- 嵌套路由用 `parentName`：找到父 record 后 push 到其 children，同时生成带完整层级 `matched` 数组的 record（matched 决定 RouterView 的逐层渲染）。
- 权限菜单落地模式：登录后调 `filterRoutes(asyncRoutes, userRoles)` 过滤 → 逐个 `router.addRoute(route)` → 若当前地址匹配新路由需 `router.replace(to.fullPath)` 二次导航（因为初始导航已 404）。
- 另一种落地：路由表全部注册但 `beforeEach` 里做 meta.roles 校验；对比：addRoute 是"物理不存在"，守卫是"存在但拦截"，前者防直接 URL 访问更彻底。

```javascript
// 简化实现，帮助理解 addRoute 与权限菜单流程
function createRouter() {
  const matchers = [];
  function addRoute(record, parent) {
    if (parent) {
      // 嵌套：挂到父 children，matched 记录完整链
      parent.children = parent.children || [];
      parent.children.push(record);
      record.matchedChain = [...(parent.matchedChain || [parent]), record];
    } else {
      matchers.push(record);
      record.matchedChain = [record];
    }
    return () => removeRoute(record); // 返回删除函数
  }
  function removeRoute(record) {
    const i = matchers.indexOf(record);
    if (i > -1) matchers.splice(i, 1);
  }
  function resolve(path) {
    for (const r of matchers) {
      // 简化匹配：只做前缀/全等演示
      if (r.path === path) return { matched: r.matchedChain };
      if (r.children) {
        const c = r.children.find((ch) => ch.path === path);
        if (c) return { matched: c.matchedChain };
      }
    }
    return null;
  }
  return { addRoute, removeRoute, resolve, getRoutes: () => [...matchers] };
}

// 权限菜单落地：登录后按角色注入
const router = createRouter();
router.addRoute({ path: '/login', name: 'login' });

const asyncRoutes = [
  { path: '/admin', name: 'admin', meta: { roles: ['admin'] }, children: [
    { path: 'dashboard', name: 'dashboard', meta: { roles: ['admin'] } },
  ] },
  { path: '/profile', name: 'profile', meta: { roles: ['user', 'admin'] } },
];

function setupPermissions(userRole) {
  asyncRoutes
    .filter((r) => r.meta.roles.includes(userRole))
    .forEach((r) => {
      router.addRoute(r);
      (r.children || []).forEach((c) => router.addRoute(c, r)); // 逐级注入
    });
}
setupPermissions('admin');
console.log('admin 路由数:', router.getRoutes().length);           // 2 login+admin
console.log(!!router.resolve('/admin/dashboard'));                 // true 已可访问
console.log(!!router.resolve('/profile'));                         // false user 专属未注入
```
