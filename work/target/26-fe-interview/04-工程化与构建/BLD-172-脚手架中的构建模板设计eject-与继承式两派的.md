---
title: [BLD-172] 脚手架中的构建模板设计：eject 与继承式两派的取舍。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-172：脚手架中的构建模板设计：eject 与继承式两派的取舍。
**答**：
- **eject 派**（CRA 风格）：模板复制进项目，完全自主、无黑盒；代价是无法接收上游升级（放弃治理），适合"脚手架只是起点"的团队。
- **继承派**（vue-cli service / Rspack Rsbuild / 内部 preset 包）：配置藏在依赖里，CLI 驱动；升级 = 升依赖版本；灵活性靠 plugin/配置合并钩子——主流选择。
- 混合实践：默认继承 + `--eject` 逃生门（导出当前 resolved 配置），配合"配置快照测试"（升级 preset 后跑产物 diff）。
- 脚手架模板要点：模板即代码（handlebars/占位符注入项目名、registry、上报 ID）、生成后必须可跑（含 dev/test/build 三命令）、留 TODO 标记可裁剪区。

```javascript
// 继承式脚手架的 service 层设计（@org/cli-service 简化版）
// package.json bin: { "org-service": "./bin/service.js" }
// bin/service.js：命令分发（dev/build/test 都收敛到 service，项目不直接写 webpack）
const createConfig = require('../lib/create-config');
const webpack = require('webpack');
const WebpackDevServer = require('webpack-dev-server');

async function serve() {
  const config = await createConfig({
    projectRoot: process.cwd(),
    // 读项目级可选配置：org.config.js（继承派的项目入口）
    userConfig: requireIfExists('./org.config.js'),
  });
  const server = new WebpackDevServer({ ...config.devServer, hot: true }, webpack(config));
  await server.start();
}
// eject 逃生门：把 resolved 配置落到项目里，从此脱离 preset
async function eject() {
  const config = await createConfig({ projectRoot: process.cwd(), userConfig: loadUser() });
  await fs.writeFile('webpack.config.ejected.js', `module.exports = ${util.inspect(config, { depth: 20 })}`);
  console.log('已导出配置；后续升级 preset 不再影响本项目（自负维护）');
}
// 选型结论：默认继承 + 服务化 CLI + 可 eject——治理与自由的折中
```
