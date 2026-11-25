---
title: [ARC-223] RBAC 权限变更的实时生效如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-223：RBAC 权限变更的实时生效如何设计？
**答**：
- 三档时效：即时（高危操作收回，如封禁）、分钟级（角色调整）、次登录（普通菜单变化）。不是所有变更都值得推实时，成本先想清楚。
- 推送链路：权限中心变更 → 事件总线 → WebSocket/SSE 下发"权限版本号变更"通知 → 前端拉取新快照热更路由与按钮。推送的永远是"去拉"的信号，不推全量数据。
- 前端热更：路由表重建 + 已打开页面的操作区即时收敛（当前页无权时给温和提示并禁止提交，不粗暴踢出）。
- 兜底：每次请求带权限快照版本号，后端版本不匹配返回 426/特定码触发前端刷新——推送丢失时靠请求路径自愈。

```typescript
// 权限热更管理器
let permVersion = 0;
ws.on('perm-changed', ({ version }) => {           // 只推版本号
  if (version > permVersion) refreshSnapshot(version);
});
async function refreshSnapshot(v: number) {
  permVersion = v;
  const snap = await api.get('/me/perm-snapshot');
  rebuildRoutes(snap);                              // 路由表重建
  if (pagePermsInvalid(currentRoute, snap)) toast('权限已更新，当前页操作已受限');
}
// 请求拦截器兜底：响应 code === 'PERM_STALE' → refreshSnapshot(await api.head('/me/perm-version'))
```
