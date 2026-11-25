---
title: [RBL-697] 场景题：设计系统 token 管线与构建器的集成——主题产物化
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-697：场景题：设计系统 token 管线与构建器的集成——主题产物化

**答**:
- 设计 token（颜色/间距/字号 JSON）到产物的管线：token 源（JSON/YAML，单源）→ 构建期展开为多格式产物（CSS vars / TS 常量 / Tailwind config / 原生 App 配置）→ 与构建器集成方式 = 插件（虚拟模块 `virtual:tokens`，RBL-612）或独立构建步骤（token 变更频次低，独立构建 + 产物入仓亦可）。
- 主题运行时切换的构建配合：暗色/品牌多主题时，产物应为「CSS 变量分层」（`:root` 默认层 + `.dark` 覆盖层），切换 = 加 class 不重新加载——构建器把 token 编译成「变量层集合」而非「每主题一份完整 CSS」（重复体积大、切换慢）。
- token 校验进构建门禁：1) 命名规范 lint（`--color-bg-primary` 结构）；2) 引用完整性（`color.bg.primary` 引用的子 token 存在，防悬空引用）；3) 对比度审计（文本色 vs 背景色的 WCAG 对比度，暗色主题同样跑）——产物化让「设计质量」纳入 CI。
- token 变更的影响面：token JSON 变更 → 引用该 token 的模块失效（提取时记录 token 使用面，映射到模块）——影响面报告（「改这个主色会影响 N 个组件」）是设计/前端协作的沟通工具。
- 追问钩子：为什么 token 用「CSS 变量」而不是「编译期常量替换」？——变量支持运行时切换与继承覆盖；常量替换体积更小但失去动态性。折中：稳定 token（如间距）编译期常量、主题相关 token（颜色）CSS 变量——按「是否需要运行时切换」分层。

```javascript
// token 编译器（多格式产物 + 校验）
function compileTokens(tokens, themes) {
  const problems = [];
  const resolve = (ref, stack = []) => {
    if (typeof ref !== 'string' || !ref.startsWith('{')) return ref;
    const path = ref.slice(1, -1);
    if (stack.includes(path)) problems.push({ type: 'cycle', detail: path });
    const v = get(tokens, path);
    if (v === undefined) { problems.push({ type: 'missing-ref', detail: path }); return null; }
    return resolve(v, [...stack, path]);
  };
  const css = (theme) => `:root${theme === 'dark' ? '.dark' : ''} {\n` +
    Object.entries(tokens).map(([k, v]) => {
      const val = resolve(v);
      if (val === null) return '';
      if (theme === 'dark' && v.darkOverride) return `  --${k}: ${resolve(v.darkOverride)};`;
      return `  --${k}: ${val};`;
    }).filter(Boolean).join('\n') + '\n}';
  return { cssVars: ['light', 'dark'].map(css), tsConst: toTsConst(tokens), problems };
}
// 校验进 CI：problems 非空 fail；对比度审计独立跑（暗色主题同样校验）
```
