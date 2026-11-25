---
title: [ENG-106] pnpm workspace 完整配置怎么做？catalog 协议怎么统一依赖版本？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-106：pnpm workspace 完整配置怎么做？catalog 协议怎么统一依赖版本？
**答**：
- pnpm-workspace.yaml 声明 packages 范围（apps/*、packages/*），catalog 段登记公共依赖的统一版本。
- 各包 package.json 用 "react": "catalog:" 引用，升级只改 catalog 一处，全仓生效，杜绝双 React 实例。
- 补齐配置：minimumReleaseAge、onlyBuiltDependencies 等安全项按团队需要加；lockfile 提交。
- catalog 也支持 catalog:range（允许小范围浮动），默认 catalog: 是精确锁定。

```yaml
# pnpm-workspace.yaml
packages:
  - 'apps/*'
  - 'packages/*'

# catalog：全仓公共依赖版本在此统一登记
catalog:
  react: ^19.0.0
  react-dom: ^19.0.0
  typescript: ~5.6.0
  eslint: ^9.0.0
```

```json
{
  "name": "@myorg/web",
  "dependencies": {
    "react": "catalog:",
    "@myorg/ui": "workspace:^"
  }
}
```
