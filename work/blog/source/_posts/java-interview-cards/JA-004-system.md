---
title: "[JA-004] Spring AI·system（提示词）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · system（提示词）

- **事实**：ChatClient 用 .system(...) 设系统提示、.user(...) 设用户消息，链式可多次调用
- **原理**：系统提示承载角色与规则、用户消息承载当次输入，分离设置是 prompt 工程在框架层的落点
- **常见误区**：
  1. system 与 user 必须合并成一个字符串（错）
  2. 只能设置一次 user（错）
  3. system 在 call 时才被读取（错）
- **工程用法**：角色定义与输出规则放 system
- **版本锚点**：Spring AI 1.0 GA
