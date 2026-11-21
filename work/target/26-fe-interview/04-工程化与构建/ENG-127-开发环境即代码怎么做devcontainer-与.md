---
title: [ENG-127] 开发环境即代码怎么做？devcontainer 与 nix 的思想？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-127：开发环境即代码怎么做？devcontainer 与 nix 的思想？
**答**：
- 思想：环境定义进仓库（声明 node 版本、系统依赖、初始化命令），任何人 clone 后一条命令获得一致环境。
- devcontainer：VSCode/Codespaces 标准，image + features + postCreateCommand 三件套描述环境。
- nix 路线：flake.lock 把系统级依赖也锁版本，比容器更可组合，适合对环境一致性要求极高的团队。
- 关键收益场景：native 依赖编译、多语言工具链（node + java + proto）混搭、新员工首日生产力。

```json
{
  "name": "frontend",
  "image": "mcr.microsoft.com/devcontainers/typescript-node:22",
  "features": {
    "ghcr.io/devcontainers/features/github-cli:1": {}
  },
  "postCreateCommand": "corepack enable && pnpm install && pnpm playwright install --with-deps",
  "customizations": {
    "vscode": {
      "extensions": ["dbaeumer.vscode-eslint", "esbenp.prettier-vscode"]
    }
  },
  "forwardPorts": [5173, 4173]
}
```
