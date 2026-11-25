---
title: [RBL-232] affected 检测的原理与常见误判
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-232：affected 检测的原理与常见误判

**答**:
- 原理：变更文件集（git diff base）→ 映射到所属包 → 沿「被依赖方向」传播（依赖变更包的包都受影响）→ 只构建受影响闭包
- 误判源一：根目录共享文件（配置/公共 utils）变更影响所有包——应显式声明 globalDependencies；误判源二：隐式依赖（包 A 直接 import 包 B 的内部路径但未声明依赖）——用 dependency-cruiser 校验声明完整性
- base 选择陷阱：CI 上 diff base 要用「与上次成功构建的合并点」，用 origin/main 会把别人已构建的变更算进来（缓存能救但 affected 名单失真）
- 与缓存的关系：affected 缩小任务集，缓存跳过结果未变的任务——两者叠加才是最大加速

```json
// turbo.json globalDependencies
{ "globalDependencies": ["tsconfig.base.json", "pnpm-lock.yaml", ".env.example"] }
// 误判防护：lint 规则禁止跨包深路径 import
```
