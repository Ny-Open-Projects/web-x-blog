---
title: [BLD-103] NormalModuleFactory 的 resolve 流程：enhanced-resolve 如何把 './a' 变成绝对路径？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-103：NormalModuleFactory 的 resolve 流程：enhanced-resolve 如何把 './a' 变成绝对路径？
**答**：
- 每个依赖先经过 `normalModuleFactory.hooks.factorize → resolve → factory.create()`；resolve 阶段核心是 `compiler.resolverFactory.get('normal', resolveOptions)` 产出的 enhanced-resolve Resolver（loader 有独立 resolver，支持 loader 路径相对查找）。
- enhanced-resolve 自身是插件化管线：`Resolver` 内部一条 steps 链，alias/extensions/mainFields/descriptionFiles/exportsField 各是一个解析插件节点，`unsafeCache` 对目录 lstat 结果做缓存避免重复 IO。
- 解析顺序：精确文件 → 补 extensions（.js/.ts/.json）→ 目录（读 package.json 的 exports/main → index.js）；默认 `symlinks: true` 即 resolve 到真实路径，防止 pnpm 下双实例。
- 失败抛 `ModuleNotFoundError`（挂在 compilation.errors）；resolve 失败常见根因是 exports 字段屏蔽了深层路径、alias 大小写不匹配、pnpm 幽灵依赖。

```javascript
// 1) 直接使用 enhanced-resolve：理解 webpack 的 resolve 内核
const enhancedResolve = require('enhanced-resolve');
const resolver = enhancedResolve.create.sync({
  context: __dirname,
  extensions: ['.ts', '.tsx', '.js', '.jsx', '.json'],
  mainFields: ['browser', 'module', 'main'],
  conditionNames: ['import', 'require'],   // 对应 package.json exports 的条件
  symlinks: true,                          // resolve 到真实路径，避免 pnpm 双实例
  unsafeCache: true,
});
console.log(resolver(__dirname, './a'));   // /abs/path/to/a.ts

// 2) 在 webpack 侧观测/干预 resolve：tap NormalModuleFactory 的 resolve 钩子
class ResolveProbePlugin {
  apply(compiler) {
    compiler.hooks.compilation.tap('ResolveProbePlugin', (compilation, { normalModuleFactory }) => {
      normalModuleFactory.hooks.resolve.tap('ResolveProbePlugin', (data) => {
        // data.request 是原始请求，data.context 是发起目录；可在此改写请求
        if (data.request === 'lodash') data.request = 'lodash-es';
      });
      normalModuleFactory.hooks.factorize.tapAsync('ResolveProbePlugin', (data, cb) => {
        const t0 = Date.now();
        const done = (err, result) => {
          if (result) {
            // 记录慢 resolve：CI 中定位"哪个请求解析最慢"
            console.log('[resolve]', data.request, Date.now() - t0 + 'ms');
          }
          cb(err, result);
        };
        // 不接管流程，仅观测：tap before 其他 resolver 插件即可
        done(null, undefined); // 纯演示，真实实现应调用 originalCb 或改用 intercept
      });
    });
  }
}
// resolverFactory 层的拦截（更正规）：
// compiler.resolverFactory.hooks.resolver
//   .tap('Slow', (resolver, options) => resolver.hooks.result.tap('Slow', r => r));
```
