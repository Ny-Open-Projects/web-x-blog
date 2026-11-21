---
title: [TS-055] paths 路径别名怎么配置？要注意什么？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-055：paths 路径别名怎么配置？要注意什么？
**答**：
- `baseUrl` + `paths` 定义别名映射，`paths` 支持通配符，必须以 baseUrl 为基准。
- TS 只负责类型解析，运行时解析要靠 bundler（vite/webpack）的 alias 配置同步。
- `moduleResolution` 决定模块解析策略，bundler 项目建议用 "bundler"。
- include/exclude 控制参与编译的文件范围。

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@components/*": ["src/components/*"]
    },
    "include": ["src", "types"],
    "exclude": ["node_modules", "dist"]
  }
}
```

## 第十五章 declare 与声明文件
