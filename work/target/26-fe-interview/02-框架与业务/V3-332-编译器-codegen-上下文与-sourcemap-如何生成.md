---
title: [V3-332] 编译器的 codegen 上下文与 sourcemap 是怎么生成的？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-332：编译器的 codegen 上下文与 sourcemap 是怎么生成的？
**答**：
- CodegenContext 维护：代码字符串缓冲、缩进层级、helper 集合（去重登记）、变量前缀（`_ctx.` / `_setup.`）、组件与指令的注册表。
- push 系列 API（push/indent/newline/deindent）逐段拼接，每个模板节点生成代码时记录「输出位置 ↔ 模板 loc」映射。
- 生成完成后用 magic-string 把位置映射转成 source map，浏览器调试模板时能断点到原始 template 行。
- `prefixIdentifiers` 阶段把模板里的裸标识符绑定到正确的来源（setup 变量、props、ctx），这是表达式能独立运行的前提。
- 工程价值：排查「模板报错定位错行」时，直接检查 sourcemap 是否被二次构建工具破坏。
