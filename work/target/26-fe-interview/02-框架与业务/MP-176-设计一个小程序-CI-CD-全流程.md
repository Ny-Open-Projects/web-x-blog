---
title: [MP-176] 设计一个小程序 CI/CD 全流程？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-176：设计一个小程序 CI/CD 全流程？
**答**：
- 触发：PR 触发校验流水线（lint/单测/体积/依赖分析），合并 release 触发发布流水线（构建/上传/提审/灰度）。
- 密钥管理：miniprogram-ci 上传私钥存 CI Secret，AppID/环境变量按环境注入，绝不入库。
- 自动化点：自动生成版本描述（changelog）、自动截图冒烟（automator 核心链路）、自动推体验码到群、审核通过后**人工确认灰度**（防自动全量事故）。
- 可观测：每次发布生成发布单（版本/变更/负责人/检查项），失败重试与回滚按钮（回滚 = 上传上一个 tag 产物）。

```yaml
# .github/workflows/mp-release.yml
name: mp-release
on:
  push: { branches: [release] }
jobs:
  quality:
    steps: [checkout, setup-node, npm-ci, lint, unit-test, analyze-dist]
  upload:
    needs: quality
    steps:
      - run: npm run build:prod
      - run: npx miniprogram-ci upload --pp dist --pkp $MP_KEY --appid $MP_APPID --uv ${GITHUB_SHA::7} --desc "$(git log -1 --pretty=%s)"
      - run: node scripts/automator-smoke.js        # 核心链路冒烟
      - run: node scripts/notify-group.js           # 推体验码
  audit-release:
    needs: upload
    environment: production                          # 需人工 approve 才灰度
    steps:
      - run: npx miniprogram-ci submit-audit || node scripts/gray.js --ratio 5
```
