---
title: [RBL-112] Bun 的 lockfile 机制与 npm/pnpm 迁移兼容性？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-112：Bun 的 lockfile 机制与 npm/pnpm 迁移兼容性？
**答**：
- 原生格式：bun.lockb（二进制，含完整依赖树与 integrity 校验）与 bun.lock（文本 JSONC，新默认），两者都支持确定性安装。
- 迁移：bun install 可直接读取 package.json 与 npm 的 package-lock.json（不读 pnpm-lock 的部分语义），首次迁移生成自己的 lockfile；版本解析尽量与 npm 一致，但复杂 overrides/resolutions 场景要核对。
- workspace：原生支持 workspaces（package.json workspaces 字段），monorepo 可直接替换 pnpm；软链接布局与 pnpm 的隔离结构不同（bun 默认 hoist 风格）。
- frozen-lockfile：CI 用 --frozen-lockfile 保证不改动依赖树。
- 风险点：团队工具链切换要同步文档与 CI；私有 registry/自建镜像的认证（.npmrc）支持要验证。
- 追问钩子：lockfile 切换意味着回滚成本（恢复 package-lock 需重新 npm install 校验），迁移要在独立分支验证依赖树 diff。

```bash
# 迁移流程
bun install                     # 读 package.json / package-lock.json，生成 bun.lock
git diff --stat                 # 确认依赖版本 diff
bun install --frozen-lockfile   # CI 严格模式
bun outdated                    # 依赖更新检查
```
