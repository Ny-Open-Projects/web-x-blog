---
title: [ENG-024] SWC 和 Rspack 是什么？解决什么问题？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-024：SWC 和 Rspack 是什么？解决什么问题？
**答**：
- SWC 是 Rust 实现的 JS/TS 编译器，能力对标 Babel，速度快一个数量级，Next.js 默认使用。
- Rspack 是 Rust 实现的高性能 webpack 兼容构建器，Rsbuild 基于它提供开箱配置。
- 迁移成本低：webpack 项目可基本无缝切到 Rspack，获得数倍构建提速。
- 取舍：生态插件覆盖度略低于 webpack，复杂自定义 plugin 可能需要适配。

```javascript
// .swcrc
{
  "jsc": {
    "parser": { "syntax": "ecmascript", "jsx": true },
    "target": "es2018",
    "transform": {
      "react": { "runtime": "automatic" }
    }
  },
  "minify": true
}
```

---

## 第五章 Babel AST 与 Tree shaking（ENG-025 ~ ENG-030）
