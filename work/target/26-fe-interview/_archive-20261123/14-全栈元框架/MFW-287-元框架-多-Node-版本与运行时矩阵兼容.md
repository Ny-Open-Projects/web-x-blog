---
title: [MFW-287] 多 Node 版本/运行时矩阵兼容治理
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## MFW-287：运行时矩阵兼容

**答**:
- 矩阵构成：Node LTS 版本 × 部署形态（容器镜像基线）× 平台（arm64/x64）——Next/SwC 原生二进制随 Node ABI 变（N-API 缓解大版本差异）
- 治理三件：engines + .nvmrc + CI 矩阵测试（RBL-282 同款搬进元框架仓）；镜像基线统一 digest 锁定（base image 漂移也是漂移）；升级走专项（binding 重编译 + 平台矩阵重跑）
- Edge/Node 双运行时仓的特殊性：同一份代码两个运行时语义差异（URL/globals/Crypto）——条件导入（.node.ts/.edge.ts）+ 双端 lint 边界（server-only 类规则）
- 发布守门：部署前 runner Node 版本断言（错误环境部署直接 fail——版本错配的运行时行为差异极难事后排查）

```text
矩阵：Node LTS × 镜像基线(digest 锁) × arch
双运行时仓：.node.ts/.edge.ts 条件件 + lint 边界
守门：部署前 process.version 断言
```
