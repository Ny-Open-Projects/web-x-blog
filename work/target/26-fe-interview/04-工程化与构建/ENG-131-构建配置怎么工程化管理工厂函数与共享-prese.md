---
title: [ENG-131] 构建配置怎么工程化管理？工厂函数与共享 preset 包怎么做？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-131：构建配置怎么工程化管理？工厂函数与共享 preset 包怎么做？
**答**：
- 各业务仓库复制粘贴 vite.config 是配置腐化的根源：升级、规范调整要改 N 份且必然漂移。
- 标准做法：抽出 build-preset 内部包，导出工厂函数 createVitePreset，按项目类型 app/lib/node 返回差异化配置。
- preset 内部收敛插件集合、分包策略、压缩与 sourcemap 策略；对外只暴露少量 options，保证规范可统一、项目可定制。
- 版本管理：preset 用固定版本号发布，仓库按季度统一升级，避免每次 install 漂移。

```typescript
// packages/build-preset/src/index.ts —— 工厂函数收口构建配置
import { defineConfig, type UserConfig } from 'vite'

type ProjectType = 'app' | 'lib'

interface PresetOptions {
  projectType?: ProjectType
  port?: number
  externals?: Record<string, string>
}

export function createVitePreset(options: PresetOptions = {}) {
  const { projectType = 'app', port = 5173, externals = {} } = options
  return defineConfig((): UserConfig => ({
    plugins: sharedPlugins(),          // 规范插件：分包分析 sourcemap 策略 lint 插件
    build: projectType === 'lib'
      ? { lib: { entry: 'src/index.ts', formats: ['es', 'cjs'] }, sourcemap: true }
      : { target: 'es2018', rollupOptions: { external: Object.keys(externals) } },
    server: { port },
  }))
}

// 业务仓库里只剩三行
// import { createVitePreset } from '@corp/build-preset'
// export default createVitePreset({ projectType: 'app' })
```
