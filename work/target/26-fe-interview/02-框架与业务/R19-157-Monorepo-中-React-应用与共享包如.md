---
title: [R19-157] Monorepo 中 React 应用与共享包如何组织？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-157：Monorepo 中 React 应用与共享包如何组织？
**答**：
- 结构：pnpm workspace + `apps/*`（站点）+ `packages/*`（ui、hooks、api-client、config），共享包用 TS 源码或构建产物两种模式。
- 引用方式：内部包走 workspace 协议 `"@acme/ui": "workspace:*"`；共享包变更用 changesets 管理版本（对外发包）或 fixed 模式（仅内部使用，跟随 app 发版）。
- 构建策略：配置包（eslint/tsconfig）直接被继承；UI 包推荐 `tsc + vite lib mode` 产出 ESM + d.ts，Turbo 缓存并行构建。
- 关键坑：React 单实例（peerDependencies 声明 + app 提供）、HMR 跨包失效（UI 包出源码模式或配 optimizeDeps 排除）。

```yaml
# pnpm-workspace.yaml
packages:
  - 'apps/*'
  - 'packages/*'
```

```json
// packages/ui/package.json —— 共享组件包的关键声明
{
  "name": "@acme/ui",
  "version": "0.1.0",
  "type": "module",
  "exports": {
    ".": { "types": "./dist/index.d.ts", "import": "./dist/index.js" },
    "./styles.css": "./dist/styles.css"
  },
  "files": ["dist"],
  "scripts": { "build": "vite build && tsc --emitDeclarationOnly" },
  "peerDependencies": {
    "react": "^19.0.0",
    "react-dom": "^19.0.0"
  },
  "devDependencies": {
    "react": "^19.0.0"
  }
}
```

```json
// apps/web/package.json —— 应用侧消费
{
  "name": "@acme/web",
  "dependencies": {
    "@acme/ui": "workspace:*",      // workspace 协议：本地链接，改包即时生效
    "@acme/hooks": "workspace:*",
    "react": "^19.0.0"              // React 由 app 唯一提供，杜绝双实例
  }
}
```

```javascript
// turbo.json —— 任务编排与缓存
{
  "tasks": {
    "build": {
      "dependsOn": ["^build"],   // 先构建依赖的包
      "outputs": ["dist/**"]
    },
    "lint": {},
    "test": { "dependsOn": ["^build"] }
  }
}
// 常用命令：
// pnpm -F @acme/ui build      单包构建
// pnpm -r --filter ./apps/web dev  启动应用（UI 包走源码或 watch 构建保证 HMR）
// npx changeset               管理共享包版本与 CHANGELOG
```

## 第二十三章 状态库实现（R19-158 ~ R19-162）
