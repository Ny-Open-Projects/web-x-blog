---
title: [ENG-008] npm scripts 的生命周期钩子是怎么执行的？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-008：npm scripts 的生命周期钩子是怎么执行的？
**答**：
- 任意自定义脚本 name 会先自动执行 prename 再执行 postname，例如 build 前后钩子。
- 内置生命周期：prepare 在本地开发与打包前执行（husky 常挂这里）、prepublishOnly 在发布前执行。
- 钩子是隐式魔法，团队内要控制使用密度，过多 pre/post 会让调用链难以追踪。
- 脚本里可以通过 npm_package_* 环境变量读取包信息。

```javascript
// package.json
{
  "scripts": {
    // 执行 pnpm build 时自动按序执行 prebuild -> build -> postbuild
    "prebuild": "rimraf dist",
    "build": "vite build",
    "postbuild": "node scripts/print-size.mjs",
    // prepare：安装依赖后自动执行，husky 靠它注册 git hooks
    "prepare": "husky",
    // 发布前校验，失败则中止 npm publish
    "prepublishOnly": "pnpm test && pnpm build"
  }
}
```

---

## 第二章 Vite 原理与实践（ENG-009 ~ ENG-014）

```mermaid
flowchart LR
  subgraph dev["开发模式"]
    A["浏览器按 ESM 请求模块"] --> B["Vite dev server 拦截"]
    B --> C{"命中预构建缓存"}
    C -->|否| D["esbuild 预构建依赖"]
    C -->|是| E["按需编译源码并返回 ESM"]
    D --> E
  end
  subgraph prod["生产构建"]
    F["Rollup 打包"] --> G["Tree shaking 与代码分割"]
    G --> H["输出带 hash 的静态产物"]
  end
```
