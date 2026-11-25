---
title: [SCN-1130] IoT 设备的设备影子冲突处理（多端同时改配置）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1130：IoT 设备的设备影子冲突处理（多端同时改配置）

**答**：
- 冲突：两运维同时改 desired——版本号比较（后者覆盖+前者通知），或字段级合并。
- 前端：编辑冲突提示（你的修改已被覆盖，展示最新配置）。
- 审计：配置变更历史（diff 视图）。

```javascript
// 影子冲突
function shadowConflict(local, remote) {
  if (remote.version > local.version)
    return { conflict: true,
      action: '提示覆盖',
      latest: remote.desired,
      diff: diffDesired(local.desired, remote.desired) };
  return { conflict: false };
}
function diffDesired(a, b) {
  return Object.keys({ ...a, ...b })
    .filter(k => a[k] !== b[k])
    .map(k => ({ key: k, old: a[k], new: b[k] }));
}
```
