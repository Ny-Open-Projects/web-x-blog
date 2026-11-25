---
title: [BAS-194] EditorConfig 和 Prettier 冲突了怎么协调？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-194：EditorConfig 和 Prettier 冲突了怎么协调？
**答**：
- 定位不同：EditorConfig 跨编辑器管最基础的缩进/换行/字符集，对任何语言生效；Prettier 只管代码格式化且可配置项更多。
- 协调原则：同一件事只在一处声明——缩进、换行符、字符集交给 .editorconfig，Prettier 里删掉重复配置项，避免两处打架。
- Prettier 会读取 .editorconfig 作为未显式配置项的兜底，但 Prettier 自身配置优先级更高。

```ini
# .editorconfig：跨语言的底线配置
root = true

[*]
charset = utf-8
end_of_line = lf
indent_style = space
indent_size = 2
insert_final_newline = true
# 协调：Prettier 不再重复配 tabWidth/useTabs，避免两处不一致
```
