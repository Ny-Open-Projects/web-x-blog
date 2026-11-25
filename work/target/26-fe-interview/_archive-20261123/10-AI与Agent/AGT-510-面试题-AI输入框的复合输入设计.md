---
title: [AGT-510] AI 对话输入框要支持文本+附件+语音+@引用知识库，复合输入的交互与数据结构怎么设计？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-510：AI 对话输入框要支持文本+附件+语音+@引用知识库，复合输入的交互与数据结构怎么设计

**答**：
- 输入框本质是「parts 数组」：text / image / file / mention（知识库或 agent）统一建模，发送时按服务端协议序列化，而不是拼接字符串。
- mention 用触发符 + 异步联想（@后搜知识库），插入的是结构化引用（id+title），渲染成 chip；粘贴图片要给缩略图预览与移除入口。
- 草稿按会话持久化（含 parts），切换会话不丢；语音输入与文本编辑共存时给明确的合成预览。

```javascript
// 输入模型：parts 数组
function buildDraft() { return {
  parts: [
    { type: 'text', value: '帮我看下 ' },
    { type: 'mention', ref: { kind: 'kb', id: 'kb-12', title: '退款政策' } },
    { type: 'text', value: ' 这份文档，另外这两个截图里的问题也回答下' },
    { type: 'image', assetId: 'a-1', preview: blobUrl },
  ],
}; }
function serialize(parts) {  // 发送前按协议序列化，mention 换成标准标记
  return parts.map(p => p.type === 'text' ? p.value
    : p.type === 'mention' ? `@kb:${p.ref.id}` : `[asset:${p.assetId}]`).join('');
}
```

