---
title: [RBL-037] 笔试：手写 DefinePlugin 简化版（编译期常量注入）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-037：笔试：手写 DefinePlugin 简化版（编译期常量注入）
**题目**：实现一个 Rspack plugin，在 emit 前对所有 JS 产物做常量替换：1) 输入 { '__BUILD_TIME__': Date, '__APP_NAME__': String } 形式的映射；2) 字符串常量在产物中以字面量替换；3) 只处理 .js 文件；4) 构建启动时打印将注入的常量清单；5) 说明真实 DefinePlugin 应在模块层而非产物层替换的原因。

```javascript
class MiniDefinePlugin {
  constructor(defines) { this.defines = defines; }
  apply(compiler) {
    const entries = Object.entries(this.defines);
    console.log('[MiniDefine] 注入常量:', entries.map(([k]) => k).join(', '));
    compiler.hooks.emit.tap('MiniDefinePlugin', (compilation) => {
      for (const [name, asset] of Object.entries(compilation.assets)) {
        if (!name.endsWith('.js')) continue;
        let src = asset.source().toString();
        for (const [key, value] of entries) {
          // 字符串值替换为 JSON 字面量；Date 等对象同样序列化
          const literal = typeof value === 'string' ? JSON.stringify(value) : String(value);
          // \b 边界避免替换标识符的子串（如 __APP_NAME__x）
          src = src.replace(new RegExp(`\\b${key}\\b`, 'g'), literal);
        }
        compilation.updateAsset(name, { source: () => src, size: () => src.length });
      }
    });
  }
}
module.exports = MiniDefinePlugin;
```
**评分点**：
- 用 \b 词边界防止子串误替换（正确性关键）。
- 字符串常量 JSON.stringify 成合法 JS 字面量。
- 钩子选 emit 并用 updateAsset 改产物（API 正确）。
- 能说出产物层替换的缺陷：无法被 tree shaking/DCE 感知、死分支残留体积（真实方案在 AST 层注入，未引用分支可被压缩器摇掉）。
