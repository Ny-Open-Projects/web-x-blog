---
title: [WEB-082] Chromium 的多进程模型由哪些进程组成？各自负责什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-082：Chromium 的多进程模型由哪些进程组成？各自负责什么？
**答**：
- 浏览器主进程（Browser）：负责书签/地址栏 UI、网络请求的调度入口、磁盘存储、子进程管理，是唯一有完整系统权限的进程。
- 渲染进程（Renderer）：每个站点（隔离后）一个，跑 Blink 排版引擎与 V8，页面 JS 全部在这里执行。
- GPU 进程：统一负责所有进程的合成与光栅化指令，3D/2D 加速都在此收口。
- 网络服务进程（Network Service）：socket 池、DNS、HTTP 缓存、HSTS 都在这里；另有 Utility 进程承担音频、存储等杂项。
- 设计动机：隔离故障（一个标签崩溃不拖垮浏览器）与隔离权限（渲染进程无权碰网络与文件）。

```mermaid
graph TD
    B[浏览器主进程<br/>地址栏与书签 UI<br/>调度与权限中枢]
    B --> N[网络服务进程<br/>socket 池与 DNS<br/>HTTP 缓存与 HSTS]
    B --> R1[渲染进程 A<br/>站点 one 的 Blink 与 V8]
    B --> R2[渲染进程 B<br/>站点 two 的 Blink 与 V8]
    B --> G[GPU 进程<br/>合成与光栅化指令收口]
    B --> U[Utility 进程<br/>音频解码与存储等杂项]
    R1 -->|IPC 请求网络| N
    R2 -->|IPC 请求网络| N
    R1 -->|提交帧| G
    R2 -->|提交帧| G
```
