---
title: [WEB-026] memory cache 和 disk cache 有什么区别？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-026：memory cache 和 disk cache 有什么区别？
**答**：
- memory cache 存在内存里，读取极快，但进程结束（关标签页/重启浏览器）就没了；一般存放当前会话频繁使用的资源、图片。
- disk cache 落盘，容量大、跨会话存在，读取有 IO 开销；大文件与不常用资源优先进磁盘。
- 浏览器自己决定放哪，前端无法指定；经验规律：刷新页面多命中 memory，重开页面命中 disk。
- 与之并列还有 Service Worker Cache（可编程、最优先）和 HTTP/2 推送缓存，面试能说清层级即可。

```bash
# 用 curl 验证响应头，判断资源会进哪种缓存
curl -sI https://cdn.example.com/app.js | grep -i cache-control

# DevTools 观察：Network 面板 Size 列
# memory cache  - 命中内存缓存
# disk cache    - 命中磁盘缓存
# 数字（如 15.3 kB）- 真实发生网络请求

# 强制绕过缓存的方法
curl -sI -H 'Cache-Control: no-cache' https://cdn.example.com/app.js
# 或 DevTools 勾选 Disable cache（仅打开 DevTools 期间生效）
```
