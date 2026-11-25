---
title: [ENG-132] 构建参数怎么 CLI 化？环境编排怎么落地？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-132：构建参数怎么 CLI 化？环境编排怎么落地？
**答**：
- 构建命令散落在 README 里没人维护：把 build 参数（目标环境、sourcemap 开关、是否上传）CLI 化，脚本统一解析。
- 环境编排是一个命令串起多个环境的动作：build → 上传 → 触发冒烟，全部脚本化而非人肉点击。
- 参数落到 CI 可复用：CI 只是调同一个脚本传不同 flag，本地与线上行为一致，避免"本地好的 CI 坏的"。
- 非法参数 fail fast 并打印 usage；危险组合（prod + sourcemap）在脚本里直接卡死。

```bash
#!/usr/bin/env bash
# scripts/build.sh —— 构建参数 CLI 化与环境编排
set -euo pipefail

ENV="test"; SOURCEMAP=false; SKIP_UPLOAD=false
while [[ $# -gt 0 ]]; do
  case "$1" in
    --env) ENV="$2"; shift 2 ;;                    # test | staging | prod
    --sourcemap) SOURCEMAP=true; shift ;;
    --skip-upload) SKIP_UPLOAD=true; shift ;;
    *) echo "未知参数 $1"; echo "用法: build.sh --env staging [--sourcemap] [--skip-upload]"; exit 1 ;;
  esac
done

case "$ENV" in
  test) VITE_API=https://api-test.corp.com ;;
  staging) VITE_API=https://api-staging.corp.com ;;
  prod) VITE_API=https://api.corp.com ;;
  *) echo "非法环境 $ENV"; exit 1 ;;
esac

VITE_API=$VITE_API VITE_SOURCEMAP=$SOURCEMAP npm run build

if [[ "$ENV" == "prod" && "$SOURCEMAP" == "true" ]]; then
  echo "禁止 prod 构建携带 sourcemap sourcemap 只进内部监控平台"; exit 1
fi
[[ "$SKIP_UPLOAD" == "false" ]] && node scripts/upload.js --env "$ENV" ./dist
```
