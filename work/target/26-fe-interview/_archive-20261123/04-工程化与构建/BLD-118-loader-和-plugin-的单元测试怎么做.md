---
title: [BLD-118] loader 和 plugin 的单元测试怎么做？memfs 虚拟文件系统方案。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-118：loader 和 plugin 的单元测试怎么做？memfs 虚拟文件系统方案。
**答**：
- loader 测试两层：纯函数层（loader 主体抽成 `transform(source, options)` 直接断言输出）与集成层（用 webpack 的 `runLoaders` 或 mini compilation 在真实管线里跑）。
- plugin/完整构建测试：webpack 官方测试栈是 `webpack/test` 的 `compile()` helper + **memfs**（把 OutputFileSystem 换成内存文件系统），构建产物直接从内存读，不落盘、可并发、快。
- 关键 API：`compiler.outputFileSystem = createFsFromVolume(new Volume())`；断言用 `outputFileSystem.readFileSync('/dist/main.js')`；sourcemap 用 `SourceMapSource` 消费。
- 快照策略：jest `toMatchSnapshot` 断言产物关键片段（别全量快照，contenthash 会抖动）；断言 error 列表用 `stats.toJson({ errors: true })`。

```javascript
// test/loader.test.js：memfs 方案测试一个自定义 loader 与一个 plugin
import { webpack } from 'webpack';
import { createFsFromVolume, Volume } from 'memfs';
import myLoader from '../src/loader.cjs';
import BannerAuditPlugin from '../src/banner-audit-plugin.cjs';

const compile = (fixture) =>
  new Promise((resolve, reject) => {
    const compiler = webpack({
      mode: 'none',
      context: '/project',
      entry: '/project/entry.js',
      output: { path: '/dist', filename: 'main.js' },
      module: {
        rules: [{ test: /\.special\.js$/, use: [{ loader: myLoader, options: { flag: true } }] }],
      },
      plugins: [new BannerAuditPlugin()],
    });
    // 关键：内存文件系统替换（memfs）
    compiler.outputFileSystem = createFsFromVolume(new Volume());
    compiler.inputFileSystem = compiler.outputFileSystem;
    compiler.intermediateFileSystem = compiler.outputFileSystem;
    // 预置虚拟项目文件
    compiler.outputFileSystem.mkdirSync('/project', { recursive: true });
    compiler.outputFileSystem.writeFileSync('/project/entry.js', fixture);
    compiler.run((err, stats) => {
      if (err) return reject(err);
      const errors = stats.toJson({ errors: true }).errors;
      const output = compiler.outputFileSystem.readFileSync('/dist/main.js', 'utf8');
      resolve({ errors, output });
    });
  });

test('myLoader 转换内容正确且 plugin 产物含审计标记', async () => {
  const { output } = await compile("import x from './a.special.js'; export default x;");
  expect(output).toMatch('__AUDIT__');       // plugin 注入的标记
  expect(output).toContain('transformed');   // loader 的转换结果
});
```

## 十三章 Babel 与 AST 深入（BLD-119 ~ BLD-128）
