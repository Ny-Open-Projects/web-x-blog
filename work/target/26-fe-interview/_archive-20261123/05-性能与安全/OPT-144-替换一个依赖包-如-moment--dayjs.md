---
title: [OPT-144] 替换一个依赖包（如 moment → dayjs）前，如何评估收益避免"白折腾"？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-144：替换一个依赖包（如 moment → dayjs）前，如何评估收益避免"白折腾"？

**答**：
- 三步评估法：①静态收益——bundlephobia 查两包体积（moment 71KB vs dayjs 7KB），注意算 gzip 后和本项目实际用到 Locale 的体积；②动态实测——在当前仓库用 size-limit / webpack-bundle-analyzer 跑替换前后 diff，包含所有间接引用；③运行时收益——解析耗时、内存（moment 对象重）用 Performance 面板对比。
- 警惕"假替换"：替换 A 后引入的 B 插件包反而更大（如 dayjs 不带插件基本够用，全插件安装则收益减半）；tree-shaking 失效的 CJS 包要单独评估。
- 决策口径：核心包 > 30KB gzip 且迁移成本 < 2 人日才值得做；< 10KB 的差异通常不值得冒回归风险。
- 迁移技巧：先写 adapter 层收敛调用点，替换只改 adapter 内部实现。

```bash
# 一一对应：依赖替换收益评估三步实测
# 1. 静态查询：bundlephobia 看 gzip 体积与是否可 tree-shake
#    moment: 71.1KB gzip | dayjs: 7.2KB gzip（含 zh-cn locale 约 +3KB）
npx bundlephobia moment
npx bundlephobia dayjs

# 2. 当前项目实测：替换前后各跑一次，产出精确 diff
npm i size-limit @size-limit/preset-app --save-dev
cat >> package.json <<'JSON'
  "size-limit": [
    { "name": "vendor-before", "path": "dist/assets/vendor-*.js", "gzip": true, "limit": "300 KB" }
  ]
JSON
npm run build && npx size-limit --why      # --why 生成 treemap 确认 moment 的实际占比
# 也可直接在产物里搜依赖体积：
du -ch dist/assets/*.js | tail -1

# 3. 迁移：adapter 收敛调用点，替换只动一层
# utils/date.js 内部从 moment 换成 dayjs，业务代码零改动
npm rm moment && npm i dayjs
npm run build && npx size-limit            # 复测：vendor gzip 从 312KB 降到 168KB
```
