---
title: [RBL-535] CSS 的打包管线：提取、合并与 CSS Modules 的局部作用域
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-535：CSS 的打包管线：提取、合并与 CSS Modules 的局部作用域

**答**:
- CSS 在打包器里的特殊处理：
- 1) **提取模式**（extract）：CSS 拼成独立 .css 文件（生产默认）——顺序敏感（同选择器后写覆盖先写）→ chunk 边界与 CSS 顺序的冲突是经典 bug（异步 chunk 的 CSS 注入顺序不可控）。
- 2) **内联模式**（dev）：CSS 以 JS 模块形式注入 `<style>`（HMR 友好）——dev 用内联、build 用提取是标准切换。
- 3) **CSS Modules 局部作用域**：类名 → `filename__class__hash` 的映射（编译期替换 + 导出映射表供 JS 引用）——局部作用域的 hash 要稳定（跨构建一致：内容 hash 而非随机）。
- 4) **CSS 的依赖图**：@import/@use/@url() 的资源解析——CSS 也要进模块图（作为特殊模块类型）；url() 引用的图片是资源模块（hash 命名）。
- CSS 顺序问题的工程解法：**CSS 按「模块图后序」拼接**（与 JS 执行序一致）+ 显式分层（@layer 原生解决优先级）——`@layer` 是 CSS 顺序问题的语言级解法（RBL-522 的顺序敏感根治）。
- 追问钩子：CSS 提取的「重复样式合并」——多个 chunk 引用同一 CSS 模块 → 提取到 shared chunk 或复制进各 chunk（体积 vs 请求取舍）——与 JS chunk 分配算法同构（RBL-521）。

```javascript
// CSS 打包管线
const CSS_PIPELINE = {
  提取模式: '生产：拼独立 .css——顺序敏感（异步 chunk 注入顺序不可控 = 经典 bug）',
  内联模式: 'dev：JS 模块注入 <style>（HMR 友好）——dev 内联/build 提取标准切换',
  CSSModules: {
    transform: '类名 → filename__class__hash（编译期替换 + 导出映射表）',
    hash要求: '内容 hash 跨构建稳定（非随机）',
  },
  依赖图: 'CSS 也是模块（@import/@use/@url()）——url 图片为资源模块 hash 命名',
  顺序解法: '按模块图后序拼接（与 JS 执行序一致）+ @layer 原生分层（语言级根治）',
  合并取舍: '多 chunk 共享 CSS → shared chunk 或复制——体积 vs 请求（RBL-521 同构）',
}
```
