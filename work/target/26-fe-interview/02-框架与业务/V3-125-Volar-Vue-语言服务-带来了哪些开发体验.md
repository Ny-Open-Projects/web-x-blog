---
title: [V3-125] Volar（Vue 语言服务）带来了哪些开发体验能力？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-125：Volar（Vue 语言服务）带来了哪些开发体验能力？
**答**：
- 把 SFC 的 template、script、style 当一个整体做类型检查：模板表达式报错、props 类型提示、插槽类型校验。
- strictTemplates 打开后模板里未声明的变量、错误的 prop 类型都会标红，把运行时问题前移到编辑器。
- vueCompilerOptions 声明编译目标与全局类型；tsconfig 的 moduleResolution 用 bundler 配合 Vite。
- 配套约定：纯类型文件用 .d.ts 增强模板全局组件，dts 生成文件纳入版本管理。

```typescript
// tsconfig.json —— Vue3 + Volar 推荐配置
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "bundler", // 配合 Vite 的解析策略
    "strict": true,
    "types": ["vite/client"], // 资源导入类型：import xxx from './a.png'
    "skipLibCheck": true
  },
  "include": ["src/**/*.ts", "src/**/*.vue"],
  "vueCompilerOptions": {
    "target": 3.4, // 编译目标版本，决定可用的宏与语法
    "strictTemplates": true // 模板表达式也走严格类型检查：未知变量、错误 prop 类型直接标红
  }
}
```
