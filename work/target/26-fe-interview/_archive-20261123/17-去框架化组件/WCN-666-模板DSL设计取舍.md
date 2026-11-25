---
title: [WCN-666] 设计团队模板 DSL 时，类 HTML（Vue 风格）与类 JSX（React 风格）如何取舍？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-666：设计团队模板 DSL 时，类 HTML（Vue 风格）与类 JSX（React 风格）如何取舍？

**答**：
- 结论：类 HTML 模板对设计师/低代码友好、编译优化信息更完整（静态可分析）；类 JSX 灵活、与 JS 生态无缝但静态分析更依赖约定。
- 维度：学习曲线、工具链（补全/高亮）、编译期可分析性、动态表达力、与设计系统 token 的结合。
- 追问钩子：为什么低代码平台偏爱类 HTML？因为非开发者能理解且可视化编辑器可结构化操作——考察对「受众决定 DSL」的判断。

```javascript
// 类 HTML 模板：静态可分析，适合编译优化
const htmlTpl = `<Button variant="primary">{{ label }}</Button>`;
// 类 JSX：灵活，动态表达力强
const jsxTpl = (props) => <Button variant={props.v}>{props.label}</Button>;
// 同一设计系统组件，两种 DSL 都能消费
const DSL = {
  html: { analyzable: true, designerFriendly: true },
  jsx:  { analyzable: 'partial', jsFriendly: true },
};
console.log(DSL.html.analyzable ? 'HTML 模板利于编译期优化' : '');
```
