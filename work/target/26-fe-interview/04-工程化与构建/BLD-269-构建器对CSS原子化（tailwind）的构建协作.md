---
title: [BLD-269] 构建器与 CSS 原子化（Tailwind）的协作怎么做？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-269：Tailwind 构建协作怎么做？
**答**：
- JIT 管线：内容扫描（content 配置的文件集）→ 提取类名 → 按需生成 CSS → 与构建器集成（vite 插件/watch 协同——内容变更触发重扫）。
- 体积特征：产物 CSS 与「用到的类」线性相关（不是全量）——体积优化的关键是 content 配置精确（漏配文件 = 类缺失，多配文件 = CSS 膨胀）。
- 缓存敏感：内容扫描的产物全量重建——类名 hash 变化频繁（SCN-BLD-206 缓存敏感）——大项目考虑按路由拆分 content。
- 与组件库协同：组件库用 Tailwind 时类名静态可分析（不能字符串拼接类名——扫描器看不到）。
- 追问钩子：为什么 Tailwind 「字符串拼接类名」是缺陷高发区——扫描器靠静态字符串匹配生成 CSS；`text-${color}-500` 动态拼接时扫描器看不到完整类名 → CSS 未生成 → 运行时无样式（静默）；解法是 safelist 声明或完整类名写出——原子化的「静态可分析」前提必须被所有代码遵守。

```javascript
// content 精确配置
content: ['./src/**/*.{ts,tsx}', './packages/ui/src/**/*.tsx'],
// 缺陷模式
`text-${color}-500`            // 扫描器看不到 → CSS 未生成
// 修复
const classes = { red: 'text-red-500', blue: 'text-blue-500' };   // 完整类名
```
