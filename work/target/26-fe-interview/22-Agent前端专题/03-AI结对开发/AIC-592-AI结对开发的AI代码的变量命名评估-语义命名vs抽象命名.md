---
title: [AIC-592] AI 代码的变量命名评估
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-592：AI 代码变量命名评估

**答**:
- AI 变量命名的问题模式：1) **泛型命名**（`data`/`result`/`item`/`value`/`temp`——不表达业务含义（"data"是什么数据？商品？用户？——命名应含业务上下文：`products`/`userProfile`）；2) **不一致命名**（同一概念多种命名——`userId`/`user_id`/`uid`/`id`（同一文件中混用——一致性丢失）；3) **缩写过度**（`usr`/`prd`/`cfg`——缩写节省打字但增加阅读负担（`user` 比 `usr` 更可读）；4) **匈牙利命名法残留**（`strName`/`intCount`——类型前缀在 TypeScript 中冗余（类型系统已经标注了类型）。
- 命名的评估维度：1) **语义明确度**（`getUserOrders` 明确 vs `getData` 模糊——命名是否表达"做什么"与"关于什么"；2) **一致性**：camelCase for variables/functions、PascalCase for types/components（命名规范的统一）；3) **长度适中**（3~30 字符——太短（`x`/`d`）不可读、太长（`theUserThatCurrentlyHasOrdersBeingLoaded`）难读。
- 追问钩子：为什么「AI 的泛型命名」比「人的泛型命名」更有害？——人用 `data` 通常有上下文（写 `data` 时知道自己指的是什么——上下文弥补了命名的模糊）；AI 用 `data` = 无上下文（LLM 生成时的"通用回退名"——不代表任何具体业务概念）；「AI 命名的模糊性」：AI 生成 `data` 时可能自己都不知道 data 是什么（训练数据中 `data` 是最常见的变量名——LLM 的"默认回退"）——人读 AI 的 `data` 时完全无法推断含义。

```typescript
// 变量命名质量评估
function assessNaming(code: string) {
  const GENERIC_NAMES = new Set(['data', 'result', 'item', 'value', 'temp', 'obj', 'res', 'ret']);
  const issues: { name: string; type: string; line: number }[] = [];
  code.split('\n').forEach((line, i) => {
    // 泛型命名
    for (const m of line.matchAll(/(?:const|let|var)\s+(\w+)\s*=/g)) {
      if (GENERIC_NAMES.has(m[1].toLowerCase()))
        issues.push({ name: m[1], type: 'generic-name', line: i + 1 });
    }
    // 匈牙利命名
    for (const m of line.matchAll(/\b(?:str|int|bool|arr)[A-Z]\w*/g)) {
      issues.push({ name: m[0], type: 'hungarian', line: i + 1 });
    }
    // 过度缩写
    for (const m of line.matchAll(/\b(?:usr|prd|cfg|cnt|idx)\b/g)) {
      issues.push({ name: m[0], type: 'over-abbreviated', line: i + 1 });
    }
  });
  return { issues, ok: issues.length === 0 };
}
```
