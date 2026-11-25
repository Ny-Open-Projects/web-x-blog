---
title: [BLD-112] 多主题构建方案：编译期产出多份主题产物 vs 运行时 CSS 变量切换，怎么选与怎么实现？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-112：多主题构建方案：编译期产出多份主题产物 vs 运行时 CSS 变量切换，怎么选与怎么实现？
**答**：
- 编译期方案：把主题 token 写成多份 less variables 文件，循环 entry/theme 调 webpack 多编译器（`webpack([cfgA, cfgB])`），每主题一份 `theme.<name>.css` + JS 产物，产物相互独立、运行时零开销，适合主题少（≤4）且要严格设计走查。
- 运行时方案：less 侧把颜色抽成 `var(--brand-color)`（`modifyVars` 编译默认值），切换时 JS 改 `document.documentElement.style.setProperty('--brand-color', ...)`；构建只有一份产物，适合主题多、需用户自定义。
- 混合方案（生产主流）：基础样式编译期多主题，长尾组件用 CSS 变量；或用 `@ant-design/cssinjs`/`css-vars-ponyfill` 类方案按需生成。
- 决策点：主题数量、切换频率、是否需免闪白（编译期+link 预载最优）、包体积预算（编译期 N 份 = N 倍 CSS）。

```javascript
// 编译期多主题：多编译器配置（build-themes.js）
const webpack = require('webpack');
const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const themes = require('./themes.json'); // ["light", "dark", "brand-blue"]

function makeConfig(theme) {
  return {
    name: theme,
    entry: { index: './src/index.js' },
    output: { path: path.resolve(__dirname, `dist/${theme}`), filename: '[name].[contenthash].js' },
    module: {
      rules: [
        {
          test: /\.less$/,
          use: [
            MiniCssExtractPlugin.loader,
            'css-loader',
            {
              loader: 'less-loader',
              options: {
                lessOptions: {
                  modifyVars: require(`./src/themes/${theme}.less.vars.js`), // @brand-color: '#1677ff' 形式
                  javascriptEnabled: true,
                },
              },
            },
          ],
        },
      ],
    },
    plugins: [
      new MiniCssExtractPlugin({ filename: 'css/theme.css' }), // 每主题目录下独立产物
    ],
  };
}

webpack(themes.map(makeConfig), (err, stats) => {
  // stats 为数组：多编译器各自 stats，需逐个判断 hasErrors
  if (err) throw err;
  stats.forEach((s) => console.log(s.toString({ colors: true, chunks: false })));
});
// 运行时方案对照：less 里 token 全部写成 var(--brand-color, #1677ff)
// 切换：document.documentElement.style.setProperty('--brand-color', '#7c3aed')
```
