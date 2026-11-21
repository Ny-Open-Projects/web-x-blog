---
title: [ARC-020] pnpm workspace 的目录结构如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-020：pnpm workspace 的目录结构如何设计？
**答**：
- `apps/` 放可部署产物（站点、服务），`packages/` 放被复用的库；二者界限必须清晰，禁止反向引用。
- 包命名用 scope（`@corp/xxx`），内部依赖一律 `workspace:*` 协议，天然防幽灵依赖。
- 配置文件（tsconfig/eslint/prettier）收敛到 `packages/tsconfig` 等内部包，避免根目录复制粘贴。

```text
monorepo/
├── apps/
│   ├── web-shop/          # C 端商城（可部署）
│   ├── admin/             # 中后台（可部署）
│   └── ssr-server/        # BFF/SSR 服务
├── packages/
│   ├── ui/                # @corp/ui 组件库
│   ├── design-tokens/     # @corp/design-tokens Token 源
│   ├── request/           # @corp/request 请求层
│   ├── utils/             # @corp/utils 纯函数
│   └── tsconfig/          # @corp/tsconfig 配置即包
├── tooling/               # eslint-config / scripts（不发布）
├── pnpm-workspace.yaml
├── turbo.json
└── package.json
```

```yaml
# pnpm-workspace.yaml
packages:
  - apps/*
  - packages/*
  - tooling/*
# 根 package.json 关键配置：
# "packageManager": "pnpm@9.x"  锁定包管理器
# 内部引用一律写 "@corp/ui": "workspace:*"
```
