---
title: [WEB-442] JSONP 劫持是什么，现在还要防吗
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-442：JSONP 劫持是什么，现在还要防吗

**答**：
- JSONP：用 `<script src>` 绕过跨域拿数据，回调名由前端传、数据以 `callback({...})` 返回——本质是全局函数注入
- 劫持原理：JSONP 无凭证校验的传统下，第三方站可以引你站点的 JSONP 接口，直接拿走用户数据（配合 Cookie 凭证时更危险）
- 时代背景：CORS 普及后 JSONP 已淘汰，但老系统、埋点上报、广告 SDK 里仍常见
- 还要防吗：存活的 JSONP 接口仍要收口——回调名白名单校验、Referer 校验、敏感数据禁止 JSONP 输出
- 面试话术：答「先判断是否还有 JSONP 存量，有则迁移 CORS + 回调白名单，无则明确不做」体现工程判断

```javascript
// 服务端回调名白名单
app.get('/api/jsonp', (req, res) => {
  const cb = req.query.callback;
  if (!/^[\w$.]{1,32}$/.test(cb) || !['jsonpCallback', 'window.cb'].includes(cb)) {
    return res.status(400).end();
  }
  res.type('js').send(`${cb}(${JSON.stringify(publicData)})`);
});
```
