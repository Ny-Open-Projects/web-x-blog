---
title: [RBL-646] 构建器与 tsc 的职责边界：类型检查为什么不该进构建热路径
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-646：构建器与 tsc 的职责边界：类型检查为什么不该进构建热路径

**答**:
- SWC/oxc/rolldown 做「TS 剥离」（strip types）而非「类型检查」：类型检查需要完整类型图（跨模块推导、泛型解析），计算量 O(全仓库类型闭包)——放进构建热路径会让 dev 秒开变成秒级等待；正确的架构是「构建管转换、检查器独立跑」（IDE 增量 tsc / CI 专项任务）。
- 职责边界的具体分配：构建器负责——语法转换、装饰器/enum 等语言特性降级、isolatedModules 兼容（单文件可转）；tsc 负责——类型错误、跨模块一致性、d.ts 生成（composite 项目）。isolatedModules 约束的意义就是「保证单文件转换语义完备」，违反它（如 re-export 类型不加 type 标记）会在 strip 型构建器下静默出错——构建器要主动诊断这个模式。
- 类型信息的有限利用：构建器不解类型但可读 tsconfig 的 paths/target/装饰器配置来决定转换行为——「配置消费」与「类型检查」分离；d.ts 的产出（SDK 发布场景）必须由 tsc/api-extractor（需要类型图），构建器不做。
- 诊断体验：strip 模式下「类型错了但构建成功」会让用户误以为没问题——最佳实践是 dev server 显示「构建成功 + 类型检查后台进行中」，类型错误以覆盖层提示而非构建失败——把「构建时间」与「类型反馈时间」解耦。
- 追问钩子：为什么 vite build 默认不跑 tsc？——build 的 SLA 是产物正确（运行时语义），类型不改变运行时行为（除 enum 等特殊语法已处理）；CI 里 build + typecheck 并行任务比串行快一倍——解耦也是并行化的前提。

```javascript
// 构建器对 isolatedModules 违规的诊断
// 违规：export type { T } 未标 type / import 类型未用 import type（verbatimModuleSyntax）
function diagnoseTypeOnly(code) {
  const diagnostics = [];
  // re-export 类型未标 type：strip 后 import { T } 变成运行时导入 -> 找不到
  const re = /export\s+\{\s*(\w+)\s*\}\s*from/;
  let m;
  if ((m = re.exec(code)) && isTypeOnlyExport(m[1]))
    diagnostics.push({
      code: 'RBL4100', severity: 'error',
      message: `导出 '${m[1]}' 是类型但未标 type —— strip 模式下会变成运行时导入`,
      hint: `改为 export type { ${m[1]} }，或开启 verbatimModuleSyntax`,
    });
  return diagnostics;
}
// 协作流水线（CI）
// parallel: [rolldown build, tsc --noEmit]  // 并行而非串行
```
