---
title: [R19-225] Server Action 怎么调试？本地开发有哪些实用手段？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-225：Server Action 怎么调试？
**答**：
- Network 面板：action 请求以 POST 呈现（名字为 action id），看 payload（Flight 编码）与响应；DevTools 的 "Server Actions" 分组（Next 15+）显示耗时。
- 服务端日志：action 内 console.log 直接打到终端（不是浏览器），加 requestId 串联。
- 断点：VS Code debug attach Node 进程，action 代码可断点；hot reload 生效。
- 常见问题定位：序列化错误看报错对象类型；redirect 失效查 try/catch；鉴权失败打 session 快照（脱敏）。
- 本地复现生产问题：用 staging 数据 + 同配置本地跑，或远程调试（端口转发）。
