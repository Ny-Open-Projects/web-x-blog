---
title: [ENG-042] GitHub Actions 如何实现自动部署 CD？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-042：GitHub Actions 如何实现自动部署 CD？
**答**：
- 触发条件用 release published 或 tag push，保证只有版本发布才上线。
- 敏感信息放 repo 的 Secrets 与 Variables：SSH 私钥、目标主机、环境变量。
- 构建产物用 rsync/scp 推到服务器，或打成 Docker 镜像推到镜像仓库。
- environment: production 可以配置人工审批门禁。

```yaml
name: Deploy

on:
  release:
    types: [published]

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
      - run: pnpm install --frozen-lockfile
      - run: pnpm build
        env:
          VITE_API_BASE: ${{ vars.VITE_API_BASE }}

      - name: 上传产物到服务器
        run: |
          mkdir -p ~/.ssh
          echo "${{ secrets.SSH_KEY }}" > ~/.ssh/id_ed25519
          chmod 600 ~/.ssh/id_ed25519
          rsync -avz --delete dist/ deploy@${{ secrets.DEPLOY_HOST }}:/var/www/app
```
