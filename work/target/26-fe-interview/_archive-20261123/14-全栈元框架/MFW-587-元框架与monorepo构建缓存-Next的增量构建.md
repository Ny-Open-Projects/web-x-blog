---
title: [MFW-587] Monorepo 中 Next 的增量构建：缓存边界与失效
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-587：Monorepo 中 Next 的增量构建

**答**:
- Next 构建的增量性：next build 本身是全量（路由全编译）——增量靠「外部缓存」：1) **turbo/nx 任务级缓存**（build 输出 .next 目录 hash 缓存——输入不变直接复用 RBL-581）；2) **Next 内部缓存**（.next/cache：webpack/turbopack 的模块级缓存——下次 build 复用编译缓存「构建加速但不跳过构建」）；3) **增量预渲染**（RBL-535：只渲染变化 URL）。
- 缓存键的构成：源码 hash + 依赖闭包 hash（shared 包）+ 环境变量 + Next 版本——「漏一环 = 错缓存」（环境变量进 bundle：NEXT_PUBLIC_* 是构建输入 RBL-760）。
- 缓存的产物验证：缓存恢复后的产物完整性（RBL-638 校验——恢复的 .next 与 manifest 对账：缓存投毒防线）；CI 缓存的隔离（分支间缓存隔离——experimental 分支脏缓存回主干的防护 RBL-581 反模式）。
- 追问钩子：为什么「turbo 缓存 .next 时要排除 .next/cache」？——.next/cache 是「编译过程缓存」（webpack 内存态落盘——跨进程复用加速编译）；它不含最终产物语义（与输出无关）——把它放进 turbo 缓存 = 缓存键污染（编译缓存与源码状态耦合——恢复后编译缓存可能错配）；「过程缓存与产物缓存分离」：turbo 缓存产物（.next 静态/server 文件）、Next 自管过程缓存（.next/cache）——分层缓存的职责分离（RBL-799 的构建版）。

```json
// turbo.json：Next 任务的缓存配置
{
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": [".next/**", "!.next/cache/**", ".next/standalone/**", "dist/**"],
      "inputs": ["$TURBO_DEFAULT$", "!**/*.test.*", ".env*"]
    }
  }
}
// .next/cache 排除：Next 自管过程缓存
// inputs 补充：环境变量文件（NEXT_PUBLIC_* 进 bundle——构建输入）
// 缓存恢复后的完整性校验（CI）
async function verifyRestoredCache(dir, manifest) {
  for (const [route, files] of Object.entries(manifest.routes)) {
    for (const f of files) {
      if (!(await fsExists(`${dir}/${f}`)))
        throw new Error(`缓存恢复不完整: 路由 ${route} 缺 ${f}`);
    }
  }
}
```
