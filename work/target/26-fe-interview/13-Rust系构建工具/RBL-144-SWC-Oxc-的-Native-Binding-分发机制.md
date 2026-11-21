---
title: [RBL-144] SWC/Oxc 的平台 binding 是怎么分发的？装机报错怎么排查
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-144：SWC/Oxc 的平台 binding 是怎么分发的？装机报错怎么排查

**答**：
- 机制：npm 包本体是空壳 + optionalDependencies 声明各平台二进制包（@swc/core-linux-x64-gnu、@swc/core-darwin-arm64、musl 变体等），npm/pnpm 按当前平台 OS+CPU 只装对应一个。
- 常见报错 `failed to load native binding` 的原因：1) 镜像/CI 跳过了 optional deps（--no-optional）；2) musl 与 glibc 混用（Alpine 必须装 musl 变体）；3) pnpm 平台过滤配置（supportedArchitectures）漏了 CI 机器架构；4) Node 版本过老 N-API 不兼容。
- 排查路径：先 `npm ls @swc/core` 与 `node -e "require('@swc/core')"` 复现，再检查平台包是否真的装上（ls node_modules/@swc/），最后核对 libc（ldd --version）。
- Oxc/Rolldown 同机制（napi-rs），排查思路一致；Rust 工具链统一踩这条坑。
- 追问钩子：CI 缓存 node_modules 时要缓存"所有可能平台的产物"或按平台 key 分缓存，否则跨架构 runner 复用缓存必炸。

```bash
# 排查清单（复制即用）
node -e "console.log(process.platform, process.arch)"   # 平台信息
npm ls @swc/core && ls node_modules/@swc/                # 平台包是否在
npm install @swc/core-linux-x64-gnu --force --no-save    # 手动补装验证

# .npmrc（Alpine/CI 常用修复）
# musl 环境：
#   libc=musl
# pnpm 跨平台 CI：
#   supported-architectures[] = os=current, os=linux, cpu=current, cpu=x64, cpu=arm64, libc=glibc, libc=musl
```
