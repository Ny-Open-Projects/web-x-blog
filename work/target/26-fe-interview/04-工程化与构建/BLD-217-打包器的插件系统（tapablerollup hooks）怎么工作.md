---
title: [BLD-217] 打包器的插件系统怎么工作？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-217：插件系统怎么工作？
**答**：
- webpack tapable：钩子类型（Sync/AsyncSeries/AsyncParallel + bail/waterfall/loop）——钩子类型决定多插件的执行语义（bail 有返回值停止/waterfall 传递结果）。
- rollup/vite 钩子：构建期（resolveId/load/transform）与生成期（renderChunk/generateBundle）分离——vite 复用 rollup 插件接口 + dev 独有钩子（configureServer）。
- 插件间依赖：enforce（pre/post）与顺序声明——插件顺序 bug（transform 顺序错）是常见构建错误。
- 治理：插件注册表/性能开销声明（SCN-ENG-245）。
- 追问钩子：为什么 tapable 的「waterfall 钩子」最容易出顺序 bug——waterfall 把上一个插件的返回值作为下一个的输入（如 transform 链），插件 A 修改了资源后插件 B 基于修改后的处理——顺序错了产出就错且难以察觉；写插件时必须声明对前序插件产物的假设。

```javascript
// tapable 类型语义
SyncBailHook:        任一插件返回非 undefined → 停止
AsyncSeriesWaterfallHook: 返回值传递给下一插件（顺序敏感）
// rollup 钩子
{ name: 'my', resolveId(spec) {...}, transform(code, id) {...},
  renderChunk(code, chunk) {...} }
```
