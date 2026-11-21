---
title: "[RD-002] String·SDS（编码）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## String · SDS（编码）

- **事实**：String 底层是 SDS（简单动态字符串）支持二进制安全与 O(1) 长度
- **原理**：SDS 记录长度字段与预分配空间，免 strlen 与缓冲区溢出，可存图片等二进制数据
- **常见误区**：
  1. SDS 就是以 \0 结尾的 C 字符串（错）
  2. SDS 不支持二进制（错）
  3. 长度获取 O(n)（错）
- **工程用法**：缓存序列化对象/计数器场景
- **版本锚点**：SDS 实现
