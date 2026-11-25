---
title: [AGT-011] Prompt 模板如何管理？怎样避免提示词散落各处、改一次发一次版？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-011：Prompt 模板如何管理？怎样避免提示词散落各处、改一次发一次版？
**答**：
- 提示词当资产管理：中心化存储、`{{变量}}` 插值、版本号，可放配置中心或独立文件。
- 渲染时校验变量缺失，缺参直接报错而不是渲染出空字符串。
- 版本化后可做 A/B 与评测回归（AGT-039），换版本先用评测集跑一遍再上线。
- 复杂模板可用 Jinja2 语法或成熟库（如 LangChain PromptTemplate），自研一个 30 行的插值器也够用。

```typescript
// Prompt 模板：{{变量}} 插值 + 中心化版本管理，改提示词不需要发版
const F = '\u0060'.repeat(3);   // 围栏用码点构造，避免源码内出现字面围栏
const templates = {
  'code-review': {
    version: 'v3',
    template: '请审查以下 {{language}} 代码，重点关注 {{focus}} 问题：\n' + F + '\n{{code}}\n' + F,
  },
} as const;

type TemplateKey = keyof typeof templates;

function renderPrompt(key: TemplateKey, vars: Record<string, string>): string {
  return templates[key].template.replace(/\{\{(\w+)\}\}/g, (_, name: string) => {
    if (!(name in vars)) throw new Error(`模板 ${key} 缺少变量 ${name}`);
    return vars[name];
  });
}

const prompt = renderPrompt('code-review', {
  language: 'typescript',
  focus: '内存泄漏',
  code: 'window.__cache.push(document.createElement("div"))',
});
```
