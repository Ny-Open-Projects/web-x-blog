---
title: [V3-124] unplugin 系列生态有哪些常用插件？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-124：unplugin 系列生态有哪些常用插件？
**答**：
- unplugin-auto-import：vue/vue-router/pinia 的 API 免手写 import，同时生成 dts 供 TS 识别。
- unplugin-vue-components：模板组件免 import，配合 resolver 实现组件库样式按需加载。
- @intlify/unplugin-vue-i18n：i18n 资源预编译进产物，运行时更小更快。
- 三者共同点：基于统一的 unplugin 接口，同一份插件代码可跑在 Vite/Webpack/Rollup 上。

```typescript
// vite.config.ts —— unplugin 三件套
import { defineConfig } from "vite";
import AutoImport from "unplugin-auto-import/vite";
import Components from "unplugin-vue-components/vite";
import VueI18nPlugin from "@intlify/unplugin-vue-i18n/vite";
import { ElementPlusResolver } from "unplugin-vue-components/resolvers";

export default defineConfig({
  plugins: [
    AutoImport({
      imports: ["vue", "vue-router", "pinia"], // ref/computed/useRouter 等免手写 import
      dts: "types/auto-imports.d.ts", // 生成类型声明，TS 不报错
      eslintrc: { enabled: true }, // 同步生成 ESLint 全局变量配置
    }),
    Components({
      resolvers: [ElementPlusResolver()], // 组件库按需：组件 + 样式一起引入
      dts: "types/components.d.ts", // 让模板里的 <ElButton /> 获得类型
    }),
    VueI18nPlugin({
      include: [/locales/], // i18n 资源预编译，运行时体积更小
    }),
  ],
});
```
