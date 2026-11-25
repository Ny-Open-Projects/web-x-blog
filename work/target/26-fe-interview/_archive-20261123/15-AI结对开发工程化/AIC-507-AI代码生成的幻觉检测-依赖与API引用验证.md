---
title: [AIC-507] AI 代码生成的幻觉检测
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-507：AI 代码生成的幻觉检测

**答**:
- AI 代码幻觉的三个维度：1) **依赖幻觉**（import 不存在的包——`lodash-es-deep`（看似合理但不存在——RBL-943 的防防线）；2) **API 幻觉**（调不存在的方法——`arr.removeAt(2)`（数组没有 removeAt）；`React.useRef.current()`（useRef 返回对象非函数）；3) **类型幻觉**（类型不匹配——`str.length` 当 number 用但实际是 string | null；「幻觉的检测」：编译器（TypeScript 严格模式 = API 幻觉的检测器）+ 运行时（`import` 失败 = 依赖幻觉的检测器）。
- 幻觉的分层检测：1) **编译期**（TS 严格模式——API 幻觉/类型幻觉检出 RBL-946）；2) **构建期**（bundle 依赖审计——依赖幻觉检出 RBL-943）；3) **运行时**（测试——逻辑幻觉（代码逻辑错误——编译通过但语义错）只有测试才能检出；4) **人工**（语义幻觉——"AI 认为业务规则是 X 但实际是 Y"——只有领域知识才能发现。
- 追问钩子：为什么「AI 的 API 幻觉」比「AI 的逻辑幻觉」更容易自动检测？——API 幻觉 = 编译器可检出（TypeScript 严格模式：`arr.removeAt` 不存在 → 编译错）；逻辑幻觉 = 语义问题（`if (age > 18)` 但业务规则是 >16——编译器不知道业务规则）；「编译器 vs 领域知识」的检测能力边界：编译器管语法/类型/API 存在性、测试管逻辑正确性、人工管业务正确性——三层检测各管一段（RBL-504 信任分级的依据）。

```typescript
// 幻觉检测的三层防线
// 1) 编译期：TypeScript strict
// tsc --noEmit → API/类型幻觉检出
// 2) 构建期：依赖审计
function auditImports(code: string, lockfile: Record<string, string>) {
  const imports = [...code.matchAll(/from\s+['"]([^.'"][^'"]*)['"]/g)]
    .map(m => m[1].split('/')[0]);
  return imports.filter(pkg => !(pkg in lockfile))
    .map(pkg => ({ pkg, type: 'hallucinated-dependency' }));
}
// 3) 运行时：测试
// AI 写实现 → AI 写测试 → 人审测试 → 测试跑通 → 可信
// 测试检出逻辑幻觉（编译通过但结果错）
```
