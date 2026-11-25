---
title: [ENG-067] 手写一个 CLI 脚手架的核心流程是怎样的？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 笔试题, 08]
type: 笔试题
---

## ENG-067：手写一个 CLI 脚手架的核心流程是怎样的？
**答**：
- 入口：package.json 的 bin 字段注册命令，文件头加 #!/usr/bin/env node（shebang）。
- 命令解析用 commander（或 cac）：定义 create 子命令、参数与选项。
- 主流程串联：交互问答（prompts）→ 拉取模板（git clone 或 npm 包内拷贝）→ 变量注入 → 安装依赖 → git init。
- 工程化细节：失败要清理半成品目录，输出统一加 logger 前缀，支持 --template 透传跳过交互。

```javascript
#!/usr/bin/env node
import { Command } from 'commander';
import { create } from './commands/create.js';

const program = new Command();

program
  .name('my-cli')
  .description('团队前端脚手架')
  .version('1.0.0');

program
  .command('create <name>')
  .description('创建一个新项目')
  .option('-t, --template <template>', '指定模板', 'vue3-ts')
  .option('--skip-install', '跳过依赖安装')
  .action((name, options) => create(name, options));

program.parse(process.argv);
```
