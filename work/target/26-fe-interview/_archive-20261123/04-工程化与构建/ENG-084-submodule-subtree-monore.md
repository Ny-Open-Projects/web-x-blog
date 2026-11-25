---
title: [ENG-084] submodule、subtree、monorepo 怎么选？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-084：submodule、subtree、monorepo 怎么选？
**答**：
- submodule：主仓库只存引用指针，克隆后要 update --init 才有内容；版本边界清晰但心智负担重，CI/新手上手成本高。
- subtree：把外部仓库内容真实合入主仓库，普通 clone 即可用；同步命令复杂但无额外操作成本。
- monorepo：多团队高频协作时统一仓库 + pnpm workspace，工具链成熟（Turborepo/changesets）是当下主流。
- 经验法则：低频依赖选 submodule（或干脆发 npm 包）；需要源码级联调直接 monorepo；subtree 适合"要源码但不想拆"的场景。

```bash
# submodule：引用式管理，克隆后需初始化
git submodule add https://github.com/org/shared-ui.git packages/shared-ui
git clone --recurse-submodules https://github.com/org/app.git   # 克隆时一并拉取
git submodule update --remote                                    # 更新到子仓库最新

# subtree：内容合入主仓库，普通 clone 即可用
git subtree add --prefix=packages/shared-ui https://github.com/org/shared-ui.git main --squash
git subtree pull --prefix=packages/shared-ui https://github.com/org/shared-ui.git main --squash
```
