---
title: [ENG-077] .editorconfig 解决什么问题？和 Prettier 是什么关系？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-077：.editorconfig 解决什么问题？和 Prettier 是什么关系？
**答**：
- editorconfig 是编辑器层面的基础约定（缩进、换行符、字符集、末尾换行），VSCode/JetBrains 原生支持。
- 它解决"打开文件那一刻"的一致性：Prettier 只在保存/CI 时格式化，editorconfig 让编辑器行为先对齐。
- 层级继承：root = true 标记根目录，子目录可再放 .editorconfig 覆盖特定文件类型。
- 注意保持与 Prettier 配置一致（indent_size=2 对应 printWidth 之外的缩进约定），避免互相打架。

```ini
# .editorconfig
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
indent_style = space
indent_size = 2
trim_trailing_whitespace = true

[*.md]
trim_trailing_whitespace = false

[*.{yml,yaml}]
indent_size = 2
```
