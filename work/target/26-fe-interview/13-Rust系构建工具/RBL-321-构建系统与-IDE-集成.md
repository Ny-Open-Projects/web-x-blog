---
title: [RBL-321] 构建系统与 IDE 的集成（类型跳转/构建错误内联）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-321：构建系统与 IDE 的集成

**答**:
- 类型集成：monorepo 内包走 TS paths（源码直跳）还是 dts（产物跳转）——paths 开发体验好但构建语义漂移风险；混合方案（dev 用 paths、CI 用 dts）+ 校验两边一致
- 构建错误进 IDE：构建错误输出 LSP 兼容格式（文件:行:列+规则码）→ VS Code Problems 面板显示——构建诊断与编辑器诊断统一
- 虚拟模块的跳转支持：构建期生成的虚拟模块（*.virtual.ts）要生成 .d.ts stub 供 TS 识别——不处理则用户处处红线
- 快速迭代闭环：IDE 保存 → dev server 精准 HMR；IDE 内一键「重建该模块」（插件调 dev server API）——调试构建问题的 DX 关键

```json
// tsconfig paths（dev 直跳）
{ "paths": { "@team/core": ["./packages/core/src/index.ts"] } }
// 虚拟模块 stub
declare module 'virtual:routes' { export const routes: Route[] }
```
