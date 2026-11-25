---
title: [RBL-133] .swcrc 配置体系：jsc/env/module 怎么配
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-133：.swcrc 配置体系：jsc/env/module 怎么配

**答**：
- `jsc` 管"怎么编译"：`parser`（源语法 typescript/tsx/ecmascript）、`transform`（react/legacyDecorator 等）、`target`（es5~es2022 输出水位）、`loose`（宽松模式产物更小但语义略偏）。
- `env` 管"为谁编译"：接 browserslist targets，按需降级语法并注入 core-js polyfill（mode: usage/entry），配置后覆盖 `jsc.target`。
- `module` 管"输出什么模块"：es6/commonjs/amd/umd，commonjs 下可配 `interop` 处理 default 导入兼容。
- 注意 jsc.baseUrl 与 paths：SWC 原生支持 tsconfig paths 别名重写，但不会做模块解析（resolve 是打包器的事）。
- 追问钩子：`test`/`exclude` 字段允许一个项目放多份 .swcrc 分文件类型生效（配合 swc CLI 或 loader 层分发）。

```json
{
  "test": ".*\\.ts?$",
  "jsc": {
    "parser": { "syntax": "typescript", "tsx": true, "decorators": true },
    "transform": {
      "legacyDecorator": true,
      "decoratorMetadata": true,
      "react": { "runtime": "automatic", "importSource": "@emotion/react" }
    },
    "target": "es2020",
    "loose": false,
    "externalHelpers": true,
    "paths": { "@/*": ["./src/*"] }
  },
  "module": { "type": "es6" },
  "minify": false
}
```
- externalHelpers: true 时把 helper（_classCallCheck 等）抽成 import 而不是每个文件内联，产物体积明显下降，但要求构建工具能解析 @swc/helpers 依赖。
