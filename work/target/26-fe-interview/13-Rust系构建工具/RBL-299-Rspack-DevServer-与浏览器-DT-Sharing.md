---
title: [RBL-299] Rspack DevServer 的 HMR 链路与浏览器侧细节
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-299：Rspack DevServer 的 HMR 链路与浏览器侧细节

**答**:
- 链路：文件变更 → Rust 增量构建 → 产物生成 → WS 推送 update 清单 → 浏览器 runtime 执行（拉取更新模块 → accept 处理）
- 浏览器侧：HMR runtime 管模块缓存失效与 accept 传播；失败链（无 accept → 传播到 root → 整页 reload）
- 客户端配置：dev.client.overlay（错误浮层）、WebSocket 端口/path 自定义（反向代理场景必须配置正确——代理场景 HMR 连不上是高发问题）
- 多页/多实例：每个 compiler 一个 HMR 通道或共享通道按 id 区分——混乱会导致 A 页面收到 B 页面的更新

```javascript
devServer: {
  client: { overlay: { errors: true, warnings: false }, webSocketURL: 'auto://0/ws' },
  // 反代场景：nginx 把 /ws 转发到 devserver —— path 不配对 HMR 失联
}
```
