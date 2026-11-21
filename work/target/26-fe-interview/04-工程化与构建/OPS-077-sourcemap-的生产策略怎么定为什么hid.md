---
title: [OPS-077] sourcemap 的生产策略怎么定？为什么"hidden"最合适？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-077：sourcemap 的生产策略怎么定？为什么"hidden"最合适？
**答**：
- 三个选择：normal（产物末尾带 sourceMappingURL 注释，map 随产物公开）、hidden（生成 map 但不写注释）、不生成（线上无法还原）。
- hidden 是生产标准：构建产出 .map 文件供上传监控平台，但浏览器/CDN 拿不到 map，兼顾可还原与安全。
- hidden 的配套动作：构建后立刻把 map 上传监控平台再从发布产物中剔除（或上传与部署分目录）。
- 注意与构建缓存配合：map 生成会拖慢构建，CI 里按需开关。

```javascript
// vite.config.js：hidden sourcemap 生产策略
import { defineConfig } from 'vite';

export default defineConfig(({ mode }) => ({
  build: {
    // production 生成 map 但不注入 sourceMappingURL 注释
    // 浏览器 DevTools 与 CDN 都看不到 map，只有拿到 .map 文件的监控平台能还原
    sourcemap: mode === 'production' ? 'hidden' : true,
    minify: 'esbuild',
    rollupOptions: {
      output: {
        // map 与产物同目录生成，CI 上传后剔除
        // dist/assets/app-abc123.js + dist/assets/app-abc123.js.map
      },
    },
  },
  esbuild: {
    // 保留函数名便于部分还原（可选权衡：微小体积代价换更好栈信息）
    keepNames: false,
  },
}));

// CI 流程约定（bash 注释示意）：
//   pnpm build
//   npx sentry-cli sourcemaps upload ...   # 先上传 map
//   find dist -name '*.map' -delete        # 再从部署产物剔除（见 OPS-082）
```
