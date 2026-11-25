---
title: [MFW-634] LLM 生成 UI 的产物管线：AI 组件的 RSC 集成
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-634：LLM 生成 UI 的 RSC 集成

**答**:
- AI 生成 UI 的 RSC 形态（GenUI）：1) **LLM 输出结构化 UI 描述**（组件名 + props JSON——生成「组件引用」而非 HTML）；2) RSC 渲染：LLM 输出 → 组件注册表查找（RBL-809 SDUI 协议的 LLM 版：`{ component: 'ProductCard', props: {...} }` → <ProductCard {...props} />）；3) 安全边界：LLM 输出的组件必须在注册表白名单（防注入任意组件/props——schema 校验 RBL-809）。
- 生成流式与 RSC 流式叠加：LLM token 流 → JSON 增量解析（partial JSON——流式组件渲染：字段到达即渲染对应部分）；「流式 JSON 解析」（不完整 JSON 的容错解析——LLM 流式的标准工程）。
- 组件注册表的窄面：AI 可用的组件集 ⊆ 注册表（白名单 + props schema 校验——「LLM 可信但输出验证」RBL-942 的 UI 版）。
- 追问钩子：为什么「LLM 输出组件引用」比「LLM 输出 HTML」更安全且更一致？——HTML = 任意标记（XSS/样式破坏/无约束）；组件引用 = 白名单内的类型化组件（props schema 校验——注入面收敛到「合法组件 + 合法 props」）；且组件引用与设计系统一致（LLM 不懂设计系统——注册表兜底）；「LLM 输出的约束化」：生成自由度收敛到「组合的自由」而非「标记的自由」——与 RBL-942 幻觉依赖防线同构：验证闸门在边界。

```typescript
// AI 组件注册表（白名单 + schema）
const UI_REGISTRY = {
  ProductCard: { props: z.object({ name: z.string(), price: z.number(), img: z.string().url() }) },
  Summary: { props: z.object({ text: z.string() }) },
  Chart: { props: z.object({ type: z.enum(['bar', 'line']), data: z.array(z.tuple([z.string(), z.number()])) }) },
};
// RSC 渲染：LLM 输出 → 组件
export async function AIRender({ llmOutput }: { llmOutput: string }) {
  const spec = JSON.parse(llmOutput);                    // { component, props }
  const entry = UI_REGISTRY[spec.component];
  if (!entry) throw new Error(`组件不在白名单: ${spec.component}`);   // 白名单校验
  const props = entry.props.parse(spec.props);           // zod schema 校验
  return renderComponent(spec.component, props);         // RSC 直接渲染
}
// 流式 JSON 解析（partial JSON 容错）
function parsePartial(json: string) {
  try { return JSON.parse(json); } catch {}
  // 补全未闭合的括号
  let s = json; let stack = [];
  for (const ch of json) if ('[{'.includes(ch)) stack.push(ch); else if (']}'.includes(ch)) stack.pop();
  for (const ch of stack.reverse()) s += ch === '{' ? '}' : ']';
  try { return JSON.parse(s); } catch { return null; }   // 流式渲染：字段到达即显示
}
```
