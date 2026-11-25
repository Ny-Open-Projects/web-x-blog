---
title: [AGT-864] AI 辅助微前端开发时（跨应用调用/共享依赖），如何防止 AI 生成破坏边界的代码？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-864：AI 辅助微前端开发时（跨应用调用/共享依赖），如何防止 AI 生成破坏边界的代码

**答**：
- 边界规则注入 AI 上下文：哪些跨应用调用必须走事件总线/不能直接 import 兄弟应用代码/共享依赖只能用声明版本——规则写成 lint（eslint-plugin 边界规则）+AI rules 双层，AI 违规产出会被 lint 拦截。
- 契约测试护航：跨应用接口的契约测试（provider 验证），AI 改动跨应用接口时自动触发对方应用的契约验证。
- 影响 AI 上下文：只喂当前子应用+契约定义，不喂兄弟应用实现（既省上下文又防 AI "顺手"改别家代码）。

```javascript
// 边界规则：AI 产出必须过这道lint
const boundaryRules = {
  'no-cross-app-import': (imp) => !imp.path.startsWith('../other-app'),
  'shared-dep-version': (imp) => imp.version === DECLARED[imp.pkg],
};
function aiGuard(output) {
  const violations = lint(output, boundaryRules);
  if (violations.length)
    return ai.revise(output, violations, { hint: BOUNDARY_DOC });
  return output;
}
```

