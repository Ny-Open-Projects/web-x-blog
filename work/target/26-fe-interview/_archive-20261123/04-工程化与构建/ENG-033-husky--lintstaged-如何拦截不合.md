---
title: [ENG-033] husky + lint-staged 如何拦截不合规提交？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-033：husky + lint-staged 如何拦截不合规提交？
**答**：
- husky 把 git hooks 目录指向仓库内脚本，团队共享同一套钩子。
- lint-staged 只对 git 暂存区的文件跑 lint --fix 与 prettier，速度快且不碰未改动文件。
- pre-commit 钩子执行 npx lint-staged，失败则提交中止。
- 好处：问题在本地提交前暴露，不让 CI 白白跑一轮。

```bash
# 安装并初始化 husky
npm install --save-dev husky lint-staged
npx husky init

# pre-commit 钩子内容：对暂存区文件执行检查
echo "npx lint-staged" > .husky/pre-commit

# package.json 中配置 lint-staged 规则：
# "lint-staged": {
#   "*.{js,jsx,ts,tsx}": ["eslint --fix", "prettier --write"],
#   "*.{css,scss,json,md}": ["prettier --write"]
# }

git add package.json
git commit -m "chore: add lint-staged"
```
