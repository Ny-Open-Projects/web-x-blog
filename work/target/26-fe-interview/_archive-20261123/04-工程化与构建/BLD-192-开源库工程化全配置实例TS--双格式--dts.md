---
title: [BLD-192] 开源库工程化全配置实例：TS + 双格式 + dts + test + CI 一条龙。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-192：开源库工程化全配置实例：TS + 双格式 + dts + test + CI 一条龙。
**答**：
- 目录与产物：src（TS 源码）→ dist（esm+cjs+d.ts 双格式，exports 映射，BLD-143）；测试 vitest（esbuild 快）+ 覆盖率卡口；lint（eslint + prettier）与类型检查独立 script。
- 发布链：changesets（BLD-147）+ GitHub Actions provenance + 发布前 `pnpm prepack`（自动构建，保证发出去的是 dist）；`files` 字段白名单 + `engines` 声明。
- 质量门禁：PR 必过 build+typecheck+test+size-report（库也要预算，helper 泄露检测：dist 里 `require("tslib")` 次数异常即报警）。
- 文档与体验：TypeDoc? README + playground（pnpm link 或 vite alias 源码直连）、`npm explain? ` — 面试能讲清"从 clone 到 npm publish"的完整路径即合格。

```json
// 开源库 package.json 全貌（ts + 双格式 + exports + 发布链）
{
  "name": "@org/tiny-store",
  "version": "0.0.0",
  "type": "module",
  "main": "./dist/index.cjs",
  "module": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": { "types": "./dist/index.d.ts", "import": "./dist/index.js", "require": "./dist/index.cjs" }
  },
  "sideEffects": false,
  "files": ["dist"],
  "scripts": {
    "build": "tsup src/index.ts --format esm,cjs --dts --clean --sourcemap",
    "test": "vitest run --coverage",
    "typecheck": "tsc --noEmit",
    "prepack": "pnpm build"                       // npm publish 前自动构建（防发旧码）
  },
  "devDependencies": {
    "tsup": "^8.0.0", "vitest": "^2.0.0", "typescript": "catalog:",
    "@changesets/cli": "^2.27.0"
  },
  "engines": { "node": ">=18" }
}
```

```yaml
# .github/workflows/lib-ci.yml：PR 门禁 + 发布一条龙
name: ci
on: [push, pull_request]
jobs:
  quality:
    runs-on: ubuntu-latest
    permissions: { contents: read }
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm, registry-url: 'https://registry.npmjs.org' }
      - run: pnpm install --frozen-lockfile
      - run: pnpm typecheck && pnpm lint && pnpm test
      - run: pnpm build
      - run: node scripts/check-helpers.mjs    # helper 泄露/体积预算
  release:
    if: github.ref == 'refs/heads/main'
    needs: quality
    runs-on: ubuntu-latest
    permissions: { contents: write, id-token: write }   # provenance 需要 id-token
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm, registry-url: 'https://registry.npmjs.org' }
      - run: pnpm install --frozen-lockfile
      - uses: changesets/action@v1
        with: { publish: pnpm publish --provenance --access public }
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
```
