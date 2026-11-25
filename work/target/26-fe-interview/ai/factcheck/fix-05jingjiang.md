# 修复记录：精讲 100 题（4 条报告 + 1 条主会话补充）

> 报告 `05jingjiang.md` 报 4 条需修，主会话于 2026-11-24 修复时另发现 1 处连带误述一并修正。共 5 条。

## 已修
| 题号 | 改了哪一行（改后原文 ≤30 字） | 说明 |
|---|---|---|
| ARC-124 | 「monorepo 在根配置用 `test.projects: ['packages/*']` 分项目；workspace 自 3.2 起已废弃」 | Vitest `workspace` 已废弃，官方由 `test.projects` 取代 |
| BLD-030 | 「配置项是 `optimization.concatenateModules`；要看合并结果读 stats」 | webpack 无 `concatenatedModules` 选项（未知键被静默忽略），且其用途是开启作用域提升而非「查看合并了谁」 |
| BLD-082 | 「esbuild 最低只降到 ES2015，`target: 'es5'` 直接报错；要 ES5 换 Babel」 | 原文「降到 es5 以下它就不支持」方向说反：esbuild 根本不支持 ES5 输出 |
| BLD-081 | 「三个入口：transform、build、context（`ctx.watch()/ctx.serve()` 挂在 context 上）」 | esbuild 顶层 API 无 `serve`（0.17 起移入 context 方法） |
| BLD-041（Vite dev server） | 「默认走 HTTP/1.1，靠浏览器高并发连接缓解」 | 原文「靠 HTTP/2 多路复用缓解」与 Vite dev server 默认协议不符（HTTP/2 需显式开启且通常配 HTTPS） |

## 驳回
| 文件 | 报告说的片段 | 为什么其实没错 |
|---|---|---|
| — | 无 | 4 条需修均属实；第 5 条为主会话核对 BLD-041 时发现的连带问题 |
