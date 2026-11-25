---
title: [MFW-080] Nuxt 的 auto-import 是什么原理，有什么代价和约束？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-080：Nuxt 的 auto-import 是什么原理，有什么代价和约束？
**答**：
- 原理：构建期（unimport 扫描）收集 Vue API、composables/、components/ 下的导出，代码里直接写 `useFetch`、`<ProductCard>` 时由**编译期注入 import 语句**——不是运行时全局变量，因此 tree-shaking 仍然有效，产物不含未用到的代码。
- 收益：少写样板 import；组件按目录语义命名（`app/components/base/Button.vue` → `<BaseButton>`）。
- 代价与约束：① 重名遮蔽难察觉（本地函数名与 auto-import 冲突）；② 「定义在哪」对新人不直观，IDE 跳转依赖类型生成（.nuxt/types）；③ 目录即 API——文件改名=公共接口变更，重构成本被放大。
- 生产建议：团队项目里 composables 用显式导出为主，auto-import 用于高频 Vue API 与公共 UI 组件；关闭对第三方库的 auto-import 以减小心智负担。

```vue
<script setup lang="ts">
// 不写 import { useFetch } from 'nuxt/app' —— 编译期自动注入
const { data } = await useFetch('/api/products');

// 显式风格（推荐用于业务 composables）：
// import { useCart } from '~/composables/useCart'
</script>
```

```ts
// nuxt.config.ts —— 收紧 auto-import 面
export default defineNuxtConfig({
  imports: {
    autoImport: true,
    scan: { dirs: ['composables'] }, // 限定扫描范围
  },
  components: {
    dirs: [
      { path: '~/components', pathPrefix: true }, // Base/Button.vue -> <BaseButton>
    ],
  },
});
```
