---
title: "[SP-022] Bean 生命周期·@PreDestroy（销毁）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Bean 生命周期 · @PreDestroy（销毁）

- **事实**：销毁回调顺序：@PreDestroy、DisposableBean.destroy、destroy-method
- **原理**：与初始化三回调镜像对称，容器关闭（context.close 或 Boot 优雅停机）时执行
- **常见误区**：
  1. 销毁回调在 JVM 退出时自动调用（错）
  2. @PreDestroy 最后执行（错）
  3. prototype Bean 也有销毁回调（容器不管理 prototype 销毁）（错）
- **工程用法**：释放连接与线程池的正确位置
- **版本锚点**：Spring 文档
