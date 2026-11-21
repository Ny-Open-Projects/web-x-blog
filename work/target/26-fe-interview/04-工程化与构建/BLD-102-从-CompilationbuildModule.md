---
title: [BLD-102] 从 Compilation.buildModule 到 module.build，loader 到底是在哪一步被执行的？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-102：从 Compilation.buildModule 到 module.build，loader 到底是在哪一步被执行的？
**答**：
- 调用链：`compilation.addEntry()` → `addModuleChain/handleModuleCreation` → `_addModuleData` → `compilation.buildModule(module)` → `module.build(options, compilation, resolver, fileSystem, callback)`。
- `NormalModule.build` 内部先 `this.doBuild()`：创建 loaderContext（含 this.async/this.callback/this.data），然后把 loader 数组交给 `loader-runner` 的 `runLoaders`——**loader 的真正执行入口是 NormalModule.doBuild 调用的 runLoaders**，pitch 阶段倒序、normal 阶段正序都在这里。
- doBuild 返回后的源码顺序：处理 loader 报错（`markModuleAsErrored`）或继续 → 把 loader 产物包成 `OriginalSource` 赋给 `this._source` → 用 parser（acorn）`parser.parse(source)` 生成 AST 并收集 dependencies → build 完成触发 `compilation.hooks.buildModule/afterBuild`。
- 面试要点：loader 抛错只让单个 module 标记 error 不中断构建；build 是"每个模块一次"，rebuild（HMR）只对失效模块重跑 build。

```javascript
// NormalModule.build 精简伪源码（webpack5，标注 loader 执行位置）
class NormalModule extends Module {
  build(options, compilation, resolver, fs, callback) {
    this._forceBuild = false;              // 缓存体系用
    return this.handleBuildTask(options, compilation, (err) => {
      // ...构建完成收尾
    });
  }
  _doBuild(options, compilation, resolver, fs, callback) {
    const loaderContext = this.createLoaderContext( // ① 造 loader 上下文
      resolver, options, compilation, fs
    );
    const processResult = (err, result) => {
      if (err) return this.markModuleAsErrored(/*...*/);   // loader 报错不中断整体构建
      const javascript = result[0];                        // ② loader 链最终产物字符串
      // ③ 关键分界：loader 在 runLoaders 内已全部执行完，下面才轮到 parser
      this._source = new OriginalSource(javascript, this.identifier());
    };
    // ④ loader 执行入口：iterate loaders + loader-runner 的 runLoaders
    runLoaders(
      {
        resource: this.resource,            // 绝对路径资源
        loaders: this.loaders,              // [{ loader, options }] 已 resolve 成绝对路径
        context: loaderContext,
        readResource: compilation.compiler.readFile? // fs 读取封装（含 memfs 替换点）
      },
      (err, result) => processResult(err, result)
    );
  }
  // doBuild 之后（省略中间细节）：
  markModuleAsErrored /* ... */
  // build 尾部：  const { source } = this.parse?
  // 实际： this._source = new OriginalSource(javascript, this.identifier());
  //       parser.parse(this._source.ast? , { module: this, ... })
  //       —— parser 在解析中往 this.dependencies 里 push Dependency
  //       最后 callback() 回到 compilation.buildModule → 处理 dependencies 递归
}
```
