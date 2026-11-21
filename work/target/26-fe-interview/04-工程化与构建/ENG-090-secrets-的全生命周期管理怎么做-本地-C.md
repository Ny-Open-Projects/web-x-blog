---
title: [ENG-090] secrets 的全生命周期管理怎么做（本地/CI/生产）？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-090：secrets 的全生命周期管理怎么做（本地/CI/生产）？
**答**：
- 本地：.env 不入库 + .env.example 模板入库；敏感值用 1Password CLI/direnv 注入，杜绝粘贴进聊天与 issue。
- CI：只经平台 secrets（GitHub Actions secrets/GitLab CI variables）注入环境变量，禁止 echo、禁止写进日志与 artifacts。
- 生产：K8s Secret/云 KMS/Vault 管理，应用启动时挂载；CI 对生产凭据最小授权（只给部署所需权限）。
- 轮换与审计：凭据定期轮换、按人/服务独立发放；一旦泄漏立即吊销而不是改代码隐藏。

```yaml
# GitHub Actions 中 secrets 的正确用法
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production        # 环境级 secrets，可加人工审批
    steps:
      - name: deploy
        env:
          DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}   # 只经环境变量传递
          DEPLOY_HOST: ${{ vars.DEPLOY_HOST }}        # 非敏感值用 vars
        run: ./scripts/deploy.sh
        # 禁止：echo $DEPLOY_TOKEN、写进文件、放进 npm script 参数
```
