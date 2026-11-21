---
title: [BLD-014] 插件中的错误如何正确抛出？什么时机 fail 合适？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-014：插件中的错误如何正确抛出？什么时机 fail 合适？
**答**：
- 同步钩子直接 throw：webpack 会捕获并进入 failed 流程，构建失败退出码非 0。
- 异步钩子（tapAsync）用 callback(new Error(...))，tapPromise 直接 reject；不要在异步里 throw（会变成 unhandled rejection）。
- 警告走 compilation.warnings.push(new Error(...))，错误走 compilation.errors.push：警告不阻断构建，错误阻断；CI 卡口建议用错误。
- fail 时机选择：影响产物正确性的（如缺少必需文件）越早越好，可在 beforeCompile 就校验；只影响告警的在 processAssets 阶段报。

```javascript
// robust-plugin.js
class RobustPlugin {
  constructor({ requiredFile } = {}) { this.requiredFile = requiredFile; }

  apply(compiler) {
    // 1 影响正确性 在编译前就 fail-fast（tapAsync 用 callback 报错）
    compiler.hooks.beforeCompile.tapAsync('RobustPlugin', (params, cb) => {
      if (this.requiredFile && !fs.existsSync(this.requiredFile)) {
        return cb(new Error(`RobustPlugin 缺少必需文件 ${this.requiredFile}`));
      }
      cb();
    });

    compiler.hooks.compilation.tap('RobustPlugin', (compilation) => {
      // 2 可容忍问题 推 warnings 不阻断构建
      compilation.hooks.processAssets.tap('RobustPlugin', (assets) => {
        const big = Object.values(assets).filter((s) => s.size() > 1024 * 500);
        if (big.length) {
          compilation.warnings.push(new Error(`有 ${big.length} 个产物超过 500KB，请检查分包`));
        }
      });
    });
  }
}
const fs = require('fs');
module.exports = RobustPlugin;
```
