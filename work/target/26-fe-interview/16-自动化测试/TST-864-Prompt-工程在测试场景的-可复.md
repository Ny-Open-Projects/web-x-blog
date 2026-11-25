---
title: [TST-864] Prompt 工程在测试场景的「可复用性」如何保证？（prompt 版本管理）
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-864：Prompt 工程在测试场景的「可复用性」如何保证？（prompt 版本管理）
**答**：
- 结论：把 prompt 当「代码」管理——版本化、参数化、可测试、可回滚，避免 prompt 散落在聊天记录里无法复现。
- 做法：prompt 模板存仓库（含变量占位符），与测试代码一起 review；变更走 PR 并跑「prompt 回归测试」。
- 参数化：把项目特有信息（框架、规范）抽成变量，而非写死在 prompt 里，便于跨项目复用。
- 可观测：记录每次调用的 prompt 版本 + 模型 + 参数，生成质量异常时能定位是哪个版本导致。
- 追问钩子：prompt 微调后效果「好像变好了又好像变差了」，你如何用数据而非感觉判断？

```javascript
// Prompt 模板：版本化 + 参数化
const PROMPT_TEMPLATES = {
  'gen-unit-test@v2': {
    version: '2.1.0',
    template: (ctx) => `为 ${ctx.framework} 函数 ${ctx.fnName} 生成测试，遵循 ${ctx.styleGuide}，覆盖正常/边界/异常。`,
    variables: ['framework', 'fnName', 'styleGuide'],
  },
};
function renderPrompt(id, vars) {
  const t = PROMPT_TEMPLATES[id];
  if (!t) throw new Error(`未知 prompt ${id}`);
  const missing = t.variables.filter(v => !(v in vars));
  if (missing.length) throw new Error(`缺少变量 ${missing.join(',')}`);
  return { version: t.version, text: t.template(vars) };
}
console.log(renderPrompt('gen-unit-test@v2', {
  framework: 'Vitest', fnName: 'formatMoney', styleGuide: '团队规范A'
}));
```
