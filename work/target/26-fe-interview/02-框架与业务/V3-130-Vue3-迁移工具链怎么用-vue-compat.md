---
title: [V3-130] Vue3 迁移工具链怎么用（@vue/compat 与 gogocode）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-130：Vue3 迁移工具链怎么用（@vue/compat 与 gogocode）？
**答**：
- 策略：大项目不硬切，用 @vue/compat 兼容层按特性渐进迁移——MODE 2 下默认 Vue2 行为，再逐项关闭兼容开关。
- 迁移构建会列出所有未兼容点（filters、$on、$children 等），按清单逐个消灭后移除 compat。
- gogocode / vue-codemod 负责静态转换：批量把 filters、事件 API、slot 语法改写成 Vue3 写法，人工只处理遗留。
- globals 兼容层：把 Vue2 全局 API（Vue.use 等）映射到新 API，过渡期少改业务代码。

```typescript
// main.ts —— @vue/compat 渐进迁移
import { configureCompat, createApp } from "vue";
import App from "./App.vue";

// 1. 全局进入 compat 模式：默认按 Vue2 语义运行
configureCompat({
  MODE: 2,
  // 2. 逐项关闭：已按 Vue3 语义改造完成的特性单独列在这里
  COMPONENT_V_MODEL: false, // v-model 已改为 modelValue 协议
  RENDER_FUNCTION: false, // h 函数已改为 Vue3 签名
  GLOBAL_EXTEND: false,
});

const app = createApp(App);
app.mount("#app");

// 配套步骤：
// 1) package.json 把 vue 替换为 @vue/compat，webpack/vite 配置 alias
// 2) 控制台会逐条打印未兼容告警，按清单消灭
// 3) gogocode 批量静态转换（filters、事件总线、slot 语法）减少人工
// 4) 全部告警清零后 MODE 改 3 并移除 compat 依赖
```
