---
title: [ARC-215] 联邦下的 CI/CD 流水线如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-215：联邦下的 CI/CD 流水线如何设计？
**答**：
- 子应用流水线：build（产 manifest+snapshot）→ 上传 CDN（版本目录，保留 N 版）→ 契约回归（ARC-214）→ 影响面审批 → 灰度发布（改 manifest 指针按比例）→ 全量。
- 主应用流水线大幅变轻：不再因子应用改动而重建；只在自身代码/共享配置变化时构建。CI 时间从"全联邦编译"降为"单体编译"。
- 环境映射：dev/stage/prod 三套 manifest 指针路由，feature 分支可用独立的临时版本（预发环境验证联邦链路）。
- 安全门禁：CDN 产物校验（SRI/签名）、expose 变更的 semver 检查、snapshot 的 requiredVersion 交叉校验全部卡在发布前。

```yaml
# 子应用 .ci.yml（示意）
stages: [build, upload, contract, release]
build:    { cmd: 'mf-build && mf-snapshot' }            # 产出 manifest.json + snapshot
upload:   { cmd: 'oss-cp dist/ oss://mf/shop/${VER}/', keep: 10 }  # 保留 10 个版本支持秒回滚
contract: { cmd: 'mf-contract-run --downstreams host,pay' }        # 平台代跑下游契约
release:
  manual: true                                        # 有影响面时人工审批
  gray:   { steps: ['5%:15m', '30%:30m', '100%'], metric: 'mf-error-rate' }  # 灰度看联邦错误率
```
