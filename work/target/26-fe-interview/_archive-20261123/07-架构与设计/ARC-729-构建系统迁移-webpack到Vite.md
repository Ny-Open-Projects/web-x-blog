---
title: [ARC-729] 构建系统迁移：webpack 到 Vite
date: 2026-11-21
categories: [前端架构]
tags: [前端面试, 面试题, 迁移]
type: 面试题
---

## ARC-729：webpack → Vite 迁移

**答**：
- 迁移收益先行量化：dev 启动（webpack 大仓 60s → Vite 秒级）、HMR——收益要数据化（说服管理层的唯一语言）
- 迁移的兼容清单：loader 生态（webpack 特有 loader 的 Vite 插件等价物）、环境变量（process.env → import.meta.env）、CommonJS 依赖（vite-plugin-commonjs/pre-bundling）、CSS 方案
- 双构建器过渡期：dev 用 Vite（快）build 用 webpack（稳定产物）——分阶段切换降低风险，产物一致性验证后再全切
- 迁移的隐形坑：路径别名大小写（macOS 忽略 Linux 严格）、动态 require、worker 语法差异——CI（Linux）是差异的放大器
- 深水点：迁移的「产物等价验证」——Vite 构建产物与 webpack 产物的功能对比（自动化冒烟 + 体积对比）——构建器迁移的验收是产物等价而非能跑

```text
webpack→Vite:
  收益量化: dev 启动/HMR (数据化)
  兼容: loader 生态/env/CSS/动态require
  过渡: dev=Vite, build=webpack → 产物等价后全切
  坑: 别名大小写(Linux 严格) / worker 语法
  验收: 产物等价验证 (冒烟+体积对比)
```
