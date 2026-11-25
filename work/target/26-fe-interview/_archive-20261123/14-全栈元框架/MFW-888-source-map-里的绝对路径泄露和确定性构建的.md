---
title: [MFW-888] source map 里的绝对路径泄露和确定性构建的路径规范化怎么处理
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-888：source map 里的绝对路径泄露和确定性构建的路径规范化怎么处理

**答**：
- 结论：source map 常含构建机绝对路径，既泄露内部目录结构又破坏可复现性；用 sourceRoot + 相对路径 + 路径规范化消除机器依赖。
- 落地：编译时用相对路径生成 sources，设置 sourceRoot；生产可选只上传 sourcemap 到错误平台而不随产物发布，兼顾调试与安全。
- 追问钩子：完全不生成 sourcemap 可以吗？——线上错误无法符号化，排障成本极高，通常用「上传但不在 CDN 暴露」。

```javascript
// webpack/vite 配置示意：路径相对化
const config = {
  build: {
    sourcemap: 'hidden',                            // 生成但不引用（不在产物暴露）
    rollupOptions: { output: { sourcemapPathTransform: (p) =>
      p.replace(/\/home\/ci\/workspace\//g, 'src/') // 绝对路径 → 相对
    } }
  }
};
// 校验：产物中不应出现构建机路径
// grep -R "/home/" dist/ → 应为空
```
