---
title: [ENG-085] 服务端 git hooks 怎么做强制卡口？pre-receive 实例？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-085：服务端 git hooks 怎么做强制卡口？pre-receive 实例？
**答**：
- 本地 hook 挡不住 --no-verify，规范要强制落地必须靠服务端：GitLab server hook、Gitea/Gitolite pre-receive。
- pre-receive 从 stdin 读入 oldrev newrev refname 三元组，逐个 ref、逐个提交校验，不合规直接 exit 1 拒绝推送。
- 常见卡口：main 禁直推、提交信息规范、禁止 force push 保护分支、大文件扫描。
- 注意性能与体验：拒绝信息要写清楚修复方式，重检查（全量 lint/test）放 CI 而不是 pre-receive。

```bash
#!/bin/bash
# 服务端 pre-receive 钩子
ZERO=0000000000000000000000000000000000000000
while read oldrev newrev refname; do
  # 卡口一：main 禁止直接推送，必须走 MR
  if [[ "$refname" == "refs/heads/main" && "$oldrev" != "$ZERO" ]]; then
    echo "main 禁止直接推送，请走 Merge Request" >&2
    exit 1
  fi
  # 卡口二：提交信息必须符合 Conventional Commits
  for commit in $(git rev-list "$oldrev..$newrev"); do
    msg=$(git log -1 --format=%s "$commit")
    if ! grep -qE '^(feat|fix|chore|docs|refactor|test|ci|perf|style|revert)(\(.+\))?: ' <<< "$msg"; then
      echo "提交 $commit 信息不符合规范：$msg" >&2
      exit 1
    fi
  done
done
exit 0
```
