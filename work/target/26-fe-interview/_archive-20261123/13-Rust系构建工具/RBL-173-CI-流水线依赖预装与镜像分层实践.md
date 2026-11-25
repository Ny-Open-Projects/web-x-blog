---
title: [RBL-173] CI 流水线的镜像分层与依赖预装实践
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-173：CI 流水线的镜像分层与依赖预装实践

**答**：
- 思路：把"几乎不变"的东西（Node 版本、pnpm、Rust 工具二进制、全局 CLI）固化进自定义 runner 镜像，把"经常变"的（项目 node_modules）留给缓存层——install 阶段从分钟级压到 10s 内。
- 镜像内容分层：base（OS+Node+corepack）→ tools（Rspack/Bun/esbuild 二进制、turbo、oxlint）→ 无项目内容。项目仓库只声明所需版本，镜像用 digest 锁定。
- 维护节奏：镜像按月/按需重建（工具版本升级驱动），CI 侧用镜像 tag + 版本对齐检查（本地与 CI 工具版本 drift 检测）。
- 与依赖缓存的关系：镜像装不了项目依赖（每项目不同），所以 node_modules 仍走 lockfile-keyed 缓存；镜像解决的是"全局工具安装"而非"项目依赖安装"。
- 追问钩子：能说出镜像更新的迁移风险——镜像一换全仓库 CI 行为变，要灰度（部分 repo 先切）并保留旧镜像 tag 回滚。

```dockerfile
# ci-base-image/Dockerfile —— 自定义 runner 镜像
FROM node:22-bookworm-slim
RUN corepack enable && corepack prepare pnpm@9.12.0 --activate
# Rust 系工具：直接放二进制（从官方 release 下载，锁版本）
ARG RSPACK_VERSION=0.7.4
RUN curl -fsSL https://github.com/xxx/rspack/releases/download/v${RSPACK_VERSION}/rspack-linux-x64 \
      -o /usr/local/bin/rspack && chmod +x /usr/local/bin/rspack
RUN curl -fsSL https://bun.sh/install | bash -s "bun-v1.1.20" \
 && ln -s ~/.bun/bin/bun /usr/local/bin/bun
RUN npm i -g turbo@2.2 @oxlint/cli@0.9   # 任务编排与快检工具
# 校验层：镜像内版本自检脚本
COPY check-tools.sh /usr/local/bin/check-tools.sh
RUN /usr/local/bin/check-tools.sh        # 版本不符直接让镜像构建失败
```
