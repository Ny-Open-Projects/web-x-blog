---
title: [ENG-215] 前端工具链的统一抽象（内部 CLI）怎么设计？什么时候不要做？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-215：内部 CLI 怎么设计？
**答**：
- CLI 定位：封装「正确路径」而非封装一切——`fe create/fe upgrade/fe release` 三五个高频命令解决 80% 场景，逃生舱直接透传底层工具。
- 插件化内核：CLI 是壳，能力以插件注册（创建模板/升级编排/发布流程），团队可扩展不 fork 主程序。
- 升级自愈：CLI 自带 `fe doctor`（环境自检）+ 升级提示 + 向后兼容策略（命令弃用先告警两版）。
- 不做 CLI 的时机：工具尚在快速迭代期/团队 < 10 人/底层工具（pnpm/vite）已经足够顺手——过早封装是把学习成本转嫁给 CLI 维护者。
- 追问钩子：为什么 CLI 要「透传逃生舱」而不是全封装——封装层滞后于底层工具能力（vite 新特性 CLI 不支持就卡住）；`fe run -- pnpm xxx` 透传让团队永远有出路。

```javascript
#!/usr/bin/env node
// 内部 CLI 壳 + 插件内核
import { createCli } from '@fe/cli-core';
import { createPlugin, upgradePlugin, releasePlugin } from '@fe/cli-plugins';
const cli = createCli({ name: 'fe' });
cli.use(createPlugin).use(upgradePlugin).use(releasePlugin);
cli.command('run', '透传底层工具（逃生舱）')
   .allowUnknownOptions()
   .action((args) => spawn(args.raw.join(' '), { stdio: 'inherit' }));
cli.parse(process.argv);
```
