---
title: [ENG-078] husky v9+ 与 lint-staged 的最新配置怎么写？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-078：husky v9+ 与 lint-staged 的最新配置怎么写？
**答**：
- v9 大幅简化：npx husky init 一条命令生成 .husky/pre-commit，脚本里只剩一行调用，去掉了废弃的 add。
- 目录 .husky/ 下的文件就是纯 shell 脚本，直接写要执行的命令，不再需要 source 配置头。
- lint-staged 负责只处理 git 暂存区文件：改哪个文件跑哪个工具，全量 lint 才留给 CI。
- v9 兼容 core.hooksPath 机制，monorepo 中注意在根目录初始化一次即可。

```bash
# 初始化（v9 一条命令搞定）
npx husky init
# pre-commit 文件内容只需一行
echo "npx lint-staged" > .husky/pre-commit
```

```json
{
  "lint-staged": {
    "*.{ts,tsx}": ["eslint --fix", "prettier --write"],
    "*.{css,scss}": ["stylelint --fix"],
    "*.{json,md,yml}": ["prettier --write"]
  }
}
```
