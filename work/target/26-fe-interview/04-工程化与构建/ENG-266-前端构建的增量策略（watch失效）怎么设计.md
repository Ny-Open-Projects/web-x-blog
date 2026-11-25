---
title: [ENG-266] 构建增量策略（watch 模式/缓存失效边界）怎么设计？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-266：增量策略怎么设计？
**答**：
- 失效粒度：模块级失效（改一个文件只重转该文件及其反向依赖闭包）——失效粒度粗（整项目重跑）让增量名存实亡。
- 依赖追踪完整性：动态导入/worker 文件/css @import/字体引用都要进依赖图，漏追踪导致「改了不生效」——比慢更伤害信任。
- watch 与持久缓存协同：首次启动加载持久缓存（冷启动秒开），后续改动增量失效。
- 虚拟模块与插件失效：插件产物（codegen/svg sprite）作为虚拟模块参与失效图。
- 追问钩子：为什么「改了不生效」比「构建慢」更严重——慢只是等待，用户可以忍；不生效让开发者开始怀疑工具（重启构建/清缓存），进入「迷信操作」状态，DevEx 崩塌；失效完整性是增量构建的生命线。

```javascript
// 失效图完整性检查（dev 冒烟）
async function invalidationSmokeTest() {
  await dev.start();
  edit('src/a.ts', 'export const x = 2');
  await expectHmr('src/a.ts');
  edit('styles/main.css', '.a { color: red }');   // css @import 链
  await expectHmr('styles/main.css');
  edit('worker.js');                               // worker 依赖
  await expectRebuild('worker.js');
}
```
