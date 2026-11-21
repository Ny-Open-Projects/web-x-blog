---
title: [H5-123] Badging API 与 Contact Picker 各解决什么小需求？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-123：Badging API 与 Contact Picker 各解决什么小需求？
**答**：
- Badging：`navigator.setAppBadge(n)` 在**应用图标**上显示数字角标（PWA/已安装站点的任务栏、Dock 图标），`clearAppBadge()` 清除；用于未读数、待办数提醒，比标题栏 "(3)" 更醒目。
- Badging 仅在已安装的 PWA（或桌面快捷方式）中生效，Chromium 系为主；需用户安装后再触发，页面里直接调用通常无效。
- Contact Picker：`navigator.contacts.select(props, { multiple })` 弹出**系统通讯录选择器**，用户点选后才返回所选联系人字段（姓名/电话/邮箱/地址/图标）。
- 设计原则：网站**永远无法**静默读取通讯录，必须用户手势触发 + 逐次选择；不可保存选择结果供下次免授权使用。
- 场景：邀请好友（取手机号）、转账收款人（选联系人）、邀请邮件群发。

```javascript
// 1) Badging：PWA 未读消息角标
function syncBadge(unreadCount) {
  if (!('setAppBadge' in navigator)) return;   // 能力检测
  unreadCount > 0
    ? navigator.setAppBadge(unreadCount).catch(() => {})
    : navigator.clearAppBadge().catch(() => {});
}
// push 推送到达时
self.addEventListener('push', () => { /* SW 内同样可 setAppBadge */ });

// 2) Contact Picker：邀请好友
inviteBtn.addEventListener('click', async () => {
  if (!('contacts' in navigator) || !window.ContactsManager) {
    return showInviteLink();                   // 降级：复制邀请链接
  }

  try {
    const contacts = await navigator.contacts.select(
      ['name', 'tel'],                         // 只请求需要的字段
      { multiple: true },                      // 可多选
    );

    const invitees = contacts.map((c) => ({
      name: c.name?.[0] ?? '未命名',
      phone: c.tel?.[0],
    }));
    await fetch('/api/invite', {
      method: 'POST',
      body: JSON.stringify({ invitees }),
    });
  } catch (err) {
    if (err.name !== 'AbortError') console.warn('通讯录选择失败：', err);
  }
});
```
