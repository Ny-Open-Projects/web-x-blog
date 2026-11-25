---
title: [AIC-690] 团队用多个 IDE，AI 规则怎么统一分发？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-690：团队用多个 IDE（Cursor/Copilot/Claude Code），AI 规则怎么统一分发？

**答**：
- 结论先行：**「单一规则源 + 编译时分发」——维护一份团队规范源文件，自动转换成各 IDE 的规则格式，不要再每个 IDE 各写一份**（AIC-203 双 IDE 支持）。
- 痛点：Cursor 用 `.cursor/rules`、Copilot 用 `.github/copilot-instructions.md`、Claude Code 用 `CLAUDE.md`——各写一份必然不同步，A IDE 加了规范 B IDE 没加。
- 方案：1) **单一源**：用一种中立格式（如 `ai-rules.yaml`）维护团队规范，带 glob/优先级/元数据；2) **转换器**：写脚本/CI 把中立源转成各 IDE 格式，提交时自动生成（AIC-005 规则合并器）；3) **CI 校验**：检查各 IDE 规则文件是否与源一致，不一致就报错——防止有人手动改了分发生成的文件；4) **版本化**：规则源进 git，变更走 review。
- 内容分层：通用规范（全 IDE 生效）放源；IDE 特有配置（如某 IDE 的特定语法）单独放适配层——避免为迁就某 IDE 污染通用规范。
- 追问钩子：为什么「单一源 + 自动生成」优于「人工同步多份」？——因为人工同步必然遗漏（人不是编译器，不会记得每个副本都要改），而自动生成是确定性的——改一次源，所有 IDE 规则同时更新；把「靠人记得同步」变成「机器保证同步」。

```typescript
type Rule = { glob: string; content: string };

// 单一源 → 多 IDE 格式转换器
function distributeRules(rules: Rule[], ide: 'cursor'|'copilot'|'claude'): string {
  if (ide === 'cursor') {
    return rules.map((r, i) => `---
glob: ${r.glob}
---
# rule-${i}
${r.content}`).join('

');
  }
  if (ide === 'copilot') {
    return rules.map(r => `<!-- ${r.glob} -->
${r.content}`).join('

');
  }
  return rules.map(r => `## ${r.glob}
${r.content}`).join('

'); // claude: markdown
}

const rules = [
  { glob: '**/*.tsx', content: '用函数组件，禁止 class' },
  { glob: 'src/api/**', content: 'API 调用必须带错误处理' },
];
console.log(distributeRules(rules, 'cursor').includes('glob: **/*.tsx'));
console.log(distributeRules(rules, 'copilot').includes('<!-- **/*.tsx -->'));
console.log(distributeRules(rules, 'claude').includes('## src/api/**'));
```
