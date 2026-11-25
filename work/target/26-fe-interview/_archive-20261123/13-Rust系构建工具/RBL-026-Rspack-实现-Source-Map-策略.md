---
title: [RBL-026] Rspack 的 source map 策略如何选型？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-026：Rspack 的 source map 策略如何选型？
**答**：
- dev 速度优先：cheap-module-source-map（行级映射+loader sourcemap 合并），rebuild 快；eval-* 系最快但映射粒度差，Rspack 下收益不如 webpack 明显（编译本来就快）。
- 生产安全优先：hidden-source-map——产物不带 sourceMappingURL 注释，map 上传到监控平台（Sentry/内部符号服务）用于错误堆栈还原，不泄露源码。
- 灰度环境折中：nosources-source-map 或 inline 极小的 map 便于现场排查。
- 链路完整性：swc/less/postcss 等转换必须开启各自 sourcemap 输出，否则最终 map 中间层断链，还原行号漂移。
- Rspack 特性：map 生成在 Rust 侧完成，大项目全量 source-map 的构建开销比 webpack 低很多，可以放心用更精确模式。
- 追问钩子：hidden-source-map 的 map 文件要配 CI 产物上传，忘传等于没有 map。

```javascript
// rspack.config.js 按环境选型
module.exports = (env) => ({
  devtool: env.mode === 'production' ? 'hidden-source-map' : 'cheap-module-source-map',
});
// CI：生产构建后上传 map
// curl -F file=@dist/app.7f3a1b2c.js.map https://sentry/api/releases/.../files/
```
