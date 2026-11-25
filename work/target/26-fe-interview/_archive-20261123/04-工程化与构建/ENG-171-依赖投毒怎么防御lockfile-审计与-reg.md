---
title: [ENG-171] 依赖投毒怎么防御？lockfile 审计与 registry 白名单怎么设计？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-171：依赖投毒怎么防御？lockfile 审计与 registry 白名单怎么设计？
**答**：
- 投毒路径：包新版本被植入恶意代码、typosquatting 仿冒包名；防御核心是"默认不可信新版本"。
- lockfile 第一道闸：CI 必须 --frozen-lockfile，lockfile 变更要能对应 package.json 的显式声明变更。
- 白名单代理：内部 verdaccio 只放行白名单包与已审核版本，外部新版本进镜像带延迟窗口（潜伏期观察）。
- 补充手段：已知恶意包黑名单检测、install 脚本钩子审计，可疑依赖用 --ignore-scripts 安装。

```yaml
# composite action 片段 —— CI 依赖投毒防线
name: anti-supply-chain
runs:
  using: composite
  steps:
    - shell: bash
      name: lockfile 一致性校验
      run: pnpm install --frozen-lockfile --ignore-scripts   # 不同步直接失败
    - shell: bash
      name: 已知恶意包黑名单检测
      run: node scripts/blocklist.mjs pnpm-lock.yaml
    - shell: bash
      name: install 脚本钩子审计
      run: |
        node scripts/audit-install-scripts.mjs > install-scripts.txt
        grep -q postinstall install-scripts.txt \
          && echo "::warning::存在安装期脚本 见审计文件 需评审" \
          || echo "PASS 无安装期脚本"
```
