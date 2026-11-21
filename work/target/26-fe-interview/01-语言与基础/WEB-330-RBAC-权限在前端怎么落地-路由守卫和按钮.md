---
title: [WEB-330] RBAC 权限在前端怎么落地？路由守卫和按钮权限分别怎么做？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 笔试题
---

## WEB-330：RBAC 权限在前端怎么落地？路由守卫和按钮权限分别怎么做？
**答**：
- 前端权限只是体验层（隐藏入口），真正的防线在后端接口鉴权——这句话必须先说。
- 路由守卫：登录态校验 + 角色匹配 meta.roles，无权重定向 403；动态路由按后端返回的菜单生成 routes。
- 按钮/操作级：封装 v-permission 指令或组件 <Auth code="order:delete">，权限码来自后端，与接口权限一一对应。

```javascript
router.beforeEach(async (to) => {
  const { token, perms } = await ensureUser();
  if (!token) return '/login?redirect=' + to.fullPath;
  if (to.meta?.roles && !to.meta.roles.some(r => perms.roles.includes(r))) return '/403';
});
app.directive('permission', {
  mounted(el, { value }) {
    if (!perms.codes.includes(value)) el.remove(); // 按钮级
  }
});
console.log('<el-button v-permission="order:delete">删除</el-button>');
```

**评分点**：
- 结论先行，能一句话说清核心机制
- 要点覆盖主流程与关键分支（异常/并发/边界）
- 代码可运行且体现安全或性能意识
- 能主动说出"工程上怎么选"与常见坑
