---
title: [RBL-161] Rust 系工具在 CI 里怎么装得快？二进制分发机制利用
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-161：Rust 系工具在 CI 里怎么装得快？二进制分发机制利用

**答**：
- 核心思路：这些工具（Rspack/SWC/Bun/esbuild）在 npm 包里分发平台二进制，"安装"只是下载几 MB 的 .node/可执行文件，理论秒级；慢往往出在 npm 把整个 optionalDependencies 元数据全解析一遍。
- 提速手段：1) 用 pnpm --frozen-lockfile + store 缓存，避免重复解网络包；2) 单独缓存平台二进制目录（node_modules/@swc、@rspack）；3) Bun 官方安装脚本（curl bun.sh）直接装二进制，绕过 npm；4) 镜像内置：把常用 Rust 工具直接打进 CI Docker 基础镜像，install 阶段归零。
- 版本策略：CI 镜像内置要锁版本，本地与 CI 版本 drift 会造成"本地能跑 CI 挂"；用 package.json 精确版本（不带 ^）配合镜像更新流程。
- musl/glibc 与架构问题在 CI 尤其常见（见 RBL-144）：Alpine runner 必须 musl 变体，跨架构（arm64 runner）要显式装对应包。
- 追问钩子：可以量化——对比 npm ci（全量）与命中缓存 + 二进制内置的 install 时间，说明优化收益集中在哪。

```yaml
# GitHub Actions：分层提速
- uses: actions/setup-node@v4
  with: { node-version: '22' }
- uses: pnpm/action-setup@v4
  with: { version: 9 }
- uses: actions/cache@v4
  with:
    path: ~/.local/share/pnpm/store    # pnpm store 缓存
    key: pnpm-${{ hashFiles('pnpm-lock.yaml') }}
- run: pnpm install --frozen-lockfile
# Bun 工具直接官方脚本装（秒级，不走 npm）
- run: curl -fsSL https://bun.sh/install | bash -s "bun-v1.1.20"
```
