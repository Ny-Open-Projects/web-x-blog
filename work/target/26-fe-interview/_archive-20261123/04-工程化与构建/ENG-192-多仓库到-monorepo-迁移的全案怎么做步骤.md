---
title: [ENG-192] 多仓库到 monorepo 迁移的全案怎么做？步骤 风险与回滚？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-192：多仓库到 monorepo 迁移的全案怎么做？步骤 风险与回滚？
**答**：
- 分阶段：试点（1~2 个耦合最深的仓库）→ 打通工具链（workspace 配置 CI 改造）→ 批量搬迁 → 冻结旧仓只读归档。
- 技术要点：git filter-repo 改写路径保留提交历史；旧仓库归档防继续提交；原 PR/issue 留在原平台。
- 风险清单：CI 并发雪崩（全仓触发）、目录级权限模型变化、外部引用断裂、团队 rebase 习惯冲突。
- 回滚预案：每批迁移保留旧仓只读镜像，出问题可临时切回（新提交 cherry-pick 回旧仓），稳定两周后下线旧权限。

```bash
# 多仓库迁移核心步骤 git filter-repo 保留历史
# 1. 原仓库历史改写为子目录前缀
git clone https://git.corp.com/mall/checkout-web.git && cd checkout-web
git filter-repo --to-subdirectory-filter packages/checkout --force

# 2. 并入 monorepo 保留无关历史
cd ../monorepo
git remote add checkout ../checkout-web
git fetch checkout
git merge --allow-unrelated-histories checkout/main --no-edit

# 3. 验证历史可追溯
git log --follow --oneline packages/checkout/src/index.ts | head -5

# 4. 旧仓转只读归档 防止团队继续提交
curl -X PUT "https://git.corp.com/api/v4/projects/mall%2Fcheckout-web" \
  -H "PRIVATE-TOKEN: $GIT_TOKEN" -d '{"archived": true}'
```
