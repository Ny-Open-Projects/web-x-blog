---
title: [1163] 模型传入工具的参数怎么知道「是否被外部内容影响」
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 安全]
type: 面试题
---

## 1163：模型传入工具的参数怎么知道「是否被外部内容影响」

**答**：
- 污点分析思路：上下文里每个来源有信任标记（system=可信、user=半可信、external=污点）；模型生成参数引用了污点内容时，参数标记为「受污染」，高危工具拒绝受污染参数或强制审批。
- 工程实现：无法真正追踪模型「引用了哪段」（模型不暴露引用），用启发式近似——参数值与上下文污点片段的相似度、参数中出现上下文独有的字符串（URL/路径/ID）即视为受影响。
- 意义：把「注入成功」与「危害达成」的判据从「模型是否被忽悠」变成「污点数据是否流入高危参数」——可度量、可拦截。
- 追问钩子：误报（合法引用外部数据）怎么办？——白名单通道：用户明确确认过的外部数据（粘贴的文档）允许流入，且确认行为入审计。

```ts
function taintCheck(params, ctx) {
  const tainted = ctx.spans.filter(s => s.trust === 'external');
  for (const [k, v] of Object.entries(params)) {
    if (typeof v === 'string' && tainted.some(s => mentions(v, s.text))) {
      return { tainted: true, param: k };          // 污点参数
    }
  }
  return { tainted: false };
}
async function execTool(tool, params, ctx) {
  const t = taintCheck(params, ctx);
  if (t.tainted && tool.risk >= 2) return approval.require({ tool, params, taintedParam: t.param });
  return tool.run(params);
}
```
