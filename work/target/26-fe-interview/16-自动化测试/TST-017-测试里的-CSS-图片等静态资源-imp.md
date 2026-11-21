---
title: [TST-017] 组件测试里 import CSS / 图片报错怎么处理？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-017：组件测试里 import CSS / 图片报错怎么处理？
**答**：
- 根因：Node/jest-like 环境不认识 `.css/.png/.svg` 等非 JS 模块，import 直接抛错；Vitest 因为跑在 Vite 管线上，CSS/静态资源默认已按 Vite 方式处理，大部分情况开箱即用。
- 残留问题：CSS Modules 的类名 hash 在测试里是原始 key，断言类名时要小心；纯 CSS import 副作用可能想跳过。
- 方案：`test.css: { modules: { classNameStrategy: 'non-scoped' } }` 保持类名稳定；不关心样式的组件测试可用 `css: false`（默认）加速。
- 图片/字体：Vitest 交给 Vite 处理为 URL 字符串，若组件断言 src，注意 dev/测试下是 `/src/assets/x.png` 而非 hash 名。
- 追问钩子：从 Jest 迁移时常被 moduleNameMapper 处理静态资源的旧习惯误导，Vitest 下通常直接删掉这些映射。

```typescript
// vitest.config.ts
export default defineConfig({
  test: {
    css: false,                                  // 不解析 CSS，加快测试
    // css: { modules: { classNameStrategy: 'non-scoped' } } // 需要断言类名时
  },
});
// 组件里 import styles from './a.module.css';
// 测试里 getByClass(styles.btn) 在 non-scoped 下类名就是 'btn'。
```
