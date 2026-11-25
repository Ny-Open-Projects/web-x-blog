---
title: [AIC-989] 商品列表还有大量 jQuery 时代的老代码要迁移到 React，AI 结对在这场迁移里的边界在哪？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-989：商品列表还有大量 jQuery 时代的老代码要迁移到 React，AI 结对在这场迁移里的边界在哪？
**答**：
- 明确「AI 能做什么、不能做什么」：AI 擅长机械转换（DOM 操作→JSX 的初稿、事件绑定→onChange）、补类型、写测试脚手架；不擅长判断「这段老逻辑背后的业务意图」——结论：AI 做翻译，人做决策。
- 高危区要人主导：涉及隐式全局状态、DOM 直接操作顺序依赖、老浏览器兼容 hack 的代码，AI 容易误判，必须人先理解再让 AI 辅助改写。
- 边界落为「检查点」：每完成一个模块的迁移，用差分/快照验证行为等价（呼应 AIC-953），过不了就不能算迁移完成——结论：边界由验证守门。
- 追问钩子：能说出「遗留迁移最大的风险不是语法转换，而是『没人知道它在干什么』的隐式行为；AI 会自信地重写掉这些，所以边界要划在『未知意图』处」的候选人理解得最深。

```typescript
// 迁移边界：按风险分级决定 AI 参与度
function aiAutonomy(code) {
  if (/\$\(|\.on\(|innerHTML/.test(code)) return 'human-led';   // jQuery/DOM 操作
  if (/window\.|global\w*|document\./.test(code)) return 'review-required'; // 全局依赖
  return 'ai-can-draft'; // 纯逻辑可让 AI 起草
}
const snippets={ a:"$('#list').on('click',f)", b:'const total = items.reduce((s,x)=>s+x,0)' };
// 按参与度分配验证强度：人主导的也要有差分校验守门
const verifyPlan = {
  'human-led': '人先理解→手改写→特征化测试验证',
  'review-required': 'AI起草→人工重点评审全局依赖',
  'ai-can-draft': 'AI起草→差分测试全自动验证',
};
console.log(Object.entries(snippets).map(([k,v])=>({
  k, mode:aiAutonomy(v), verify:verifyPlan[aiAutonomy(v)]
})));
```
