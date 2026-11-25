---
title: [BLD-276] Tree-shaking 效果怎么度量？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-276：摇树效果怎么度量？
**答**：
- 度量定义：实际打包体积 / 包完整体积 = 摇树保留率——按包维度统计（哪些包摇得好哪些没摇）。
- 失效定位：保留率高的包逐个归因——CJS 格式/副作用声明缺失/动态导出/桶文件副作用传递（SCN-BLD-203 失效场景逐一对号）。
- 度量数据源：构建 stats（模块级：包内哪些模块被打包）vs 包内全部模块（npm 包内文件清单）——差集即「被摇掉的」。
- 度量的工程化：进 CI 报告（PR 内「某包保留率从 30% 升到 100%——有人改了 import 方式」）——摇树退化的哨兵。
- 追问钩子：为什么「按包维度统计保留率」比「总体积变化」更有诊断力——总体积变化看不出「哪个包失效」；保留率直接点名（lodash-es 保留率 100% 而 antd 保留率 80%——antd 有副作用文件没声明）——按包归因把「摇树优化」从猜测变成定点修复。

```javascript
// 保留率度量
const pkgModules = listPackageModules('antd');         // 包内全部模块
const bundled = stats.modules.filter(m => m.includes('antd'));
const retainRate = bundled.length / pkgModules.length; // 保留率
// 失效归因
bundled.filter(m => !isImportedFromEntrypoint(m));     // 被打包但未被引用 = 摇树失效
```
