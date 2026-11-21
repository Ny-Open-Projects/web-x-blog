---
title: [OPT-146] CSS 重复样式与原子类（Tailwind）产物膨胀如何治理？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-146：CSS 重复样式与原子类（Tailwind）产物膨胀如何治理？

**答**：
- 膨胀来源：①未 purge 的全量工具类（Tailwind 默认产物上百 KB）②重复的组件样式（多套皮肤/旧页面遗留）③深嵌套选择器编译出的长重复串。
- Tailwind 治理：v2 起开启 `content` 精确扫描源码，只保留用到的类，产物可从 4MB 降到 10~30KB；配合 `safelist` 白名单防动态拼接类被误删。
- 重复样式检测：`css-dedoupe` / PurgeCSS 报告 + PostCSS 自定义插件扫描重复声明；组织层面用 CSS 变量统一颜色/间距 token，减少魔法值。
- 体积进性能预算：CI 里给 CSS 单独设 size-limit 限额，超限报警。

```javascript
// 一一对应：Tailwind 精确 purge + 重复样式扫描脚本
// tailwind.config.js —— content 精确圈定，产物从 3.9MB 到 22KB
module.exports = {
  content: [
    './src/**/*.{js,jsx,ts,tsx,vue}',
    './index.html',
  ],
  safelist: [{ pattern: /^(bg|text)-(red|green)-(500|600)$/, greedy: true }], // 动态类兜底
  corePlugins: { float: false },  // 关掉不用的核心插件再省一点
};

// scripts/check-dup-css.mjs —— CI 重复声明扫描，超阈值 fail
import fs from 'node:fs';
import postcss from 'postcss';

const css = fs.readFileSync(process.argv[2], 'utf8');
const seen = new Map(); // "selector|decl" -> 首次出现位置
let dup = 0;

postcss.parse(css).walkRules(rule => {
  rule.walkDecls(decl => {
    const sig = `${rule.selector}|${decl.prop}:${decl.value}`;
    if (seen.has(sig)) { dup++; console.warn(`重复声明 ${sig}，首次见 line ${seen.get(sig)}`); }
    else seen.set(sig, rule.source?.start?.line ?? 0);
  });
});
const dupRatio = dup / seen.size;
console.log(`重复率 ${(dupRatio * 100).toFixed(1)}%（${dup}/${seen.size}）`);
if (dupRatio > 0.08) process.exit(1); // 超 8% 阻塞，进 CI
```
