---
title: [V3-463] SFC descriptor 拆分：单文件组件如何被多编译器协作处理
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 编译器]
type: 面试题
---

## V3-463：SFC descriptor 拆分：单文件组件如何被多编译器协作处理

**答**：
- parse 阶段产出 descriptor：`{ template, script, scriptSetup, styles[], customBlocks[] }`——各块带独立 loc，块内内容不解析（交给各自编译器）
- 请求拆分（Vite）：同一 .vue 文件被多次请求——`?vue&type=template`/`&type=script`/`&type=style&index=0&lang.css` 各块独立编译模块——HMR 只更新变更块
- script 与 scriptSetup 共存：编译器合成「默认导出 + setup 内容」——scriptSetup 顶层变量自动暴露给模板的机制是「编译期作用域分析」而不是运行时
- custom blocks：`<i18n>`/`<docs>` 等自定义块由插件处理——compileToDescriptor 的开放设计让生态扩展（Vite 插件消费 custom block 生成虚拟模块）
- sourcemap 链：template/script/style 三条独立 sourcemap 在 Vite 里合并回 .vue——调试断点能落回源文件的原因

```text
App.vue
  ├─ ?vue&type=template&index=0 → compileTemplate(descriptor.template)
  ├─ ?vue&type=script&setup=true → compileScript(descriptor)
  ├─ ?vue&type=style&index=0&scoped=xxx → compileStyle (scoped id 注入)
  └─ custom blocks → 插件虚拟模块
```
