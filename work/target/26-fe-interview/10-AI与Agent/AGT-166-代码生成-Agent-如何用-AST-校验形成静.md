---
title: [AGT-166] 代码生成 Agent 如何用 AST 校验形成静态检查闭环？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-166：代码生成 Agent 如何用 AST 校验形成静态检查闭环？
**答**：
- 流程闭环：模型生成代码 → 解析为 AST（语法合法即拦截大半幻觉残缺）→ 规则校验（禁用 API、类型检查、复杂度阈值）→ 自动修复（把编译器错误信息回喂模型定向修）→ 修不好才降级人工。
- AST 检查比正则强在哪：正则查 `eval(` 会被字符串和注释绕过，AST 能按「节点类型 + 语义」匹配（CallExpression 的 callee 是全局 eval）；作用域内的未定义变量、隐式 any 也能检出。
- 语言生态选择：TS/JS 用 TypeScript Compiler API 或 Babel parser；生成代码的校验要在沙箱 worker 里跑，防恶意代码在构建机上执行副作用。
- 闭环度量：记录「生成→校验失败率→修复成功率」，修复 prompt 依据高频失败类型持续迭代，这个数据集还能反哺评测集。

```typescript
// 代码生成闭环：TS AST 解析 + 规则校验 + 错误回喂修复
import ts from 'typescript';

interface Rule { name: string; check: (sf: ts.SourceFile) => string | null; }

const rules: Rule[] = [
  {
    name: 'no-eval',
    check: (sf) => {
      let hit: string | null = null;
      sf.forEachChild(function visit(node) {
        if (ts.isCallExpression(node) && node.expression.getText(sf) === 'eval') hit = '禁止使用 eval';
        node.forEachChild(visit);
      });
      return hit;
    },
  },
  {
    name: 'no-network-in-sandbox',
    check: (sf) => {
      let hit: string | null = null;
      sf.forEachChild(function visit(node) {
        if (ts.isCallExpression(node) && node.expression.getText(sf).match(/^fetch$|^XMLHttpRequest$/))
          hit = '沙箱代码禁止网络请求';
        node.forEachChild(visit);
      });
      return hit;
    },
  },
];

export function parseAndCheck(code: string): { syntaxOk: boolean; diagnostics: string[] } {
  const sf = ts.createSourceFile('gen.ts', code, ts.ScriptTarget.ES2022, true);
  const diagnostics: string[] = [];
  // 语法诊断：解析错误直接收集（残缺代码在这一步被拦截）
  ts.forEachChild(sf, (n) => {
    if (ts.isSyntaxList?.(n)) return;
  });
  const diags = (sf as any).parseDiagnostics ?? [];
  for (const d of diags) diagnostics.push(`语法：${ts.flattenDiagnosticMessageText(d.messageText, ' ')}`);
  for (const r of rules) {
    const v = r.check(sf);
    if (v) diagnostics.push(`${r.name}：${v}`);
  }
  return { syntaxOk: diagnostics.every((d) => !d.startsWith('语法')), diagnostics };
}

export async function generateWithLoop(spec: string, call: (prompt: string) => Promise<string>, maxFix = 3): Promise<string> {
  let code = await call(`实现以下需求，输出纯 TS 代码：\n${spec}`);
  for (let i = 0; i < maxFix; i++) {
    const { diagnostics } = parseAndCheck(code);
    if (!diagnostics.length) return code;
    code = await call(`你的代码未通过静态检查：\n${diagnostics.join('\n')}\n原代码：\n${code}\n请修复后重新输出完整代码。`); // 定向回喂
  }
  throw new Error(`静态检查闭环未收敛，转人工：${parseAndCheck(code).diagnostics.join('; ')}`);
}
```
