---
title: [RBL-275] 构建中的 Polyfill 策略与目标浏览器管理
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-275：构建中的 Polyfill 策略与目标浏览器管理

**答**:
- 单一事实源：browserslist（.browserslistrc）声明目标，转译（swc/oxc targets）与 polyfill（core-js 按需）都读它——多处声明必然漂移
- 按需 polyfill：usage 模式（按代码实际使用的 API 注入）优于全量引入；现代浏览器占比高时 modern build（无 polyfill）+ legacy build（nomodule）双产物
- 排查：产物 grep core-js 模块 id 统计注入了哪些 polyfill；体积异常时核对 browserslist 是否过宽（兼容到 IE 是体积黑洞）
- 治理：browserslist 变更走 RFC（影响面 = 全部产物），带体积影响评估

```text
.browserslistrc: ["chrome >= 87", "safari >= 14"]
modern/legacy 双构建：<script type="module"> + <script nomodule>
产物审计：grep "core-js/modules" dist/*.js | wc -l
```
