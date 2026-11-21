---
title: [BLD-010] compiler.hooks 中常用的钩子按时机排列有哪些？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-010：compiler.hooks 中常用的钩子按时机排列有哪些？
**答**：
- 初始化：environment / afterEnvironment → entryOption（遍历 entry 时）→ afterPlugins / afterResolvers → beforeRun / run。
- 编译前：watchRun（watch 模式专属）→ beforeCompile（可改 compilationParams）→ compile → thisCompilation → compilation。
- 编译中：make（核心，addEntry 从这里发起）→ buildModule → finishModules → seal → optimizeModules / optimizeChunks / optimizeTree / optimizeChunkModules → shouldEmit / emit。
- 收尾：afterEmit → done（拿 stats 输出报告）；失败路径：failed。
- watch 相关：watchClose、invalid（文件变化触发重编译前）、additionalAssets。

```javascript
// webpack.config.js：hooks 时机速查插件（注释即时机表）
class HookTimelinePlugin {
  apply(compiler) {
    const n = 'HookTimelinePlugin';
    compiler.hooks.environment.tap(n, () => {});            // 1 编译环境准备
    compiler.hooks.entryOption.tap(n, () => {});            // 2 处理 entry 配置
    compiler.hooks.afterPlugins.tap(n, () => {});           // 3 所有插件注册完
    compiler.hooks.beforeRun.tapAsync(n, (p, cb) => cb());  // 4 run 之前
    compiler.hooks.run.tapAsync(n, (p, cb) => cb());        // 5 开始读取文件前
    compiler.hooks.beforeCompile.tap(n, () => {});          // 6 每次编译前 可改参数
    compiler.hooks.make.tapAsync(n, (compilation, cb) => cb()); // 7 编译模块图
    compiler.hooks.afterCompile.tap(n, (c) => {});          // 8 模块图完成
    compiler.hooks.shouldEmit.tap(n, (c) => true);          // 9 是否产出的开关
    compiler.hooks.emit.tapAsync(n, (c, cb) => cb());       // 10 写 dist 之前 最后改产物机会
    compiler.hooks.done.tap(n, (stats) => {                 // 11 成功完成
      if (stats.hasErrors()) console.error(stats.toString({ colors: true }));
    });
    compiler.hooks.failed.tap(n, (err) => console.error('构建失败', err)); // 12 失败
    compiler.hooks.invalid.tap(n, (file) =>                 // watch 模式 文件变化
      console.log('检测到变化 触发重编译', file));
  }
}
module.exports = HookTimelinePlugin;
```
