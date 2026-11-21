---
title: [BLD-173] 构建参数 CLI 化：怎么设计"构建时覆盖配置"的参数体系？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-173：构建参数 CLI 化：怎么设计"构建时覆盖配置"的参数体系？
**答**：
- 分层优先级：CLI 参数 > 环境变量 > 项目配置文件 > preset 默认值；每一层的覆盖都必须**可观测**（构建日志打印"某参数被谁覆盖"），否则排查"产物为什么和预期不一样"会浪费大量时间。
- 参数设计原则：暴露**意图参数**（--analyze、--sourcemap、--target=edge）而非暴露 webpack 原生字段；`--config-overrides ./extra.js` 作为完整逃生门。
- 实现要点：`yargs`/`cac` 定义参数 → 归一化为内部 BuildOptions → 传给 preset 工厂；`--env` 透传给 webpack（env 对象）。
- 反模式：CLI 参数里塞复杂对象（JSON 字符串拼配置）——CLI 只做开关与数值，复杂结构走配置文件。

```javascript
// bin/build.js：生产级构建 CLI（yargs 版）
const yargs = require('yargs/yargs');
const { hideBin } = require('yargs/helpers');

const argv = yargs(hideBin(process.argv))
  .option('mode', { choices: ['development', 'production'], default: 'production' })
  .option('analyze', { type: 'boolean', desc: '构建后打开产物分析' })
  .option('sourcemap', { choices: ['none', 'inline', 'external', 'hidden'], default: 'external' })
  .option('config-overrides', { type: 'string', desc: '追加 webpack 配置的 js 文件' })
  .option('profile', { type: 'boolean', desc: '输出构建性能 profile' })
  .strict().parse();

// 优先级链：CLI > env > config > preset（每层覆盖打日志）
const layers = { cli: argv, env: pickEnv(['BUILD_TARGET', 'APP_ENV']), file: require('./build.config.js') };
const options = { mode: 'production', sourcemap: 'external', ...layers.file, ...layers.env, ...layers.cli };
console.log('[build] effective options:', JSON.stringify(options));   // 可观测：最终生效值

const config = createAppConfig(options);
if (argv['config-overrides']) {
  config = require('webpack-merge')(config, require(path.resolve(argv['config-overrides'])));
}
webpack(config, (err, stats) => {
  if (argv.analyze) execSync(`npx webpack-bundle-analyzer dist/stats.json`);
  process.exit(err || stats.hasErrors() ? 1 : 0);
});
// 使用：org-service build --analyze --sourcemap=hidden --config-overrides ./perf.js
```
