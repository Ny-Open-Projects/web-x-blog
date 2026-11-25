---
title: [AV-411] 协作 UI 的 presence 设计（成员列表/头像/状态）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-411：协作 UI 的 presence 设计（成员列表/头像/状态）

**答**：
- 数据：{ userId, name, color, cursor, state, lastActive }——presence 通道高频小消息。
- 渲染：成员头像栏（重叠折叠）、画布光标带名字标签、活动状态（编辑/空闲）。
- 隐私：状态粒度可配置（显示具体页面 vs 只显示在线）。

```javascript
// presence 管理
class PresenceBoard {
  constructor(max = 20) { this.members = new Map(); this.max = max; }
  update(userId, info) {
    this.members.set(userId, { ...this.members.get(userId), ...info,
      lastActive: Date.now() });
  }
  render() {
    const list = [...this.members.values()]
      .sort((a, b) => b.lastActive - a.lastActive).slice(0, this.max);
    return { avatars: list.map(m => ({ name: m.name, color: m.color })),
      overLimit: this.members.size > this.max };
  }
}
```
