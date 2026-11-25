---
title: [RBL-374] 组件库构建的多格式输出与消费兼容
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-374：组件库构建的多格式输出与消费兼容

**答**:
- 输出面：ESM（tree-shaking 友好）+ CJS（老工具链兼容）+ dts（类型）+ CSS 处理（cssinjs vs 独立 css 按需）+ sourcemap——exports 字段条件映射
- 按需加载：组件级分 chunk（每个组件独立入口）+ barrel 优化（sideEffects 精确标注：只有特定文件有副作用）——消费端只打包用到的组件
- 类型策略：dts 从源码直接生成（api-extractor 汇总单入口）vs tsc 分散生成——单入口对消费端解析更快
- 验证门禁：publint/arethetypeswrong + 全组件 import 冒烟（每个组件产物可独立解析渲染）+ tree-shaking 生效断言（unused 组件不进产物）

```text
输出：ESM+CJS+dts+CSS | 按需：组件级 chunk + sideEffects 精确标注
类型：api-extractor 单入口 | 门禁：publint + 全组件冒烟 + shaking 断言
```
