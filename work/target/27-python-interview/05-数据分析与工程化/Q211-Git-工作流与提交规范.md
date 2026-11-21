---
title: [Q211] Git 工作流与提交规范
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q211 · Git 工作流与提交规范

> 难度:★★☆ | 标签:git, Conventional Commits

**问**:团队用什么 Git 分支模型?commit message 有规范吗?

**答**:中小团队主流是 **GitHub Flow**:main 保持可发布,功能走短命 feature 分支 → PR → review → squash merge → 删除分支;发布节奏需要版本管理的用 **GitFlow**(develop/release/hotfix),但分支多、合并重,多数互联网团队用不上。提交规范推荐 **Conventional Commits**:`type(scope): subject`,type 如 feat/fix/refactor/test/docs/chore,好处是 changelog 与语义化版本可自动生成。实践要点:提交原子化(一个提交一个意图)、提交前跑测试不用 --no-verify、main 只通过 PR 进入、用 rebase 保持线性历史或 merge 保留真实脉络——二选一保持团队一致。

```bash
# 提交规范示例:非 python 文件
feat(auth): 支持 OAuth2 登录
fix(api): 修复分页参数越界导致 500
refactor(core): 抽取价格计算纯函数
test(cart): 补充优惠券叠加的参数化用例
chore(deps): 升级 httpx 到 0.27
```

```python
# file: code/05_数据分析与工程化/q211_commit_check.py
import re

PATTERN = re.compile(
    r"^(feat|fix|refactor|test|docs|chore|perf|ci)(\(.+\))?: .{1,72}$"
)

def valid_commit(msg: str) -> bool:
    return bool(PATTERN.match(msg))

def test_conventional_commits():
    assert valid_commit("feat(auth): 支持 OAuth2 登录")
    assert valid_commit("fix: 修复越界")
    assert not valid_commit("改了点东西")
    assert not valid_commit("feat: " + "x" * 100)
```

**追问**:
- Conventional Commits 的实际收益?——changelog 自动生成、版本号自动推断(semver)、变更检索;前提是团队真的按 type 提交。
- 为什么用 squash merge?——feature 分支的中间提交(WIP、fix typo)不进 main,main 历史一条 commit 一个功能,bisect 友好。
- hotfix 流程怎么走?——从 main 拉 hotfix 分支修复→测试→merge 回 main 并打 tag;有 develop 的 GitFlow 还要同步回 develop,漏了就复现。
