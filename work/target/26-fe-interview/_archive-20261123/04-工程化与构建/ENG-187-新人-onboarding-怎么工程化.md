---
title: [ENG-187] 新人 onboarding 怎么工程化？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-187：新人 onboarding 怎么工程化？
**答**：
- 目标量化：day1 提交第一行代码 week1 上线一个页面；核心指标是首次合入耗时。
- 三件套：一键环境脚本 setup.sh（nvm/corepack/依赖/种子数据/冒烟验证）、good-first-task 低风险任务池、buddy 导师制（首个 PR 必须导师 review）。
- 文档反熵：新人卡点即提 issue 修文档，把每个新人当文档的回归测试。
- 每次卡点数据用于改进 onboarding 流程本身，形成闭环。

```bash
#!/usr/bin/env bash
# scripts/setup.sh —— 新人 day1 一键环境
set -euo pipefail
echo "1/5 检查基础工具"
command -v node >/dev/null || { echo "请先安装 nvm"; exit 1; }
nvm use
corepack enable && corepack prepare pnpm@9 --activate

echo "2/5 安装依赖"
pnpm install

echo "3/5 初始化本地数据"
pnpm db:seed

echo "4/5 预热构建缓存"
pnpm exec turbo build --filter=web || pnpm build

echo "5/5 冒烟验证"
pnpm -F web dev > /dev/null 2>&1 & sleep 6
curl -sf http://localhost:5173 > /dev/null \
  && echo "OK dev server 正常 新人环境就绪" \
  || { echo "FAIL 请联系 buddy"; exit 1; }
echo "下一步 从 docs/onboarding/first-task.md 领取首个任务"
```
