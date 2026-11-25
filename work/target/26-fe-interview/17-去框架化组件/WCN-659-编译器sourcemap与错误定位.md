---
title: [WCN-659] 模板编译出错时如何给出精准的行列定位（source map 与错误恢复）？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-659：模板编译出错时如何给出精准的行列定位（source map 与错误恢复）？

**答**：
- 结论：编译阶段维护「生成代码位置 ↔ 模板位置」的映射；解析出错时携带 offset 反查行列；用错误恢复（跳过非法片段）避免一处错误阻塞整个编译。
- 做法：lexer 记录每个 token 的 offset；parser 出错抛带 offset 的 CompileError；source map 用 VLQ 编码映射；IDE 场景用增量编译只重编改动部分。
- 追问钩子：为什么 IDE 要增量编译？全量编译无法满足输入时的实时反馈——考察对「编译产物服务于开发体验」的理解。

```javascript
class CompileError extends Error {
  constructor(message, template, offset) {
    const before = template.slice(0, offset);
    const line = before.split('\n').length;
    const col = offset - before.lastIndexOf('\n');
    super(`${message} @ ${line}:${col}`);
    this.offset = offset; this.line = line; this.col = col;
  }
}
function parseExpr(expr, offsetBase) {
  const m = expr.match(/[A-Za-z_$]\w*\(/);
  if (m && !['fn', 'call'].includes(m[0].slice(0, -1))) {
    throw new CompileError(`非法调用 ${m[0]}`, expr, offsetBase + m.index);
  }
  return expr;
}
try { parseExpr('foo(', 10); }
catch (e) { console.log(e.message); } // 带行列：精准定位
```
