---
title: [WCN-778] 设计系统组件的 props API 如何做 TypeScript 类型自动生成与发布？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-778：设计系统组件的 props API 如何做 TypeScript 类型自动生成与发布？

**答**：
- 结论：以组件运行时定义（props 声明/自定义元素 manifest）为单一数据源，用脚本生成 `.d.ts`（含属性类型、事件、slots），随包发布；类型与实现同源避免漂移。
- 用 ts-morph/TypeScript Compiler API 生成声明文件；CI 校验「类型声明能否覆盖所有公开 API」；为 WC 生成 JSX IntrinsicElements 扩展，获得 JSX 类型提示。
- 追问钩子：运行时 prop 校验（如 validator）与 TS 类型不一致怎么办？考察「以一处为准 + 一致性测试」。

```javascript
// 从组件元数据生成 d.ts（片段）
const meta = { tag: 'ds-button', props: { size: "'sm'|'lg'", disabled: 'boolean' } };
function genDts(m) {
  const props = Object.entries(m.props).map(([k, t]) => `  ${k}?: ${t};`).join('\n');
  return `declare global {
  namespace JSX {
    interface IntrinsicElements {
      '${m.tag}': { ${props.replace(/^  /gm, '')} } & React.HTMLAttributes<HTMLElement>;
    }
  }
}`;
}
console.log(genDts(meta));
```
