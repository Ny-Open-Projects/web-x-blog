---
title: [ARC-500] 登录态在多 Tab/多端下的一致性架构如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-500：登录态多 Tab/多端一致性架构
**答**:
- 多 Tab 问题：A Tab 登录后 B Tab 不知道（各自请求 401）；A Tab 登出 B Tab 还在"已登录"假象。方案：登录态变更广播（BroadcastChannel/storage 事件）+ 各 Tab 订阅同步（登录/登出/切换账号三事件）。
- Token 存储权衡：localStorage（跨 Tab 共享、XSS 风险）vs HttpOnly Cookie（安全、跨 Tab 天然一致，但 CSRF 需防护）vs 内存 + 共享 Worker（最优安全但工程复杂）。主流：HttpOnly Cookie 为主，Web Token 场景 localStorage + 广播。
- 401 处理收口：请求层统一（ARC-410），并发 401 共享一次刷新；刷新失败的登出动作广播全 Tab，B Tab 收到后清态跳登录（带 returnUrl）。
- 多端一致性：单设备踢出/全端踢出（ARC-415）；会话续期推送（其他端刷新了 token，本端尽快跟进避免频繁 401）。
- 边界：隐私模式（storage 事件可用性）、多账号浏览器容器（Chrome profile 隔离天然一致）。
```javascript
// 登录态广播总线
const bus = new BroadcastChannel('auth');
export const auth = {
  async logout() { await api.logout(); clearTokens();
    bus.postMessage({ type: 'logout', ts: Date.now() }); toLogin(); }
};
bus.onmessage = ({ data }) => {
  if (data.type === 'logout') { clearTokens(); toLogin(); }   // 其他 Tab 同步登出
  if (data.type === 'refresh') rotateToken(data.token);        // 跟进续期
};
```

**追问**：

1. BroadcastChannel 在旧浏览器或隐私模式不可用，同 Tab 的 storage 事件又不触发，怎么兜底？ → 特性检测后降级为定时轮询 storage 版本号，并在页面可见性变化时主动校验一次登录态。
2. 三个 Tab 同时收到 401，怎么保证只刷新一次？ → 用 Web Locks 或基于 storage 的 leader 选举，只有一个 Tab 拿锁去刷新，其余 Tab 等广播结果再决定重放请求。
3. HttpOnly Cookie 方案下，用户怎么知道自己在别的设备被踢下线了？ → 靠接口返回的特定错误码加上会话事件的长连接或轮询，收到即清本地态、跳登录并带 returnUrl。
