---
title: [SCN-108] 团队同时存在 git flow、自定义分支和直接 push main，发布节奏混乱，如何收敛到 trunk-based？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-108：团队同时存在 git flow、自定义分支和直接 push main，发布节奏混乱，如何收敛到 trunk-based？
**答**：
- 渐进三步：先保护 main（禁直推、PR + CI 绿才能合），未完成功能用 Feature Flag 隔离；再约束短生命周期分支（≤2 天、合入前 rebase 保持线性）；最后发布从 main 拉 release 分支或直接 tag，回滚靠 revert。
- trunk-based 的前提是 CI 足够快（<10 分钟）与开关文化，缺一不可，否则大家会被迫开长分支。
- 存量长分支给截止日期，逐个拆小合入，不搞一刀切强删。

```bash
# trunk-based 落地：分支保护 + 短分支 + release 冻结 + revert 回滚
# 1) main 保护：只允许 PR 合入，CI 通过 + 1 人审批，禁止强推
gh api repos/:owner/:repo/branches/main/protection -X PUT --input - <<'EOF'
{ "required_status_checks": {"strict": true, "contexts": ["ci"]},
  "required_pull_request_reviews": {"required_approving_review_count": 1},
  "allow_force_pushes": false, "enforce_admins": true }
EOF

# 2) 短生命周期分支：当天创建当天合，最长不超过 2 天
git checkout -b feat/quick-search main
git fetch origin && git rebase origin/main    # 合入前 rebase 保持线性

# 3) 发布：从 main 拉 release 分支，修复 cherry-pick 进入后打 tag
git checkout -b release/v2.3.0 main
git cherry-pick <bugfix-sha>
git tag v2.3.0 && git push origin v2.3.0

# 4) 出问题回滚：revert merge commit，而不是删分支重来
git revert -m 1 <merge-commit-sha>
```
