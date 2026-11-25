---
title: [BLD-215] 动态 import 的打包语义怎么工作？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-215：动态 import 语义怎么工作？
**答**：
- 静态可分析的动态 import：`import('./page')` 字面量 → 独立 chunk + promise；模板字符串（`import('./pages/' + name)`）→ 打包器无法确定 → 整目录打包（context module）或警告。
- 魔法注释：webpackChunkName（命名 chunk）/ prefetch / preload —— prefetch 空闲拉取（低优先级）vs preload 当前导航必需（高优先级）。
- 动态 import 的失败语义：网络失败 → promise reject → 必须有 ErrorBoundary/重试（chunk 加载失败的 UX，SCN-OPS-218）。
- import.meta 语义：import.meta.url（模块 URL）/ webpackignore（跳过打包）——构建工具对 meta 的处理差异。
- 追问钩子：为什么「模板字符串动态 import」是体积黑洞——`import(\`./locales/${lang}\`)` 会让打包器把 locales 下所有文件都打成 chunk（context module，因为运行时 lang 可能是任何值）；解法是显式枚举（对象映射）或 glob 预声明——让打包器「知道」可能的集合。

```javascript
// 黑洞
import(`./locales/${lang}`);   // 打包整个 locales 目录
// 解法：显式映射
const loaders = { en: () => import('./locales/en'), zh: () => import('./locales/zh') };
const load = loaders[lang] ?? (() => import('./locales/en'));
// preload vs prefetch
import(/* webpackPreload: true */ './critical');      // 当前导航必需
import(/* webpackPrefetch: true */ './maybe-next');   // 空闲预取
```
