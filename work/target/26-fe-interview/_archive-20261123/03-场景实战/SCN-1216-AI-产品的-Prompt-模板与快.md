---
title: [SCN-1216] AI 产品的 Prompt 模板与快捷指令
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1216：AI 产品的 Prompt 模板与快捷指令

**答**：
- 模板：预设 Prompt 模板（分类：写作/编程/分析），变量占位（{主题}）填充。
- 快捷：斜杠命令（/翻译）+ 快捷指令面板（一键填入）。
- 沉淀：用户自定义模板保存（个人模板库）。

```javascript
// Prompt 模板
function applyTemplate(tpl, vars) {
  return tpl.replace(/\{(\w+)\}/g, (m, k) =>
    vars[k] != null ? vars[k] : `{${k}:未填}`);
}
const TEMPLATES = {
  translate: '将以下内容翻译成{语言}：\n{内容}',
  code: '用{语言}实现：{需求}，要求包含错误处理',
};
// 快捷指令：输入 / 稳出面板，选择后填充模板
```
