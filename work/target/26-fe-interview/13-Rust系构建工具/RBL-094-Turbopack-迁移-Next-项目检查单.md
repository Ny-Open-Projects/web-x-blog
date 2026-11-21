---
title: [RBL-094] Next.js 项目迁移 Turbopack 的检查单？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-094：Next.js 项目迁移 Turbopack 的检查单？
**答**：
- 第一步：盘点 webpack() 配置与第三方 loader/plugin——Next 官方有"不支持特性清单"，逐项映射到 turbo.rules 或找替代。
- 第二步：CSS/样式方案确认（Tailwind、CSS Modules、sass 内置支持）；PostCSS 配置文件照常生效。
- 第三步：自定义 webpack 插件的功能归零评估——Turbopack 无插件体系，依赖注入/产物加工类需求走 Next 的其他机制（如 next.config 钩子）。
- 第四步：环境变量与 resolve 别名迁移到 turbo 字段；验证 monorepo 的 workspace 依赖解析。
- 第五步：灰度跑 dev（本地 + 内部同学），收集 HMR 异常与编译错误回归，再推全团队。
- 已知不可迁移项类型：依赖 webpack runtime 定制的产物加工、深度 hooked 的 bundler 插件、部分老 loader。
- 追问钩子：迁移的收益主要是 dev 与 CI 缓存；如果项目 dev 已经够快（小项目），迁移优先级低。

```markdown
# Turbopack 迁移检查单
- [ ] webpack() 配置清单化，逐项映射 turbo.rules
- [ ] 无替代的 webpack 插件 → 功能降级评估
- [ ] resolve alias/extensions 迁移
- [ ] CSS 方案验证（内置支持面确认）
- [ ] monorepo workspace 解析验证
- [ ] HMR / Fast Refresh 回归（组件态保留）
- [ ] 本地灰度一周 → 团队推广
```
