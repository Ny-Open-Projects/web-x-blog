---
title: [OPS-051] GitLab CI 的 stages 与 runner 怎么配置？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-051：GitLab CI 的 stages 与 runner 怎么配置？
**答**：
- stages 顺序执行，stage 内 job 并行；rules 控制哪些分支跑哪些阶段（MR 跑 lint/test，main 加 build/deploy）。
- 缓存用 cache: key 基于 lockfile hash 缓存 node_modules/pnpm store，policy 控制拉/推。
- runner 分共享与项目专用 tag：部署 job 用打了内网标签的专用 runner（能连生产网）。
- environment 声明部署目标，配合 GitLab 的 protected environments 做审批与权限隔离。

```yaml
# .gitlab-ci.yml
stages: [lint, test, build, deploy]

default:
  image: node:22-alpine
  cache:
    key:
      files: [pnpm-lock.yaml]        # lockfile 变化才失效缓存
    paths: [.pnpm-store]
    policy: pull-push

variables:
  PNPM_CACHE_FOLDER: .pnpm-store

lint:
  stage: lint
  script: [corepack enable, pnpm install --frozen-lockfile, pnpm lint, pnpm typecheck]
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
    - if: $CI_COMMIT_BRANCH == "main"

test:
  stage: test
  script: [corepack enable, pnpm install --frozen-lockfile, pnpm test --coverage]
  coverage: '/Lines\s*:\s*(\d+\.\d+)%/'
  artifacts:
    reports: { coverage_report: { coverage_format: cobertura, path: coverage/cobertura-coverage.xml } }
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
    - if: $CI_COMMIT_BRANCH == "main"

build:
  stage: build
  script: [corepack enable, pnpm install --frozen-lockfile, pnpm build]
  artifacts: { paths: [dist/], expire_in: 7 days }
  rules: [{ if: $CI_COMMIT_BRANCH == "main" }]

deploy-prod:
  stage: deploy
  tags: [prod-runner]              # 专用 runner：位于生产网络可达区
  environment: { name: production, url: https://www.example.com }
  script:
    - rsync -azc dist/ deploy@web01:/data/web/mall/releases/$CI_COMMIT_SHORT_SHA/
    - ssh deploy@web01 ln -sfn /data/web/mall/releases/$CI_COMMIT_SHORT_SHA /data/web/mall/current
    - ./scripts/smoke.sh
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
      when: manual                 # 生产部署手动触发，作为审批点
```
