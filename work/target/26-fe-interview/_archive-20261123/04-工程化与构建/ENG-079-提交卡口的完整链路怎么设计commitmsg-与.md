---
title: [ENG-079] 提交卡口的完整链路怎么设计？commit-msg 与 pre-push 如何分层？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-079：提交卡口的完整链路怎么设计？commit-msg 与 pre-push 如何分层？
**答**：
- 分层原则：越早的 hook 越快，把重活下沉，让开发者不被慢卡口折磨到用 --no-verify 绕过。
- commit-msg 只校验提交信息（commitlint，毫秒级）；pre-commit 只查暂存区文件（lint-staged，秒级）。
- pre-push 跑重门禁：单测、typecheck、build，此时改动已成型，失败代价最低。
- 本地 hook 可被 --no-verify 绕过，服务端 pre-receive 钩子（见 Git 深水区）是规范落地的最后一道。

```bash
# .husky/commit-msg —— 只做提交信息校验，毫秒级
npx --no -- commitlint --edit "$1"

# .husky/pre-commit —— 只校验暂存区文件，秒级
npx lint-staged

# .husky/pre-push —— 推送前跑重门禁：单测与类型检查
pnpm test run
pnpm typecheck
```

---

## 第十九章 Git 深水区（ENG-080 ~ ENG-086）
