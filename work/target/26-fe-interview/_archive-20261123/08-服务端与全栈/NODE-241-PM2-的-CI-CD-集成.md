---
title: [NODE-241] PM2 的 CI/CD 集成？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-241: PM2 的 CI/CD 集成？
**答**:
- 发布流：CI 构建（tsc/tsup 产物）→ 产物上传（OSS/git tag）→ 目标机 pm2 deploy（内置 git pull + hooks）或自研脚本（pm2 reload 前置健康检查）。
- 健康门禁：reload 后探活（/health 200 且 elu 正常）——失败自动 revert（reload 旧版本目录）。
- 版本目录：releases/<buildId>/ + current 软链（与前端发布同构，NODE-176）——回滚 = 软链切回。
- 环境变量：ecosystem env 分组 + 密钥走配置中心（NODE-150）不落文件。

```bash
# deploy.sh（自研发布脚本核心）
set -e
BUILD_ID=$(git rev-parse --short HEAD)
mkdir -p /app/releases/$BUILD_ID
rsync -a dist/ /app/releases/$BUILD_ID/
ln -sfn /app/releases/$BUILD_ID /app/current
pm2 reload api --update-env
for i in 1..10; do curl -sf http://localhost:3000/health || { sleep 2; continue; }; ok=1; break; done
if [ -z "$ok" ]; then ln -sfn /app/releases/$PREV /app/current; pm2 reload api; exit 1; fi   # 回滚
pm2 save      # 进程表持久化（重启机器后恢复）
```
