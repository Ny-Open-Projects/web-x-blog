---
title: [AGT-568] 用户消息被系统扩展（检索注入/历史摘要注入），前端如何透明化？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-568：用户消息被系统扩展（检索注入/历史摘要注入），前端如何透明化

**答**：
- "实际发给模型的"与"用户输入的"不同（用户问题 + 检索片段 + 摘要注入），透明化原则：默认展示用户视角，可展开查看"系统补充了什么"。
- 展示形式：消息气泡角落的"信息源"图标，展开后列出注入项（检索片段数/命中文档/是否用摘要替代了早期历史），让用户理解回答为什么这样来。
- 敏感场景（企业合规）可强制常显注入摘要，默认折叠；注入内容要脱敏后展示。

```javascript
function InjectedContextBadge({ turn }) {
  const inj = turn.injections ?? [];       // [{type:'rag',docs:[...]}, {type:'summary'}]
  if (!inj.length) return null;
  return <Popover trigger={<Icon name="info" />}>
    {inj.map(i => <div key={i.type}>
      {i.type === 'rag' && `已检索 ${i.docs.length} 篇文档辅助回答`}
      {i.type === 'summary' && '早期对话已用摘要压缩注入'}
    </div>)}
  </Popover>;
}
```

