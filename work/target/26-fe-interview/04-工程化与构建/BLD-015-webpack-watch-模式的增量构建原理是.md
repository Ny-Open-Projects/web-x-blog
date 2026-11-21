---
title: [BLD-015] webpack watch 模式的增量构建原理是什么？invalid 钩子和文件系统缓存怎么配合？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-015：webpack watch 模式的增量构建原理是什么？invalid 钩子和文件系统缓存怎么配合？
**答**：
- watch 模式基于文件系统Watcher（默认 Watchpack，聚合抖动 aggregateTimeout）：文件变化 → 触发 invalid 钩子 → 标记失效模块（只失效变化文件所在模块及其反向依赖所在 chunk）→ 重新走 make 只编译受影响模块。
- 增量来源有两层：模块图复用（未变模块不重新 buildModule）+ 持久缓存（experimental cache: filesystem，rebuild 直接读磁盘缓存反序列化模块）。
- invalid 钩子参数是变化的文件路径，可用于 IDE 通知、日志埋点；watchClose 处理清理。
- 优化参数：aggregateTimeout 防抖、ignored 排除 node_modules、poll 轮询兜底（docker/网络盘需要）。

```javascript
// webpack.config.js：watch 相关完整配置
module.exports = {
  cache: {
    type: 'filesystem',                       // 持久化缓存 依赖 snapshot
    buildDependencies: {
      config: [__filename],                   // 配置文件变化即缓存失效
    },
  },
  snapshot: {
    managedPaths: [/^(.+?[\\/]node_modules[\\/])/], // node_modules 走托管快照 不参与时间戳比对
  },
  watchOptions: {
    aggregateTimeout: 300,   // 300ms 抖动合并 多文件连续保存只编译一次
    ignored: /node_modules/, // 不监听三方库
    followSymlinks: false,
  },
};

// 插件侧观察增量过程
compiler.hooks.invalid.tap('WatchDebug', (filePath, changeTime) => {
  console.log('invalid 变化文件', filePath);
});
compiler.hooks.watchRun.tap('WatchDebug', () => console.log('开始增量编译'));
compiler.hooks.done.tap('WatchDebug', (s) => {
  console.log('本次耗时', s.endTime - s.startTime, 'cached 模块数',
    s.toJson().modules.filter((m) => m.cached).length);
});
```
