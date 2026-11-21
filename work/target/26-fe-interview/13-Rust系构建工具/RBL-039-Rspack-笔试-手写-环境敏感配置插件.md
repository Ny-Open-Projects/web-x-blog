---
title: [RBL-039] 笔试：手写「环境探测插件」——构建期校验必填环境变量
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-039：笔试：手写「环境探测插件」——构建期校验必填环境变量
**题目**：实现 EnvCheckPlugin：1) 构造时传入必填变量名数组与对应正则校验；2) compiler 钩子里在构建开始前校验 process.env；3) 缺失或格式不符时让构建失败并给出可读错误（指明变量名与期望格式）；4) 通过后注入 DefinePlugin 同款常量（避免两处配置）；5) 提供 strict 选项：非 strict 时只 warning 不失败。

```javascript
const rspack = require('@rspack/core');
class EnvCheckPlugin {
  constructor({ rules, strict = true }) { this.rules = rules; this.strict = strict; }
  apply(compiler) {
    compiler.hooks.run.tap('EnvCheckPlugin', () => {
      const errors = [];
      for (const [name, pattern] of this.rules) {
        const v = process.env[name];
        if (v === undefined || v === '') errors.push(`缺少必填环境变量: ${name}`);
        else if (pattern && !pattern.test(v))
          errors.push(`环境变量 ${name} 格式不符: 期望 ${pattern}，实际 "${v}"`);
      }
      if (errors.length) {
        if (this.strict) throw new Error(`[EnvCheck] 构建终止\n- ${errors.join('\n- ')}`);
        compiler.getInfrastructureLogger('EnvCheck').warn(errors.join('; '));
      }
    });
    // 校验通过后同源注入，避免两处配置漂移
    new rspack.DefinePlugin(Object.fromEntries(this.rules.map(([n]) =>
      [`process.env.${n}`, JSON.stringify(process.env[n] ?? null)]))).apply(compiler);
  }
}
module.exports = EnvCheckPlugin;
// 用法：new EnvCheckPlugin({ rules: [['API_BASE', /^https:\/\/.+$/]] })
```
**评分点**：
- 选 run 钩子（构建前 fail-fast，不浪费构建时间）。
- strict 双模式（错误可配置为 fail 或 warn）。
- 注入复用同一份 rules 数据源（避免配置漂移）。
- 错误信息含变量名与期望格式（可读性）。
- 未设置时注入 null 而不是 undefined 字面量（产物合法性）。
