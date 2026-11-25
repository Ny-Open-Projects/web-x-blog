---
title: [AIC-990] 遗留模块既没文档又没测试，直接让 AI 迁移等于「蒙眼开车」，如何先帮 AI「补上眼睛」？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-990：遗留模块既没文档又没测试，直接让 AI 迁移等于「蒙眼开车」，如何先帮 AI「补上眼睛」？
**答**：
- 第一步是「观察与刻画」而非改写：先为遗留代码补特征化测试（记录当前真实行为，包括怪异行为）、生成结构/依赖地图、从代码与注释反推业务规则——结论：先让行为可见，再动手。
- 让 AI 做「代码考古」：阅读历史提交、commit message、相关文档，产出「这段代码可能在做什么」的假设清单，由人确认或纠正，形成可信赖的理解基线。
- 补测试要「锁现状」：特征化测试锁的是遗留代码当前行为（哪怕看起来是 bug），这样迁移后能验证等价；修正 bug 是另开任务，不在迁移中夹带。
- 追问钩子：能提出「在没有测试保障前，AI 迁移的输出一律视为『未经验证的草稿』，不得合并——先补眼睛意味着先把验证基础设施建起来」的候选人有扎实的迁移纪律。

```typescript
// 补眼睛：生成遗留模块理解基线
function buildBaseline(module) {
  return {
    structure: extractStructure(module.code), // 函数/依赖结构
    behaviors: module.inputs.map(i => ({ input:i, output:safeRun(module.run, i) })), // 特征化
    hypotheses: module.commits.map(c=>c.message), // 从提交历史反推意图
  };
}
function extractStructure(code){ return (code.match(/function\s+\w+/g)||[]); }
function safeRun(fn,input){ try{return JSON.stringify(fn(input));}catch(e){return 'ERR';} }
console.log(buildBaseline({
  code:'function f(){} function g(){}', inputs:[1,2],
  run:x=>x*2, commits:[{message:'修复价格四舍五入'}],
}));
```
