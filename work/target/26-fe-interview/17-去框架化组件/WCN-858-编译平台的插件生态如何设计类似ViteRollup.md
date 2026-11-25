---
title: [WCN-858] 编译平台的「插件生态」如何设计？（类似 Vite/Rollup）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-858：编译平台的「插件生态」如何设计？（类似 Vite/Rollup）

**答**：
- 结论先行：插件生态的关键是「定义清晰的生命周期钩子 + 统一的上下文对象 + 可组合的变换管线」——插件在钩子里读写 IR/产物，平台按顺序调度，从而让第三方能扩展而不改内核。
- 钩子设计：参考 Rollup——`buildStart`、`resolveId`、`load`、`transform`（源码/AST/IR 变换）、`optimizeIr`（IR 优化 Pass）、`generateBundle`（产物后处理）、`buildEnd`；编译平台特有 `parse`、`lower`（前端特有阶段）。
- 上下文对象：钩子拿到 `ctx`（含当前文件路径、源码、AST/IR、配置、日志、emitFile、addWatchFile），插件通过它交互而非全局状态。
- 顺序与并行：变换钩子串行（有依赖），分析/优化钩子可并行；用 `enforce: 'pre'|'post'` 控制顺序；插件间通过「虚拟模块」传递数据。
- 稳定性：插件 API 要版本化，避免内核升级破坏所有插件；type 定义完善；提供官方脚手架与示例降低贡献门槛。
- 追问钩子：面试官会问「插件之间冲突怎么办」——答：明确执行顺序 + 幂等约束 + 用虚拟模块而非直接改同一份数据；对破坏性插件提供隔离沙箱与回滚（如变换失败回退原内容）。

```javascript
// 迷你插件系统：生命周期钩子 + 上下文 + 串行变换
function createCompiler(config) {
  const plugins = config.plugins || [];
  const ctx = { config, warn: (m) => console.warn('[plugin]', m), files: new Map() };
  function runHook(name, arg) {
    return plugins.reduce(async (acc, p) => {
      let cur = await acc;
      if (p[name]) cur = (await p[name].call(ctx, cur)) ?? cur; // 钩子可返回新值
      return cur;
    }, Promise.resolve(arg));
  }
  return {
    async build(entry) {
      let src = await runHook('load', entry);
      src = await runHook('transform', src);
      const ir = await runHook('lower', { code: src });
      return runHook('generateBundle', ir);
    },
  };
}
const transformer = { name: 'strip-comments', transform(code) { return code.replace(/\/\/.*$/gm, ''); } };
const c = createCompiler({ plugins: [transformer] });
c.build('let a=1 // hi').then(r => console.log(r));
```
