---
title: [OPS-062] Secrets 管理有哪些原则？CI 里怎么正确注入？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-062：Secrets 管理有哪些原则？CI 里怎么正确注入？
**答**：
- 铁律：密钥不进代码库（含 git 历史）、不进日志、不进镜像层、不进前端产物——前端代码是公开的，任何进入 dist 的"密钥"都等于公开。
- CI 注入：GitHub Actions Secrets / GitLab Variables / Jenkins credentials，运行时以环境变量出现，配合 mask 防日志泄露。
- 需要 pin 与轮换：最小权限 token、定期轮换、离职回收；组织级 secret 扫描（gitleaks/trufflehog）进 CI 与 push 保护。
- 前端特有的坑：.env.production 误提交、sourcemap 里带出 env 值、错误上报把 token 打进 Sentry。

```yaml
# .github/workflows/secrets-demo.yml：CI 中正确使用 secrets 的姿势
name: secrets-demo
on: [push]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # 正确 1：secrets 通过 env 注入，永不写进命令行参数（防 ps 可见与日志打印）
      - name: Deploy with token
        env:
          DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}   # 仅此 job 的进程可见
          CDN_TOKEN: ${{ secrets.CDN_PURGE_TOKEN }}
        run: |
          ./scripts/deploy.sh   # 脚本内部读 $DEPLOY_TOKEN，不 echo
          curl -sS -H "Authorization: Bearer $CDN_TOKEN" https://cdn.example.com/api/prefetch

      # 正确 2：临时文件类密钥（SSH key）用完立即清理
      - name: SSH deploy
        env: { SSH_KEY: "${{ secrets.DEPLOY_KEY }}" }
        run: |
          echo "$SSH_KEY" > /tmp/k && chmod 600 /tmp/k
          ssh -i /tmp/k deploy@web01 'true'
          shred -u /tmp/k          # 用完销毁

      # 错误示范（勿抄）：
      # run: curl -H "Auth: ${{ secrets.DEPLOY_TOKEN }}" ...   # 展开会进日志
      # run: echo "token is $DEPLOY_TOKEN"                     # 打印即泄露

# 配套纪律：
#   - gitleaks 进 pre-commit 与 CI，push protection 开启
#   - secrets 轮换周期 90 天，人员离职 24h 内回收
#   - .env* 全部 .gitignore，仓库只留 .env.example（无真实值）
```
