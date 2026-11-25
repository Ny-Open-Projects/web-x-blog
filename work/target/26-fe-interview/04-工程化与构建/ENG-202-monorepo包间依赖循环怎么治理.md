---
title: [ENG-202] monorepo 的包间循环依赖怎么治理？怎么从「禁止」到「可控」？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-202：包间循环依赖怎么治理？
**答**：
- 分层治理：先分层定义（core ← ui ← feature ← app），层间只允许单向依赖；用 dependency-cruiser/ESLint boundaries 规则把分层变成 CI 门禁。
- 循环破除手法：类型循环用 `import type`（类型层不产生运行时依赖）；逻辑循环抽第三方包（公共逻辑下沉）或依赖倒置（定义接口在底层，实现在高层注入）。
- 存量循环治理：先「标记存量 + 冻结增量」——CI 只拦新增循环，存量按调用热度排期清理；一步到位禁所有循环会让团队绕过规则（加 eslint-disable）。
- 可控循环例外：真有双向需求时用事件解耦（A 发事件 B 订阅）而不是硬解。
- 追问钩子：为什么 import type 不算循环——TS 类型在编译期擦除，运行时无模块加载；但这依赖「verbatimModuleSyntax/isolatedModules」保证不被编译成真实 import。

```javascript
// dependency-cruiser 规则：分层单向
module.exports = {
  forbidden: [{
    name: 'no-cross-layer-upward',
    from: { path: '^packages/feature' },
    to: { path: '^packages/core', dependencyTypes: ['local'] },
  }, {
    name: 'no-circular',
    cyclic: true,
  }],
};
// 依赖倒置破循环：core 定义 interface Logger，feature 实现，app 注入
// core: export interface Logger { log(m: string): void }   —— 不 import feature
```
