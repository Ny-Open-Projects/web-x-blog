---
title: [SCN-341] 协作文档 AI 助手——编辑器内 AI 能力的嵌入设计？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-341：协作文档内嵌 AI 助手（续写/改写/翻译/总结）怎么设计？

**答**:
- 嵌入形态：行内触发（选中文本→浮动 AI 菜单：改写/翻译/扩写）、斜杠命令（空行 /ai 续写）、侧边助手（全文级：总结/问答——AGT-301 文档助手复用）；触发体验轻量（不遮挡编辑流）。
- 生成结果的应用：diff 预览（AI 改写结果与原文对比——接受/重试/取消，不直接覆盖）、插入位置锚定（光标处插入生成文本——协作文档中 AI 插入与 CRDT 协同（AI 操作也是一次编辑操作进 seq 流水，多人可见）、流式插入（生成 token 流式进文档——未闭合状态渲染 SCN-153 处理）。
- 权限与审计：AI 功能权限（文档级开关——企业可禁用）、AI 生成内容标识（编辑历史标注"AI 生成"段——可追溯）、内容安全（生成内容走审核——SCN-326 体系）。
- 成本与配额：用户配额（个人 AI 调用额度）、按需触发（非自动生成——用户显式请求控制成本）、结果缓存（同上下文重复请求缓存）。

```javascript
async function aiRewrite(selection) {
  const menu = showFloatMenu(['改写','翻译','扩写']);
  const action = await menu.pick();
  const stream = aiApi.rewrite(selection.text, action, { stream: true });
  // 流式插入为协作操作（进 CRDT 流水，多人可见）
  let buf = '';
  for await (const chunk of stream) {
    buf += chunk;
    ydoc.transact(() => ytext.insert(pos, chunk));   // 流式插入
  }
  showDiffPreview({ before: selection.text, after: buf,
    actions: ['接受', '重试', '放弃'] });            // 不直接覆盖
}
// 审计：ydoc meta 标注 AI 段；配额：quota.check(me)。
```
