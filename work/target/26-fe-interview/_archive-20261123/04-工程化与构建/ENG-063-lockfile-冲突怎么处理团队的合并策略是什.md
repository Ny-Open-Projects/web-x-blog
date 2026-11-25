---
title: [ENG-063] lockfile 冲突怎么处理？团队的合并策略是什么？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-063：lockfile 冲突怎么处理？团队的合并策略是什么？
**答**：
- 冲突根因：两个分支各自 add/update 依赖，git 无法三方合并 lockfile 中的大段哈希块。
- 处理原则：lockfile 永远由工具生成，禁止手工编辑；冲突时先解决 package.json，再按它重新解析。
- 快速做法：保留任意一侧（--theirs），跑 pnpm install --lockfile-only 重算，结果就是正确合并。
- 预防：分支生命周期短、依赖变更集中在少数人、CI 开 frozen-lockfile 校验兜底。

```bash
# 冲突现场：先解决 package.json 的冲突，然后重算 lockfile
git checkout --theirs pnpm-lock.yaml
pnpm install --lockfile-only     # 按 package.json 重新解析，生成正确的合并结果
git add pnpm-lock.yaml

# 验证合并结果可复现（CI 同款命令）
pnpm install --frozen-lockfile --dry-run

# 团队约定写进 CONTRIBUTING：lockfile 只由工具生成
echo "pnpm-lock.yaml merge=ours" >> .gitattributes  # 可选：减少冲突提示面
```
