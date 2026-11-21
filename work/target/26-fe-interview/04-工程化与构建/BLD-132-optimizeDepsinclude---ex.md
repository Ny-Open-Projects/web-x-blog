---
title: [BLD-132] optimizeDeps.include / exclude 与 force 的正确用法与常见误区。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-132：optimizeDeps.include / exclude 与 force 的正确用法与常见误区。
**答**：
- `include`：静态扫描发现不了的依赖要手动补——**动态拼接 import**（`import(`./langs/${l}.js`)` 里的第三方依赖）、条形按需组件库（vant/element-plus 虽有 esm 但被动态引用）、被 worker/ssr 间接使用。
- `exclude`：不预构建的依赖——需要源码形态（如想热更的内部包用源码 alias）、与预构建产物冲突的双实例包；但 exclude 的包若 import 了另一个裸依赖，浏览器将直接请求它并 404，必须连其依赖一起 exclude 或恢复 include（**exclude 传染性问题**，高频坑）。
- `force: true` / `--force`：忽略缓存重建 deps，用于"改了 lockfile 但 hash 没变的诡异场景"、调试 interop 问题；`optimizeDeps.esbuildOptions.plugins` 可深度干预预构建。
- 误区：把 include 当"提前加载性能优化"大量堆积（预构建产物变大、首启动变慢）；正确认知是"扫描器的兜底补丁"。

```javascript
// vite.config.ts：optimizeDeps 的生产级用法
export default defineConfig({
  resolve: {
    alias: { '@shared': fileURLToPath(new URL('./packages/shared/src', import.meta.url)) },
  },
  optimizeDeps: {
    include: [
      'lodash-es',                        // 仅被动态模板 import 使用，扫描不到 → include
      'dayjs/locale/zh-cn',
      'element-plus > @element-plus/icons-vue', // 子依赖语法：连带预构建其内部裸依赖
    ],
    exclude: [
      // 链接本地包且想实时热更时（配合 alias 到源码）；注意它依赖的裸包要一并处理
      'my-local-ui-lib',
    ],
    // exclude 传染性示例：my-local-ui-lib import 'clsx'
    //   → 浏览器直接请求 '/node_modules/clsx/...' 404
    //   → 解决：把 clsx 也 exclude（让浏览器能直接解析），或干脆不 exclude 该库
    esbuildOptions: { target: 'es2020' },
  },
  server: {
    // 误区纠正：发现新依赖自动 reload 是正常兜底，生产排查用 --debug optimizeDeps
  },
});
// CLI：vite --force     一次性强制重建
//      vite optimize    独立跑预构建（CI 预热常用）
```
