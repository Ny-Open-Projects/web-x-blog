---
title: [ENG-093] 流水线即代码有哪些设计模式？可复用 job 怎么抽象？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-093：流水线即代码有哪些设计模式？可复用 job 怎么抽象？
**答**：
- 模式一：extends/锚点复用公共 before_script 与镜像；模式二：可复用 workflow（GitHub 的 workflow_call / GitLab 的 include）跨仓库共享。
- 模式三：模板仓库 + 参数化输入，团队 CI SRE 维护一份模板，业务仓库只写差异。
- 抽象原则：抽"稳定不变的部分"（环境准备、缓存、制品上传），留"每仓不同"的参数位，避免过度封装导致排障黑盒。
- 版本化引用：include 一个具体 tag 而不是 main，模板升级要走公告与兼容期。

```yaml
# .gitlab-ci.yml：extends 组装可复用 job
.base-job:
  image: node:22-alpine
  before_script:
    - corepack enable
    - pnpm install --frozen-lockfile

lint:
  extends: .base-job
  script: pnpm lint

build:
  extends: .base-job
  script: pnpm build
  artifacts:
    paths: [dist/]
    expire_in: 1 week
```

```yaml
# 跨仓库复用：引入团队模板（锁定版本）
include:
  - project: 'fe/ci-templates'
    ref: v3.2.0
    file: '/templates/frontend-pipeline.yml'
```
