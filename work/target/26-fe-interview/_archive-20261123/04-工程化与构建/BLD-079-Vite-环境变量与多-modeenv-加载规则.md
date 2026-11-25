---
title: [BLD-079] Vite 环境变量与多 mode：.env 加载规则与 import.meta.env 的细节。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-079：Vite 环境变量与多 mode：.env 加载规则与 import.meta.env 的细节。
**答**：
- 文件加载顺序（后覆盖前）：.env → .env.local → .env.[mode] → .env.[mode].local；mode 由命令 --mode 指定，dev 默认 development、build 默认 production。
- 暴露规则：只有 envPrefix（默认 VITE_）前缀的变量进入客户端 import.meta.env；其余仅 process.env（服务端/插件侧）可用——防密钥泄漏的机制。
- import.meta.env 是构建期静态替换，动态键 `import.meta.env[key]` 在部分场景不生效（需 import.meta.env 拆包或全量 define）。
- 类型支持：src/vite-env.d.ts 里 ImportMetaEnv 接口声明自定义变量；.local 文件默认 gitignore，存个人配置。

```bash
# bash 代码块：.env 文件族
# .env                       所有 mode 都加载
VITE_APP_TITLE=业务中台
DB_PASSWORD=root123          # 无 VITE_ 前缀 仅服务端可用 不会进产物

# .env.development           仅 dev
VITE_API_BASE=/api

# .env.production            仅 build
VITE_API_BASE=https://api.example.com
```

```javascript
// package.json scripts + 使用示例
{
  "scripts": {
    "dev": "vite",
    "dev:test": "vite --mode test",
    "build": "vite build",
    "build:test": "vite build --mode test"
  }
}

// src/config.ts
const mode = import.meta.env.MODE;          // development | test | production
const base = import.meta.env.VITE_API_BASE; // 构建期静态替换
const isProd = import.meta.env.PROD;        // 布尔内置变量
export { mode, base, isProd };

// src/vite-env.d.ts 类型声明
interface ImportMetaEnv {
  readonly VITE_API_BASE: string;
  readonly VITE_APP_TITLE: string;
}
interface ImportMeta { readonly env: ImportMetaEnv; }
```
