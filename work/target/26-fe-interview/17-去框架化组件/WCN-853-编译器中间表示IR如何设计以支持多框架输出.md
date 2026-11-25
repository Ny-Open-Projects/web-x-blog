---
title: [WCN-853] 编译器中间表示（IR）如何设计以支持多框架输出？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-853：编译器中间表示（IR）如何设计以支持多框架输出？

**答**：
- 结论先行：IR 要「足够低层以脱离源语言特性，又足够保留语义以支撑优化与多后端」——主流选择是「带类型与响应式标记的树形 IR + 控制流/数据流信息」，类似简易 SSA 或带注解的 AST。
- 设计要素：① 节点类型精简（Expr/Stmt/Block/If/For/Call 等）；② 每个表达式标注「是否响应式」「依赖哪些信号」「是否静态可提升」；③ 保留作用域与类型信息供后端优化；④ 控制流用显式结构（If/For/Block）而非源语言糖，便于后端翻译。
- 多框架适配：不同后端读同一 IR——DOM 后端把「响应式表达式」编译成 `effect` 绑定，SSR 后端编译成字符串拼接并静态求值，Native 后端编译成对应模板指令；语义一致性由 IR 保证。
- 优化友好：IR 上做常量折叠、静态提升、死代码消除——与后端无关，一次优化所有目标受益。
- 权衡：IR 太抽象会丢失源语言信息（如精确 SourceMap），太具体则退化为「就不是 IR」——要在两者间取平衡，常见做法是分层 IR（HIR 高层保留语义 → LIR 低层贴近目标）。
- 追问钩子：面试官会问「响应式信息放 IR 还是后端分析」——答：放 IR（前端已做过依赖分析），避免每个后端重复分析，也保证语义一致。

```javascript
// 带响应式标记的树形 IR 示例
const ir = {
  kind: 'Block',
  children: [
    { kind: 'Static', op: 'createElement', tag: 'div' },
    { kind: 'Expr', op: 'bindText', deps: ['count'], expr: 'count * 2', reactive: true },
    { kind: 'If', cond: { deps: ['visible'], expr: 'visible' },
      then: { kind: 'Static', value: '展示' }, else: null },
  ],
};
// 多后端消费同一 IR
const backends = {
  dom: (n) => n.children.map(c => c.reactive ? `effect(()=>setText(${c.expr}))` : `emit(${c.op})`),
  ssr: (n) => n.children.map(c => c.reactive ? `\${${c.expr}}` : c.value || '').join(''),
};
console.log(backends.dom(ir));
console.log(backends.ssr(ir));
```
