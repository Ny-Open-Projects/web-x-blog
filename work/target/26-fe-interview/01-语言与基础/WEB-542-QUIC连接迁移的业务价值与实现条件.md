---
title: [WEB-542] QUIC 连接迁移的业务价值与实现条件
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-542：QUIC 连接迁移的业务价值与实现条件

**答**：
- 价值场景：移动端 Wi-Fi 切 4G、电梯里基站切换——TCP 四元组变了连接就断，QUIC 用 Connection ID 标识连接，IP 变了连接不断
- 收益不是「不重传」而是「不重握手」：TCP 断了要重新 TCP 握手 + TLS 握手 + TCP 慢启动，弱网下这是 2~5 秒的体感卡顿；QUIC 迁移只丢当前在途包
- 实现条件：客户端换网后用同一 Connection ID 发新路径的 Initial/Path Challenge，服务端 Path Validation 通过后才在新路径上续传
- 限制条件要清楚：NAT 重绑定时旧端口映射消失，需客户端主动重建；公司代理/VPN 常按五元组转发，迁移在这些环境不生效
- 前端侧验证：弱网模拟（切飞行模式再开）观察长连接接口是否仍需重连，IM/直播场景收益最明显

```javascript
// 连接迁移监控：上报网络切换后长连接的存活情况
let lastType = navigator.connection?.type;
navigator.connection?.addEventListener('change', () => {
  const now = navigator.connection.type;
  if (lastType && now && lastType !== now) {
    wsProbe(); // 网络切换后立刻探测业务长连接是否存活
  }
  lastType = now;
});
function wsProbe() {
  const t0 = performance.now();
  fetch('/api/conn-probe', { cache: 'no-store' })
    .then(() => beacon({ event: 'net-switch-survive', ms: performance.now() - t0 }))
    .catch(() => beacon({ event: 'net-switch-broken' }));
}
```
