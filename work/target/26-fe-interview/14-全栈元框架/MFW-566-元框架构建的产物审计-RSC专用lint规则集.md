---
title: [MFW-566] 元框架构建审计：RSC 专用 lint 规则集
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-566：RSC 专用 lint 规则集

**答**:
- RSC 专属 lint（eslint-plugin-react-compiler/next 核心）：1) **边界规则**：server 组件禁 hooks/事件 handler、client 组件禁 async（组件必须是同步渲染——async 用 Suspense 子组件）；2) **序列化规则**：server→client props 不可序列化类型检测（RBL-502 的静态版）；3) **数据规则**：fetch 无缓存选项的显式性（「每个 fetch 声明缓存策略」lint——默认语义太隐晦 RBL-526 陷阱清单的 lint 化）；4) 水合规则（Date.now/随机数直接渲染——RBL-915 的 lint 化）。
- lint 的分级：error（编译失败：边界违规）/warn（陷阱提示：隐式缓存）——lint 与构建器的重叠（Next 编译器部分检查 + ESLint 补全——两层防线）。
- 自定义规则的工程：规则即 fixture 测试（valid/invalid 用例对——RBL-585 fixture 模式的 lint 版）；规则集随框架版本演进（Next 15 语义变化 → 规则更新）。
- 追问钩子：为什么「fetch 缓存策略显式化」值得一条 lint？——Next 的 fetch 默认语义多版本变更过（13 默认缓存 → 15 默认不缓存）——「默认值漂移」让存量代码行为随升级翻转（RBL-953 默认值纪律的风险案例）；显式声明 = 升级免疫（意图写在代码里而非依赖默认值）——默认值漂移的防御：显式化 + codemod（RBL-941）。

```javascript
// 自定义 RSC lint 规则（eslint 插件骨架）
export const rules = {
  'require-fetch-cache': {
    meta: { schema: [], messages: { explicit: 'fetch 必须显式声明缓存策略（cache/next.revalidate）' } },
    create(context) {
      return {
        CallExpression(node) {
          if (node.callee.name !== 'fetch') return;
          const hasStrategy = node.arguments[1]?.properties?.some(
            (p) => ['cache', 'revalidate', 'tags', 'next'].includes(p.key?.name ?? p.key?.value));
          if (!hasStrategy)
            context.report({ node, messageId: 'explicit' });
        },
      };
    },
  },
  'no-async-client-component': { /* client 组件禁 async */ },
  'no-unserializable-props': { /* server→client props 类型白名单 RBL-502 */ },
  'no-hydration-time': { /* Date.now/Math.random 直接渲染 RBL-915 */ },
};
// fixture 测试（valid/invalid 对）
// tests/require-fetch-cache/invalid.tsx: fetch(url)           → error
// tests/require-fetch-cache/valid.tsx: fetch(url, { next: { revalidate: 60 } }) → 无
```
