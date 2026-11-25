---
title: [RBL-630] 原子 CSS 的构建期处理：扫描提取、变体展开与产物去重
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-630：原子 CSS 的构建期处理：扫描提取、变体展开与产物去重

**答**:
- Tailwind/UnoCSS 类工具的构建管线：1) **内容扫描**（正则提取候选类名：jsx/html/md/模板字符串里的 class 属性）；2) **解析与变体展开**（hover: 前缀生成伪类包装、responsive: 前缀生成媒体查询包装、dark: 生成祖先选择器）；3) **规则解析**（类名 → 原子规则：`text-red-500` → `color: #ef4444`，主题 token 参与）；4) **产物生成与去重**（同类名只产一条规则；文件内与跨文件去重）。
- 与打包器集成的关键点：扫描依赖**模块图**（只扫被引用的内容文件，而非全仓库 glob——大仓库 glob 全扫是 UnoCSS 性能痛点；集成进构建器后 transform 钩子里按模块提取，天然增量）。
- 增量失效模型：类名产物的失效键是「内容文件中出现的类名集合」——文件改动后集合 diff（新增类名 → 追加规则；删除 → 引用计数归零才删）。HMR 下未变化类名对应的规则不重生成，样式表 patch 更新。
- 产物形态决策：dev 下全量生成（懒按需更复杂）或按需生成（vite 插件模式）——prod 必须全量收敛（避免运行时缺口）；排序问题：原子 CSS 的规则顺序决定优先级（覆盖），生成顺序必须稳定（字典序或声明序），否则同权重规则互相覆盖产生随机行为。
- 追问钩子：为什么原子 CSS 天然适合「去重 + 长缓存」？——页面变化通常只增删类名，未变类名的 CSS 规则不变 → 拆出「原子规则层 + 页面使用清单」两层后，规则层可长缓存；这与 RBL-598 级联 hash 的「变更频率分组」同构。

```javascript
// 构建器内嵌的原子 CSS 提取（transform 钩子视角）
function extractClassNames(code) {
  const RE = /class(?:Name)?=["'`{]([^"'`}]+)["'`}]/g;
  const found = new Set();
  let m;
  while ((m = RE.exec(code)))
    m[1].split(/\s+/).forEach(c => c && found.add(c));   // 模板字符串里的 ${} 需剥离
  return [...found];
}

// 变体展开
function expandVariant(cls, theme) {
  const parts = cls.split(':');
  const base = parts.pop();
  const variants = parts;                                 // ['hover', 'md']
  let rule = resolveBase(base, theme);                    // text-red-500 -> color: #ef4444
  if (!rule) return null;                                 // 未知类名跳过
  for (const v of variants.reverse())                     // 内层先包装
    rule = wrapVariant(v, rule);                          // hover -> &:hover{...}; md -> @media{...}
  return { key: cls, css: rule };
}
const wrapVariant = (v, css) =>
  v === 'hover' ? `&:hover { ${css} }`
  : v === 'dark' ? `.dark & { ${css} }`
  : /^md|sm|lg$/.test(v) ? `@media (min-width: ${bp(v)}) { ${css} }` : css;
```
