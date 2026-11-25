---
title: [BLD-190] 构建安全加固清单：从依赖到产物到 CI 的供应链全链路。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-190：构建安全加固清单：从依赖到产物到 CI 的供应链全链路。
**答**：
- **依赖链**：lockfile 提交且 `--frozen-lockfile`（CI 禁止解析新版本）、`pnpm overrides` 锁关键包、npm provenance/attestation 验证发布源、依赖审计卡口（`pnpm audit --prod` + osv-scanner）。
- **安装与执行**：`ignore-scripts`? 生产 CI 可选开启 + allowlist（仅少数包需要 postinstall）；`.npmrc` 指向私有 registry（防 typo-squatting 公网包）；git 依赖禁用（不可复现）。
- **产物链**：产物哈希清单（BLD-188）+ SRI（BLD-170）+ sourcemap 不发布到公网 CDN；sourcemap 上传私有监控需 token。
- **CI 链**：最小权限 token（per-workflow GITHUB_TOKEN 权限收敛）、缓存当不可信输入（BLD-162）、第三方 action pin 到 commit SHA、发布凭据用 OIDC 短时凭证。

```yaml
# .github/workflows/build-secure.yml：安全加固要点全部落在配置里
permissions:
  contents: read            # 最小权限：默认只读
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      # 第三方 action 固定 commit SHA（tag 可被改写）
      - uses: pnpm/action-setup@fe02b34f222f5e89aef5aa5edebf9f6aa4637c9f # v4.0.0
      - uses: actions/setup-node@60edb5dd545a775178f525f7ae2fdc67be6003b4
        with: { node-version-file: '.nvmrc', cache: pnpm }
      - run: pnpm config set ignore-scripts true
      - run: pnpm install --frozen-lockfile --prod=false
      # 供应链审计卡口
      - run: pnpm audit --prod --audit-level=high
      - run: osv-scanner --lockfile=pnpm-lock.yaml || exit 1
      - run: pnpm build
      - run: node scripts/check-dist-hash.js     # 产物清单生成与自校验
```

```ini
# .npmrc：registry 收口与执行策略
registry=https://registry.npmmirror.com       # 或私有 registry（企业内更常见）
# 关键：生产 CI 用内部镜像源，阻断公网直接安装（typo-squatting）
# audit=false 由 CI 显式跑 audit 替代（可控记录）
engine-strict=true
```
