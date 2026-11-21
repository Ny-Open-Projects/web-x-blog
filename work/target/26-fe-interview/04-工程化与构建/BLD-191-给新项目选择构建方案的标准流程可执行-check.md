---
title: [BLD-191] 给新项目选择构建方案的标准流程：可执行 checklist。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-191：给新项目选择构建方案的标准流程：可执行 checklist。
**答**：
- **五步流程**：① 明确应用形态（SPA/MPA/SSR/库/小程序）② 列硬性约束（团队技术栈、CI 环境、浏览器矩阵、MF 需求）③ 候选收敛到 2 个（框架绑定优先：Next→Turbopack、Nuxt→Vite/Rolldown）④ 20 分钟级 PoC 对比（冷启动/增量/HMR/产物体积）⑤ 决策记录 ADR 存档。
- checklist 关键项：是否需要自定义 webpack 插件遗产、依赖生态（组件库按需方案成熟度）、SSR 支持优先级、monorepo 策略（是否 turbo/nx）、团队现有技能池。
- 默认答案表（2026 视角）：新 SPA → Vite（Rolldown 内核）；React 重 SSR → Next.js 全家桶；存量 webpack 大仓 → Rspack 渐进迁移；npm 库 → tsup/unbuild；微前端基座 → Rspack/webpack（MF 成熟度）。
- 反模式：按 GitHub star 选型、无 PoC 直接拍板、忽略"团队不会写 rollup 插件"这类隐性成本。

```text
# 新项目构建选型 checklist（PRD 评审通过后逐项勾选）
[ ] 1. 应用形态：SPA / MPA / SSR / 库 / 微前端子应用 / 小程序
[ ] 2. 框架约束：React or Vue？是否有官方全家桶（Next/Nuxt/Rsbuild）？
[ ] 3. 硬性需求：SSR？Module Federation？多主题？离线 PWA？
[ ] 4. 浏览器矩阵：browserslist 下限（决定目标与 polyfill 策略）
[ ] 5. 团队技能：会用 rollup/vite 插件吗？有 webpack 遗产吗？
[ ] 6. CI 资源：Runner 规格、可否自建远程缓存
[ ] 7. PoC（半天）：同一 demo 项目测 冷启动/HMR/冷构建/gzip 体积 四指标
[ ] 8. 风险预演：若所选工具停滞，回退路径是什么？
[ ] 9. ADR 记录：结论 + 数据 + 放弃的候选及原因（存 docs/adr/）
```

```javascript
// 决策树伪码（工具化选型的雏形）
function chooseBuildTool({ form, framework, needs, legacy }) {
  if (form === 'lib') return needs.dts ? 'tsup' : 'unbuild';          // 库：零心智
  if (framework === 'next') return 'turbopack';                        // 框架绑定
  if (form === 'mp') return 'taro-build';                              // 小程序 DSL
  if (needs.mf && legacy.webpackPlugins > 10) return 'rspack';         // MF + 遗产
  if (form === 'spa' && !needs.ssr) return 'vite';                     // 默认答案
  if (needs.ssr && framework === 'vue') return 'nuxt';
  return legacy.webpack ? 'rspack-gradual' : 'vite';
}
// 输出不是终点：必须跑第 7 步 PoC 校验默认答案，ADR 归档（第 9 步）
```
