---
title: [WEB-467] Cookie 丢失的排查 SOP
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-467：Cookie 丢失的排查 SOP

**答**：
- 排查顺序：① 请求根本没带（Domain/Path 不匹配、SameSite 拦截）② 浏览器拒收（Secure 头但页面是 http、SameSite=None 缺 Secure）③ 被设置又被覆盖（同名不同 Path/Domain）④ 第三方 Cookie 被 Chrome 分区/禁用
- SameSite 是头号元凶：跨站跳转回来带的 Cookie 需要 `SameSite=None; Secure`；子域跳转（site 同站）用 Lax 即可
- 名称冲突：同名 Cookie 不同 Path 会并存，浏览器发送时按「更长 Path 优先」排序，服务端读到旧值，看起来像「改了不生效」
- 工具方法：DevTools Application 面板看 Cookie 实际落盘情况；Network 面板看请求 Cookie 头（被发送的是浏览器视角真实状态）
- Chrome 新特性干扰：CHIPS 分区 Cookie、3PC 退出计划，嵌入式 iframe 场景必须迁移到 Partitioned 或 token 方案

```bash
# 检查响应头里的 Set-Cookie 是否会被接受（⚠ 标记）
curl -sI 'https://api.example.com/login' | grep -i set-cookie
# Set-Cookie: sid=1; SameSite=None  ← 缺 Secure，Chrome 会拒收
```
