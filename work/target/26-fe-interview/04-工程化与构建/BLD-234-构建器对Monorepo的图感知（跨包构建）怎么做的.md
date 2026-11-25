---
title: [BLD-234] 构建器对 Monorepo 的图感知（跨包构建）怎么做的？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-234：跨包构建怎么做的？
**答**：
- 两种模式：源码引用（app 直接 import 包源码——统一构建，无需包产物）vs 产物引用（包先构建出 dist，app 引 dist）——源码引用 dev 快（无需先构建包），产物引用贴近发布语义。
- 跨包增量：包变更 → 消费方 app 重建（affected 闭包，SCN-ENG-286）——构建器/turbo 的图感知决定增量正确性。
- 混合策略：dev 源码引用（HMR 跨包直达）+ prod 产物引用（包按发布语义构建，产物与 npm 发布一致）——dev/prod 语义差异要显式处理。
- 产物引用的 watch：包构建的 watch 输出被 app watch 消费——双 watch 联动（链式失效）。
- 追问钩子：为什么 dev 用「源码引用」prod 用「产物引用」要显式设计而不是全用其一——全源码引用：prod 构建的包行为与 npm 发布的 dist 行为可能不同（构建条件差异）——「测的包 ≠ 发的包」；全产物引用：dev 时改包代码要先构建包（HMR 链条长，反馈慢）——混合模式让 dev 反馈速度与 prod 语义保真兼得。

```javascript
// dev: alias 直指源码
resolve: { alias: { '@org/ui': path.resolve('../ui/src') } }
// prod: 产物引用
resolve: { alias: { '@org/ui': '../ui/dist' } }
// turbo 跨包增量
turbo run build --filter=app...   // ui 变更 → app 自动重建
```
