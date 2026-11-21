---
title: [RBL-364] Rust 构建工具的交叉编译与多平台分发
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-364：Rust 构建工具的交叉编译与多平台分发

**答**:
- 目标矩阵：平台（darwin/linux/win）× 架构（x64/arm64）× libc（gnu/musl）——musl（静态链接）用于 Alpine/无 glibc 环境
- CI 交叉编译：GitHub Actions 矩阵 + cross 工具（容器内交叉编译）——macOS arm64 需原生 runner（交叉到 arm64-macos 支持差）
- 分发链路：编译产物 → 平台包（optionalDependencies）或独立二进制（curl 安装脚本）→ 安装时按 process.platform/arch 选包 → fallback 编译（无预编译包时源码编译，慢但兜底）
- 校验：每平台产物冒烟（最小构建用例）+ 二进制 hash 记录（供应链审计）

```text
矩阵：平台×架构×libc → CI 矩阵编译 → optionalDependencies 分发
兜底：无预编译包 → 源码编译（慢）
校验：每平台冒烟 + 二进制 hash
```
