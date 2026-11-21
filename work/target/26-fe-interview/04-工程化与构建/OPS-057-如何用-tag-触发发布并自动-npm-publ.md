---
title: [OPS-057] 如何用 tag 触发发布并自动 npm publish？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-057：如何用 tag 触发发布并自动 npm publish？
**答**：
- tag 是"发布的事实记录"：打 tag v1.2.3 触发流水线构建、测试、发布，流程与版本号一一对应，天然可追溯可回滚。
- npm 发布用 NPM_TOKEN + `--provenance`（来源证明），只允许 tag 触发防误发；版本号从 tag 提取并校验 package.json 一致。
- 防呆：同 tag 重复推送要拒绝（npm 侧同版本不可覆盖，报错即幂等）；发布后跑冒烟（装包+构建样例工程）。
- 私有包场景用内部 registry（verdaccio/nexus），token 与外部 npm 分开管理。

```yaml
# .github/workflows/publish.yml
name: publish
on:
  push:
    tags: ["v*"]            # git tag v1.2.3 触发

jobs:
  publish:
    runs-on: ubuntu-latest
    environment: npm-publish
    steps:
      - uses: actions/checkout@v4

      - uses: pnpm/action-setup@v4
        with: { version: 9 }
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm, registry-url: "https://registry.npmjs.org" }

      - name: Verify tag matches package.json   # 版本一致性防呆
        run: |
          TAG=${GITHUB_REF#refs/tags/v}
          PKG=$(node -p "require('./package.json').version")
          [ "$TAG" = "$PKG" ] || { echo "tag $TAG != package.json $PKG"; exit 1; }

      - run: pnpm install --frozen-lockfile
      - run: pnpm build && pnpm test

      - name: Publish
        run: npm publish --access public --provenance
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}

      - name: Smoke install          # 发布后真实安装验证
        run: |
          cd /tmp && npm init -y
          npm install $(node -p "require('$GITHUB_WORKSPACE/package.json').name")@latest
          node -e "console.log('installed ok')"
```
