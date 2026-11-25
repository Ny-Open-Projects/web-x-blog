---
title: [ENG-070] 脚手架如何做版本升级？为什么破坏性升级要配 codemod？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-070：脚手架如何做版本升级？为什么破坏性升级要配 codemod？
**答**：
- 升级分两档：小版本公告自动更新（npx 每次拉最新）；大版本提供 migrate 命令自动迁移。
- 破坏性变更靠人工改代码必漏，codemod（jscodeshift）基于 AST 批量改写，产出可 review 的 diff。
- 迁移脚本与脚手架同仓库同版本发布：npx my-cli migrate router-v6，保证版本对齐。
- 升级体验闭环：check 命令探测项目与最新模板差异 → migrate 自动改 → 人工确认 → 提交。

```bash
# 1. 探测项目与最新脚手架版本的配置差异
npx my-cli check

# 2. 破坏性升级执行配套 codemod（脚本与脚手架同版本发布）
npx my-cli migrate router-v6

# 3. codemod 底层示例：jscodeshift 执行 AST 转换
npx jscodeshift -t transforms/router-v6.ts --extensions=ts,tsx src/

# 4. 迁移后人工 review diff，再走正常提交门禁
git diff --stat
```
