---
title: "[DF-043] RPC·protobuf（gRPC）"
date: 2026-11-18
categories: [Java面试, 分布式]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## RPC · protobuf（gRPC）

- **事实**：gRPC：HTTP/2 多路复用+protobuf 二进制序列化（跨语言 IDL）
- **原理**：HTTP/2 流复用单连接并发多请求，protobuf 体积小解析快（IDL 生成强类型代码），云原生与跨语言场景主流
- **常见误区**：
  1. gRPC 用 HTTP/1.1（错）
  2. protobuf 可读性最好（错）
  3. gRPC 只支持同步（错）
- **工程用法**：跨语言 RPC 选型
- **版本锚点**：实战共识
