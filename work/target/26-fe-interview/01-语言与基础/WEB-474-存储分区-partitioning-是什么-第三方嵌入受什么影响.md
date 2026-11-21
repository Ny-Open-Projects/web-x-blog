---
title: [WEB-474] 存储分区是什么，第三方嵌入受什么影响
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 隐私]
type: 面试题
---

## WEB-474：存储分区是什么，第三方嵌入受什么影响

**答**：
- 存储分区（Partitioning/CHIPS）：iframe 里的 Cookie、storage 按「顶级站点」分桶存储，同一第三方在 A 站和 B 站的数据互相隔离
- 动机：消灭用 Cookie 做跨站追踪的能力；配合第三方 Cookie 退场是同一场变革
- 前端影响：第三方登录 iframe、客服组件、支付弹窗中「靠共享 Cookie 免登」的方案失效，要迁移到 Partitioned Cookie（`Partitioned` 属性）或 postMessage/token 方案
- 自查方法：DevTools Application 面板看 Cookie 是否标记 partitioned；哪些 iframe 内的请求突然不带 Cookie
- 迁移路径：跨站身份场景用 first-party set / Storage Access API（有用户授权）替代共享 Cookie

```http
Set-Cookie: support_session=abc; Secure; SameSite=None; Partitioned;
```
```javascript
// 检测分区 Cookie 支持
document.hasStorageAccess?.().then(has => console.log('可访问第一方存储:', has));
```
