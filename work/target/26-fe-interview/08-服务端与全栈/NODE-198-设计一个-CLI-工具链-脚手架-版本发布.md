---
title: [NODE-198] 设计一个 CLI 工具链（脚手架/版本发布）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-198：设计一个 CLI 工具链（脚手架/版本发布）？
**答**：
- 组成：命令解析（commander）→ 交互确认（inquirer）→ 模板渲染（ejs）→ 依赖安装（execa）；bin 字段映射命令名。
- 模板策略：模板独立仓库（或包内目录），变量注入 db/deploy 选项；生成后可 git diff 出团队规范的"标准形状"。
- 发布治理：changesets 管版本与 changelog；插件化——团队命令以 `@scope/cli-plugin-*` 约定发现，互不侵入核心。
- 工程化：CLI 自身走 ESM（NODE-158）、CI 发布自动 npm publish、`--verbose` 调试日志。

```javascript
#!/usr/bin/env node
import { program } from 'commander';
import inquirer from 'inquirer';
import { execa } from 'execa';
import { renderTemplates } from './render.js';
import { createRequire } from 'node:module';

const pkg = createRequire(import.meta.url)('../package.json');
program.version(pkg.version);

program.command('create <name>')
  .description('生成 BFF 服务脚手架')
  .action(async (name) => {
    const answers = await inquirer.prompt([
      { type: 'list', name: 'db', message: '数据库', choices: ['mysql', 'mongo'] },
      { type: 'list', name: 'deploy', message: '部署方式', choices: ['k8s', 'pm2'] },
    ]);
    await renderTemplates(name, answers);           // ejs 渲染模板目录
    await execa('npm', ['install'], { cwd: name, stdio: 'inherit' });
    console.log(`完成：cd ${name} && npm run dev`);
  });
program.parse();
// package.json: "bin": { "acme": "./bin/acme.js" } → npm link 后全局可用
```
