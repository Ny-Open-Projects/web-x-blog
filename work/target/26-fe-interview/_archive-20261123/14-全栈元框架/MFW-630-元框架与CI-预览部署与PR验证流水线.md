---
title: [MFW-630] 元框架 CI：预览部署与 PR 验证流水线
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-630：PR 验证流水线

**答**:
- PR 流水线的五段：1) **类型/lint**（秒级——推送即反馈 RBL-872）；2) **构建 + 预算**（路由画像 diff RBL-561——体积/静态性漂移门禁）；3) **预览部署**（每 PR 一个 preview URL——Vercel preview/自建 K8s namespace——owner 验收 RBL-802 的载体）；4) **E2E 冒烟**（核心路径——preview URL 上跑 RBL-628）；5) **水合/SEO 断言**（首包截断 RBL-528 + 水合 clean RBL-540）。
- 预览部署的隔离：每 PR 独立环境（数据库的隔离——测试数据/分支数据：preview 的 DB 策略（共享测试库 + 租户隔离/分支库——数据爆炸 vs 隔离度）；「preview 的生命周期」：PR 关闭即销毁（资源泄漏防线）。
- 流水线时长预算：PR 验证 < 10 分钟（开发节奏：慢验证 = 开发者跳过/waiT）；「验证深度 × 时长」的权衡（RBL-816 关键路径优化：lint 并行 build、E2E 并行路由抽样）。
- 追问钩子：为什么「preview URL」是 RSC 架构验收的不可替代环节？——RSC 的关键行为（流式/缓存/个性化）只有「真实渲染」才能验证（单测 mock 不到框架运行时 RBL-549）；preview = owner 在真实环境验收（预发级保真 + PR 级速度）——「验证环境的保真度」决定验收质量：preview 是「PR 粒度的 staging」（RBL-864 演练的 PR 版）。

```yaml
# GitHub Actions：PR 流水线
name: pr
on: pull_request
jobs:
  typecheck: { runs-on: ubuntu-latest, steps: [run: pnpm tsc --noEmit] }
  build:
    runs-on: ubuntu-latest
    steps:
      - run: pnpm build
      - run: node scripts/route-profile-diff.js   # 路由画像 diff（RBL-561）
      - run: node scripts/hydration-check.js      # 水合 clean（RBL-540）
  preview:
    runs-on: ubuntu-latest
    steps:
      - run: pnpm build && pnpm start &           # 启动 preview
      - run: pnpm e2e --grep @smoke               # 冒烟 E2E
      - uses: actions/upload-artifact@v4
        with: { name: preview-url, path: preview-url.txt }
      - run: node scripts/first-packet-test.js    # SEO 首包（RBL-528）
  cleanup:                                        # PR 关闭销毁
    if: github.event.action == 'closed'
    runs-on: ubuntu-latest
    steps: [run: kubectl delete ns pr-${{ github.event.number }}]
```
