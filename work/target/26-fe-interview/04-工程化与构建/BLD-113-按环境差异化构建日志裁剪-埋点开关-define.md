---
title: [BLD-113] 按环境差异化构建：日志裁剪、埋点开关、define 全解怎么做？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-113：按环境差异化构建：日志裁剪、埋点开关、define 全解怎么做？
**答**：
- `DefinePlugin` 是**编译期文本替换**（构建期常量），配合 `TerserPlugin` 的死代码消除（DCE）实现日志裁剪：`if (__DEV__) {...}` 在 prod 下整块被删——替换值必须写成 JSON 字面量（`JSON.stringify(...)`），字符串要双引号。
- 埋点开关三档：编译期常量（`__TRACK__` 直接删代码）、运行时配置（`window.__APP_CONFIG__` 服务端注入）、混合（debug 模式编译保留 + 运行时 sampling 采样）——面试要说出"编译期开关改配置要重新构建"这一代价。
- 注意 `DefinePlugin` 替换的是**引用点**而非赋值：`process.env.NODE_ENV`、`import.meta.env` 同理；对 `Object.keys(process.env)` 这类动态访问无效，需要 `EnvironmentPlugin`/`NormalModuleReplacementPlugin` 辅助。
- 产物差异验证：`webpack-bundle-analyzer` 前后对比 + `git grep '__DEV__' dist` 应为 0（确认 DCE 生效）。

```javascript
// webpack.config.js：完整的环境差异化配置
const webpack = require('webpack');
const TerserPlugin = require('terser-webpack-plugin');

module.exports = (env, argv) => {
  const isProd = argv.mode === 'production';
  const appEnv = { LOG_LEVEL: 'error', TRACK_ENABLE: isProd, SENTRY_DSN: isProd ? 'https://k@o.example.com/1' : '' };

  return {
    plugins: [
      new webpack.DefinePlugin({
        __DEV__: !isProd,                                  // 标识符级替换（不用 stringify）
        'process.env.NODE_ENV': JSON.stringify(isProd ? 'production' : 'development'),
        // 每个值都要 JSON.stringify，否则字符串会变成变量引用
        'process.env.APP_ENV': JSON.stringify(appEnv),
        'import.meta.env.VITE_SENTRY_DSN': JSON.stringify(appEnv.SENTRY_DSN),
      }),
      new webpack.EnvironmentPlugin({ REGION: 'cn-north-1' }), // 有默认值的环境变量，等价 define 简写
    ],
    optimization: {
      minimizer: [
        new TerserPlugin({
          terserOptions: {
            compress: {
              drop_debugger: true,
              drop_console: isProd,            // 兜底裁掉 console（__DEV__ 块已删，双保险）
              pure_funcs: isProd ? ['console.log', 'trackDebug'] : [], // 无副作用函数调用直接删
            },
          },
        }),
      ],
    },
  };
};

// 源码写法（会被 DCE）：
// if (__DEV__) { console.log('[debug]', payload); trackDebug(payload); }  → prod 产物中整块消失
// __TRACK__ && tracker.send(event);                                      → prod 下仅剩 tracker.send
```
