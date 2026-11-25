---
title: [RBL-665] webpack 配置到 Rspack 的自动翻译：规则映射、未覆盖项与人工清单
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-665：webpack 配置到 Rspack 的自动翻译：规则映射、未覆盖项与人工清单

**答**:
- 配置翻译器（codemod）的价值不是「自动完成迁移」而是「自动完成 80% + 精确列出剩余 20%」：机械可映射的（entry/output/resolve.alias/optimization 常用项）直接转换；有语义差异的（loader 选项、插件参数）转换 + 标注 TODO；完全不支持的进入「人工清单」（输出 markdown 供工程师处理）。
- 翻译规则库示例：babel-loader → builtin:swc-loader（babel 选项映射：presets @babel/preset-env → targets；@babel/plugin-transform-runtime → 声明 swc 的 externalHelpers）；terser-webpack-plugin → 内置 minifier；mini-css-extract-plugin → CssExtractRspackPlugin——每条规则 = 匹配条件 + 转换函数 + 置信度。
- 置信度分级是关键输出：high（直接换，行为等价）、medium（换了但需回归验证）、low（只提示不换）——迁移 PR 里 low/medium 项集中呈现，评审聚焦。
- 未覆盖项的处理哲学：宁可「少转换 + 明确提示」不可「错误转换」——翻译器输出「skipped 清单」（原配置片段 + 原因 + 建议），用户手动处理；静默丢弃是迁移事故主因（语义丢失无感知）。
- 追问钩子：为什么翻译器要保留原 webpack 配置做「对照测试」？——翻译正确性的唯一证据是「双配置构建产物语义一致」（RBL-649）；翻译器应该在输出里直接附带双版本对比脚本，让验证成为迁移 PR 的标准步骤。

```javascript
// 翻译规则库
const RULES = [
  {
    match: (c) => c.module?.rules?.some(r => r.use?.includes?.('babel-loader')),
    apply: (c) => {
      c.module.rules = c.module.rules.map(r =>
        r.use?.includes?.('babel-loader')
          ? { ...r, use: { loader: 'builtin:swc-loader', options: { jsc: { target: 'es2015' } } } }
          : r);
      return { confidence: 'medium', note: 'babel 选项需人工核对（preset/plugins 映射）' };
    },
  },
  {
    match: (c) => c.plugins?.some(p => p?.constructor?.name === 'DefinePlugin'),
    apply: (c) => ({ confidence: 'high', note: 'DefinePlugin 在 rspack 内置同名' }),
  },
];

function translateConfig(webpackConfig) {
  const out = structuredClone(webpackConfig);
  const report = { high: [], medium: [], low: [], skipped: [] };
  let matchedAny = false;
  for (const rule of RULES) {
    if (!rule.match(out)) continue;
    const r = rule.apply(out);
    report[r.confidence].push(r.note);
    matchedAny = true;
  }
  if (!matchedAny) report.low.push('无可映射规则——请人工评估');
  // 未覆盖检测：原生 webpack 插件仍在 plugins
  for (const p of out.plugins || [])
    if (p?.constructor?.name?.includes('Plugin') && !isRspackPlugin(p))
      report.skipped.push({ plugin: p.constructor.name, hint: '查 rspack 等价插件映射表' });
  return { config: out, report };
}
```
