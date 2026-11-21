---
title: [RBL-137] SWC 的语法转换能力：TS/JSX/装饰器/实验性提案
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-137：SWC 的语法转换能力：TS/JSX/装饰器/实验性提案

**答**：
- TS：剥离类型标注 + 处理 enum/namespaces/const enum 等需要"计算"的语法（isModule 场景下 const enum 有限制）。
- JSX：支持 classic（React.createElement）与 automatic（jsx-runtime）两种 runtime，可换 importSource 对接 Emotion/Preact。
- 装饰器：支持 legacyDecorator（TS 旧版语义）与 2022-03 标准提案两套，`decoratorMetadata` 生成设计类型元数据；选错套是迁移高频坑。
- 提案语法：optional chaining/nullish/class properties/private methods 等已内置；proposal 级特性（decorators 之外的 stage-x）覆盖不全，迁移前要逐个核对。
- 追问钩子：SWC 转换 TS 不做类型检查——类型错误照样产出，CI 里必须单独跑 tsc --noEmit 或 tsserver 校验。

```javascript
// 装饰器两套语义的配置差异
const optionsLegacy = {
  jsc: {
    parser: { syntax: 'typescript', decorators: true },
    transform: { legacyDecorator: true, decoratorMetadata: true },
  },
};
const optionsStage3 = {
  jsc: {
    parser: { syntax: 'typescript', decorators: true },
    transform: { decoratorVersion: '2022-03' }, // 标准装饰器（支持 native class field）
  },
};
// 踩坑：legacy 模式下装饰器在 class field 初始化顺序与 2022-03 不同；
// 混用 NestJS（legacy 元数据）与新提案写法会运行时找不到 metadata，需统一语义。
```
