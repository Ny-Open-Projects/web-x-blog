---
title: [1021] 注入攻击的多语言/编码变体怎么系统性防御
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 注入]
type: 面试题
---

## 1021：注入攻击的多语言/编码变体怎么系统性防御

**答**：
- 变体家族：编码类（Base64/URL/HTML 实体/Unicode 同形字）、语言类（小语种指令模型更易「忘记」约束）、拆分类（指令拆成多个无害片段，靠上下文拼起来生效）、翻译类（让模型自己翻译出指令）。
- 系统性防御不在「枚举变体」而在「改变执行前提」：无论内容怎么变，只要「工具权限与内容来源联动」的架构防线在，注入成功也做不了坏事——内容侧检测只是纵深一层。
- 检测侧实务：归一化管线（解码 → 同形字还原 → 分词）后再过检测器；多语言用例进回归集（至少覆盖攻防常用 5 种语言）。
- 追问钩子：为什么同形字（сyrillic а 混进 latin）危险？——绕过关键词检测且人眼不可见，归一化时按 Unicode 折叠表还原。

```ts
function normalize(text) {
  return text
    .replace(/[\u200B-\u200F\u202A-\u202E]/g, '')
    .normalize('NFKC')                          // 全角/兼容字符折叠
    .replace(/[\u0400-\u04FF]/g, c => HOMOGLYPH_MAP[c] || c); // 同形字还原
}
async function guard(raw) {
  const norm = normalize(raw);
  const decoded = tryDecodeAll(norm);          // Base64/URL 解码候选
  const verdict = await Promise.all([norm, ...decoded].map(detector.scan));
  return verdict.some(v => v.risky) ? block(norm) : pass(norm);
}
```
