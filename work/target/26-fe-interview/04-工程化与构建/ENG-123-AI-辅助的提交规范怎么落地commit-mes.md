---
title: [ENG-123] AI 辅助的提交规范怎么落地？commit message 生成与校验如何配合？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-123：AI 辅助的提交规范怎么落地？commit message 生成与校验如何配合？
**答**：
- 生成端：把 staged diff 喂给 AI 按团队模板产出符合 Conventional Commits 的提交信息（opencommit 等工具已内置）。
- 校验端：commitlint 卡口不变——AI 写的信息与人工信息适用同一套校验，格式不合格照样拒绝。
- 提示词要点：type 从受限枚举选、正文写动机不写流水账、breaking change 必须带标注。
- 边界：AI 生成的是草稿，提交者要对信息准确性负责，禁止闭眼回车。

```bash
# 1. 生成：diff 喂给 AI，按团队模板产出提交信息草稿
git diff --staged | llm-cli \
  "按 Conventional Commits 生成提交信息：type 限 feat fix chore docs refactor test ci perf，正文一行说明动机" \
  > /tmp/commit-msg.txt

# 2. 校验：AI 草稿同样过 commitlint 卡口
npx commitlint --edit /tmp/commit-msg.txt

# 3. 一体化工具：opencommit 直接完成生成加校验闭环
oco commit
```
