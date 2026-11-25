---
title: [RBL-317] 构建期 Feature Flag 裁剪（死代码消除的配置面）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-317：构建期 Feature Flag 裁剪

**答**:
- 原理：DefinePlugin 把 `__FEATURE_X__` 替换为 true/false → minifier 按 if(false) 剪枝 → 死代码与依赖不进产物（bundle 级 flag 裁剪）
- 与运行时 flag 的边界：构建期 flag = 不需要运行时切换的功能（如内部功能对特定租户编译剔除）；运行时 flag = 需要动态灰度——选错时机导致「想切切不动」或「体积没省下」
- 裁剪正确性风险：flag 分支的副作用（顶层注册）剪不干净、动态引用（变量 flag）不裁剪——用静态可分析写法（if 常量而非三元变量）
- 组合爆炸治理：多 flag 组合产物（x^2 种）只构建实际发布的组合；裁剪组合的产物都要过冒烟

```javascript
// DefinePlugin + 静态写法
if (__FEATURE_NEW_CART__) {          // 构建期常量 → 剪枝
  registerCart()                      // 副作用也随分支被剪
}
// ❌ const flag = __FEATURE_X__; if (flag) — 可能逃逸
```
