---
title: [BLD-149] esbuild 的插件机制与限制：onResolve/onLoad 能做什么、为什么没有 AST？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-149：esbuild 的插件机制与限制：onResolve/onLoad 能做什么、为什么没有 AST？
**答**：
- 插件只有两个核心钩子：**onResolve**（接管路径解析：virtual module、alias、external 标记）与 **onLoad**（接管文件内容：返回 contents + loader 类型 js/ts/css/text）；构建期还有 onStart/onEnd 触发统计。
- **没有 transform 级 AST 钩子**（无类似 babel visitor 的口子），也不开放内部 AST——自定义语法转换只能 onLoad 里自己调 babel/swc/正则，这是 esbuild 插件生态远小于 rollup 的根本原因。
- 其他限制：不做语义级 tree-shaking 增强配置、不支持部分 loader 特性（如 less 要先转 css 再喂）、watch 增量语义与 webpack 不同（onEnd 才能拿到结果）。
- 价值与定位：写插件做"文件级"干预（资源内联、virtual env 模块、protobuf loader）依然高效；语义级需求就别用 esbuild 独立打包。

```javascript
// esbuild 插件：virtual 模块 + onLoad 转换（展示两个钩子的全部能力）
import * as esbuild from 'esbuild';

const envPlugin = {
  name: 'env-virtual',
  setup(build) {
    // ① onResolve：拦截 import 'env' → 虚拟模块
    build.onResolve({ filter: /^env$/ }, (args) => ({
      path: 'env',
      namespace: 'env-ns',            // namespace 隔离后续 onLoad 的 filter
    }));
    // ② onLoad：产虚拟内容（构建期注入，替代 DefinePlugin 的结构化版）
    build.onLoad({ filter: /.*/, namespace: 'env-ns' }, () => ({
      contents: `export const API_BASE = ${JSON.stringify(process.env.API_BASE ?? '')};`,
      loader: 'js',
    }));

    // ③ onLoad + 自定义 loader：yaml 直接进 bundle（无 AST 钩子的典型补偿手段）
    build.onLoad({ filter: /\.yaml$/ }, async (args) => {
      const text = await require('node:fs/promises').readFile(args.path, 'utf8');
      return { contents: `export default ${JSON.stringify(require('js-yaml').load(text))};`, loader: 'js' };
    });
  },
};

await esbuild.build({
  entryPoints: ['src/index.ts'],
  bundle: true, outfile: 'dist/index.js',
  plugins: [envPlugin],
  // ④ onEnd：拿结果统计（watch 模式下的增量回调点）
  plugins2: undefined,
});
// 限制小结：改不了 AST、没有 per-module render 钩子（rollup transform 的替代即 onLoad）；
// go 二进制并发处理，速度是 babel 的 10-100x，生态换性能就是这个交易。
```

## 追问（补充）

**追问**：

1. 为什么 esbuild 没提供 AST 插件？ → 它是 Go 侧多线程编译管线，插件只能在 onResolve/onLoad 里按文本和字节介入，没有节点级钩子；需要改语法树就串 babel 或 swc 做后处理。
2. onResolve 与 onLoad 的匹配顺序？ → 注册时可用 filter 与 namespace 限定，onResolve 按插件注册顺序尝试，第一个返回结果即终止；onLoad 按 resolve 结果的 namespace 加 path 匹配。
3. 插件能力的边界在哪？ → 能改解析路径、提供虚拟模块、转译内容；不能做依赖图完成后的跨模块分析，也没有 webpack 那套 emit 与 afterEmit 生命周期。
