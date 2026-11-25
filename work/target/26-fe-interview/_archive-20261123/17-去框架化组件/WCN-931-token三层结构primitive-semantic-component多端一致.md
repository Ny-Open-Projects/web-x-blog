---
title: [WCN-931] token 三层结构（primitive / semantic / component）怎么在多端保持一致
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-931：token 三层结构（primitive / semantic / component）怎么在多端保持一致

**答**：
- 结论先行：多端一致的前提是「单一数据源 + 分层语义」——primitive 存原始色板/间距，semantic 存语义别名（color.text.primary），component 存组件级别名，各端只消费同一份 JSON。
- 解析规则统一：引用（`{color.blue.500}`）由编译器在构建期展开成各端原生格式（CSS var / iOS Asset / Android resource / 小程序 wxss），禁止端上自行再映射。
- 命名约束：命名不含平台信息（不写 px/dp），单位换算交给编译层——同一 `spacing.4` 在 Web=16px、iOS=16pt、Android=16dp、小程序=32rpx。
- 一致性校验：CI 跑「四端产物快照对比」，semantic token 缺失任一端构建即失败（设计系统中台多端发版红线）。
- 追问钩子：面试官问「某端想特殊定制怎么办」——答：走 override 层且必须声明差异原因，纳入护栏审计，不允许直接改源 token。

```javascript
// 统一 token JSON（单一数据源）
const tokens = {
  primitive: { blue500: '#1677ff', gray900: '#1f1f1f' },
  semantic: { 'color.text.primary': '{gray900}', 'color.link': '{blue500}' },
  component: { 'button.bg': '{color.link}' },
};
// 编译期解析引用 → 扁平 CSS 变量
function resolve(ref, seen = new Set()) {
  if (seen.has(ref)) throw new Error('循环引用: ' + ref);
  seen.add(ref);
  const v = tokens.semantic[ref] || tokens.component[ref] || tokens.primitive[ref];
  return v.startsWith('{') ? resolve(v.slice(1, -1), seen) : v;
}
console.log(resolve('button.bg')); // #1677ff（各端共用同一结果）
```
