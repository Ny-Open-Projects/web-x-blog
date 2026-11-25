---
title: [AIC-029] 如何防止 AI 幻觉出不存在的 API 或组件？「防幻觉验证」要落到流程的哪几步？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-029：如何防止 AI 幻觉出不存在的 API 或组件？「防幻觉验证」要落到流程的哪几步？
**答**：
- 幻觉根源：模型对「没见过」的私有库/新版本 API 按训练记忆补全。所以第一原则是**给事实**：贴 package.json 版本、贴目标库的类型声明（d.ts）、贴真实调用示例。
- 验证要落三步：① 生成后先跑 `tsc --noEmit`/lint，编译器是幻觉的第一道过滤网；② 对照 d.ts 校验用到的 API 是否存在；③ 人工只抽查关键调用点，不全读。
- prompt 里显式声明「以下列表是全部可用 API，禁止使用列表之外的方法」，并在约束里要求「不确定时输出 UNKNOWN 而不是编造」。
- 对高频幻觉点（公司内部 SDK、新框架版本）建「事实卡片」：版本 + 真实签名 + 一个例子，任务时随上下文注入。
- 追问钩子：可以自动做——生成后静态分析 import 是否存在于 node_modules，不存在直接打回重生成，这就是幻觉检查器的笔试原型。

```javascript
// 幻觉自动检测：校验 AI 代码里的 import 是否真实存在
function detectPhantomImports(generatedCode, fs) {
  const imports = [...generatedCode.matchAll(/(?:from|import)\s+['"]([^'"]+)['"]/g)]
    .map(m => m[1]).filter(p => !p.startsWith('.') && !p.startsWith('@/') && p !== 'react');
  const issues = imports.filter(name => {
    const base = name.startsWith('@') ? name.split('/').slice(0, 2).join('/') : name.split('/')[0];
    return !fs.existsSync(`node_modules/${base}`);
  });
  return { phantom: issues, action: issues.length ? 'REJECT_AND_REGENERATE' : 'PASS' };
}
```
