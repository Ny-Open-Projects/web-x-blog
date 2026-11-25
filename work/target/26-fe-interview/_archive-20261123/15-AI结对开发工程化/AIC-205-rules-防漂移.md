---
title: [AIC-205] AI 产出经常无视团队规范（比如硬编码颜色、绕过 API 层直接 fetch），如何用 rules 系统性防漂移？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-205：AI 产出经常无视团队规范（比如硬编码颜色、绕过 API 层直接 fetch），如何用 rules 系统性防漂移？
**答**：
- 正面约束 + 负面清单都要写：只写「怎么做」不够，要列「禁止项」并给替代方案。
- 规则给范例：给一个符合规范的「黄金示例」比十条描述有效。
- rules 只能劝，不能强制：强制靠 lint + CI 门禁兜底，两者形成「软引导 + 硬门禁」闭环。
- 对高频违规项做专项规则收敛，违规率进周报追踪。

```javascript
// 软引导 + 硬门禁闭环
const ruleSoft = `
## 样式规范
- 禁止硬编码颜色，必须使用 design token：color.text.primary
- 禁止组件内直接 fetch，必须走 src/api 层封装
（黄金示例见 components/Button/Button.tsx）
`;
const gates = {
  'no-hardcode-color': /#[0-9a-fA-F]{3,8}\b/,          // eslint 自定义规则扫描
  'no-direct-fetch': /fetch\(['"`](?!\/api-proxy)/,     // 只允许经 api 层
};
// AI 产出 → lint 拦截 → 违规样本回流改写 rules（每周迭代）
r
```
