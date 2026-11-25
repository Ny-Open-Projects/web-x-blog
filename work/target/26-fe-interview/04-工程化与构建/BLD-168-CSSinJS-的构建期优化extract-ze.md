---
title: [BLD-168] CSS-in-JS 的构建期优化：extract、zero-runtime 与运行时方案的对比。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-168：CSS-in-JS 的构建期优化：extract、zero-runtime 与运行时方案的对比。
**答**：
- 三代方案：**运行时**（styled-components/emotion，构建期几乎不优化，产物含 runtime ~10KB + 首帧样式注入）；**构建期 extract**（babel 插件把样式抽成 .css 文件 + 类名，保留 DX 去 runtime 成本）；**zero-runtime**（linaria/pandaCSS/vanilla-extract，编译期完成，产物即 CSS，无运行时）。
- extract 关键机制：babel plugin 在 transform 阶段把 `css`/`styled` 调用**静态求值**为类名与样式字符串，写入虚拟 css 模块；动态值（props 驱动）只能降级 CSS 变量传递——"动态样式走 CSS 变量"是所有编译方案的设计核心。
- 选型维度：设计 token 体系（panda/vanilla-extract 强）、组件库形态（需 SSR/CDN 直出 CSS）、DevTools 体验、与现有 tailwind 的共存。
- 迁移 ROI：从运行时方案迁 zero-runtime 的收益点 = 首屏 JS -10~15KB、无样式闪烁（FOUC? 提取后预载）、SSR 无需样式收集。

```javascript
// babel.config.js：@linaria 的构建期提取（zero-runtime 代表）
module.exports = {
  presets: [
    ['@babel/preset-react'],
    ['@babel/preset-typescript'],
    // linaria 的 extractor 必须排在 esbuild/转译之后、且要看到完整语法
    ['@linaria/babel-preset', {
      sourceMap: process.env.NODE_ENV !== 'production',
      displayName: process.env.NODE_ENV !== 'production',   // dev 下类名带组件名，便于调试
      evaluate: true,      // 静态求值 styled 内的模板表达式（零运行时的关键开关）
    }],
  ],
};
// 源码：
// const Title = styled.h1`color: var(--brand); font-size: ${props => props.size}px;`
// 产物：
// index.css:   .Title__t1z9k { color: var(--brand); font-size: var(--title-size); }
// index.js:    const Title = "Title__t1z9k";   ← 组件运行时只是一个类名字符串
//              动态值： <h1 style={{ '--title-size': size + 'px' }} class="Title__t1z9k">
// 对比 styled-components：产物含 runtime + 逐帧 injectStyle 调用；linaria 产物 = 纯 CSS
```

## 追问（补充）

**追问**：

1. zero-runtime 真的零运行时吗？ → 编译期把样式抽成静态 CSS 与类名，运行时只剩拼接 class 字符串；props 派生的动态样式只能降级成内联样式或 CSS 变量，能力上有取舍。
2. extract 失败的常见原因？ → 样式写在动态模板字符串里、跨文件变量无法静态求值、条件分支里的样式对象，都会被判定为不可抽取而回落到运行时注入。
3. 怎么验证抽取正确？ → SSR 输出的 class 与产物 CSS 做一一比对，再叠加视觉回归和首屏 CSS 体积前后对比，确认没有漏样式或重复注入。
