---
title: [ENG-203] monorepo 的变更影响面（谁受这个 PR 影响）怎么自动计算？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-203：变更影响面怎么自动计算？
**答**：
- 构建图快照：CI 上跑 affected 分析（turborepo --filter=...[base]），输出受影响包清单 → 派生动作（跑哪些测试/哪些 app 需要重新构建/哪些 owner 需要评审）。
- 影响面分级：直接依赖（改了包本身）→ 传递依赖（消费方）→ 发布面（哪些 app 产物含此包）；PR 描述自动生成影响清单。
- 语义化影响：patch/minor/major 由 API diff 推断（导出签名变化 = minor+），结合 conventional commits 校验版本号合理性——发布机器人自动定版本。
- 评审路由：受影响包的 CODEOWNERS 自动加为 reviewer，测试覆盖不足的包标红提示。
- 追问钩子：为什么影响面不能只看 import 图——动态导入/字符串引用/样式类名约定不在 import 图里；影响面 = 静态图 ∪ 测试覆盖 ∪ 运行时约定，静态图只是基底。

```javascript
// CI 影响面脚本
const affected = exec('turbo run build --dry=json --filter=...[origin/main]');
const packages = JSON.parse(affected).tasks.map(t => t.package);
console.log(`影响包: ${packages.join(', ')}`);
// 派生动作
assignReviewers(packages.flatMap(p => OWNERS[p]));
runTests(packages);
checkVersionBump(packages);        // API diff 推断 semver
```
