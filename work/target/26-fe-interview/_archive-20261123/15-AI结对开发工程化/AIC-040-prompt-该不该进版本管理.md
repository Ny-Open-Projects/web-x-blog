---
title: [AIC-040] Prompt 模板该不该进 Git 版本管理？「Prompt as Code」包含哪些工程实践？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-040：Prompt 模板该不该进 Git 版本管理？「Prompt as Code」包含哪些工程实践？
**答**：
- 必须进版本管理：prompt 决定产出质量，不进 Git 意味着无法回滚、无法追溯「为什么那次生成变差了」、团队各自私藏模板无法共享。
- Prompt as Code 实践：模板文件化（prompts/*.md + 变量槽位）、变更走 PR review、语义化版本、附带回归测试集（固定输入→期望输出要点）。
- 代码评审要点：模板改动要看「约束是否仍符合团队红线」「变量是否足够注入」「长度是否失控」，同代码一样提评论。
- 测试方式：批跑测试集对比新旧模板的通过率，退化则阻断合并——这就是 prompt 的 CI。
- 追问钩子：模板库可以和规则文件共用治理体系，因为规则文件本质就是「常驻 prompt」。

```javascript
// prompts/unit-test.md 的加载与变量注入（模板即资源）
import { readFileSync } from 'fs';
function loadPrompt(name, vars) {
  const raw = readFileSync(`prompts/${name}.md`, 'utf8');
  const missing = [...raw.matchAll(/\{\{(\w+)\}\}/g)]
    .map(m => m[1]).filter(k => !(k in vars));
  if (missing.length) throw new Error(`missing template vars: ${missing}`); // 槽位必须齐全
  return raw.replace(/\{\{(\w+)\}\}/g, (_, k) => vars[k]);
}
// CI 中：git diff prompts/ 有变更时 → 自动跑 prompt 回归集
```
