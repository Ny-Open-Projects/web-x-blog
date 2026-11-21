---
title: [RBL-312] 构建配置的 secret 泄露防护
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-312：构建配置的 secret 泄露防护

**答**:
- 泄露通道一：DefinePlugin 注入 secret 进前端产物（前端包是公开的！）——前端只允许 public 配置，secret 走服务端/边缘注入
- 通道二：sourcemap 带源码（含 .env 引用）——map 不进公网产物目录；通道三：构建日志 echo env；通道四：Docker 层缓存残留（多阶段 builder 层含 secret，镜像导出会带）
- 防护机制：构建期 secret 扫描（产物 grep 高熵字符串/已知前缀）、env 白名单（只允许白名单变量进 define）、CI secret 用 masking（日志自动脱敏）
- 事故响应：泄露即轮换（secret 视为已泄露）+ 产物下架 + 泄露面排查

```text
红线：前端产物不含任何 secret；验证 = 构建后自动扫描产物
Docker：secret 只在 builder 层且最终镜像不含 builder 层
```
