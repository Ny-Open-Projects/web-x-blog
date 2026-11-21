---
title: [PER-070] 多端登录互踢如何设计？Web 端如何感知被踢？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-070：多端登录互踢如何设计？Web 端如何感知被踢？

**答**：
- 服务端以“用户 + 设备类型”维度管理会话：每个端一个 session（含 token 版本），新登录按策略踢旧端（同端互踢/全端互踢/允许共存 N 个）。
- 实现：Redis 存 `user:{id}:sessions` 集合与每会话的 tokenVersion；被踢会话的 tokenVersion bump，校验时立即 401。
- Web 端感知被踢的两种通道：**WebSocket 推送 kick 事件**（实时）+ **401 拦截器兜底**（轮询/任意请求时触发），两者都要有。
- 被踢后的 UX：提示“您的账号在其他设备登录”，清理本地状态并跳登录页，不做静默登出。

```javascript
// 服务端：登录互踢 —— 新会话顶掉同类型旧会话
async function onLogin(userId, deviceType) {
  const key = `user:${userId}:sessions`;
  const sessions = JSON.parse((await rds.get(key)) ?? '[]');
  const old = sessions.find((s) => s.device === deviceType);
  if (old) {
    await rds.publish(`kick:${old.sessionId}`, JSON.stringify({ reason: 'other-device' })); // 通知旧端
    await rds.del(`session:${old.sessionId}`); // 旧会话立即失效
  }
  const sessionId = crypto.randomUUID();
  sessions.push({ sessionId, device: deviceType, loginAt: Date.now() });
  await rds.setEx(key, 60 * 60 * 24 * 7, JSON.stringify(sessions));
  return sessionId;
}
```

```javascript
// Web 端：双通道感知被踢
// 通道 1：WebSocket 实时推送
const ws = new WebSocket('wss://rt.example.com/ws');
ws.onmessage = (e) => {
  const msg = JSON.parse(e.data);
  if (msg.type === 'kick') {
    alert('您的账号已在其他设备登录');
    localStorage.removeItem('ui-prefs'); // 只清非敏感 UI 偏好，token 本就不落盘
    location.assign('/login?reason=kicked');
  }
};
// 通道 2：HTTP 401 兜底（WS 断线或推送丢失时仍然生效）
fetch('/api/me', { credentials: 'include' }).then((r) => {
  if (r.status === 401) location.assign('/login?reason=expired');
});
```
