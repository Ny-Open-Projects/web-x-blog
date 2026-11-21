---
title: [WEB-468] 跨域报错的排查 SOP，CORS 报错怎么读
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-468：跨域报错的排查 SOP，CORS 报错怎么读

**答**：
- 第一步分清四类报错文案：No 'Access-Control-Allow-Origin'（响应缺头）、Method/Headers not allowed（预检不通过）、credentials mode include（缺 Allow-Credentials 或 origin 是 *）、redirect not allowed（302 到未配置域）
- 排查顺序：先看 Network 面板 OPTIONS 预检是否发出去、状态码、响应头 trio（Allow-Origin / Allow-Methods / Allow-Headers）逐一对照实际请求
- 隐藏元凶排行：网关剥离自定义头（服务端明明配了，网关拦了）、Nginx 重复追加 Allow-Origin 出现两个值（浏览器判非法）、错误响应路径没配 CORS（401/500 时无头，前端以为是跨域）
- credentials 场景铁律：Allow-Origin 必须是具体 origin 不能是 *，且必须带 Allow-Credentials: true
- 快速自检：用 curl 模拟预检，绕过浏览器看服务端真实返回

```bash
curl -sI -X OPTIONS 'https://api.example.com/x' \
  -H 'Origin: https://app.example.com' -H 'Access-Control-Request-Method: POST' \
  -H 'Access-Control-Request-Headers: x-token' | grep -i access-control
```
