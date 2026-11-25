---
title: [SCN-1116] IoT 设备控制台的权限模型（空间/角色）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1116：IoT 设备控制台的权限模型（空间/角色）

**答**：
- 权限：空间（园区/楼栋/房间）维度授权 + 角色（管理员/运维/查看）。
- 控制：控制指令权限单独（viewer 不能下发指令）。
- 审计：控制操作全审计（谁在何时控制了什么设备）。

```javascript
// 空间权限
function spaceAuth(user, deviceId, action) {
  const device = deviceIndex.get(deviceId);
  const scope = user.spaces?.includes(device.spaceId);
  const caps = { admin: ['view', 'control', 'config'],
    ops: ['view', 'control'], viewer: ['view'] }[user.role] ?? [];
  if (!scope) return { ok: false, reason: '无该空间权限' };
  if (!caps.includes(action)) return { ok: false, reason: '角色无权限' };
  auditLog({ type: 'device-action', user: user.id, deviceId, action });
  return { ok: true };
}
```
