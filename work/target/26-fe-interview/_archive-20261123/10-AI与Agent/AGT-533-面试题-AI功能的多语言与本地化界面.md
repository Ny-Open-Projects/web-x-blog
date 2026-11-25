---
title: [AGT-533] AI 产品出海，界面 i18n 之外模型回复的语言策略怎么处理？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-533：AI 产品出海，界面 i18n 之外模型回复的语言策略怎么处理

**答**：
- 语言策略三层：用户界面语言（i18n）、回复语言（跟用户输入语言走，显式写入系统提示）、内容语言（知识库文档语言与回复语言不一致时要声明"依据英文文档，以中文回答"）。
- RTL 语言（阿语/希伯来）专项：流式渲染、光标动画、引用角标位置都要 RTL 镜像，测试不能只靠切 locale。
- 混合语言输入（中英夹杂）要在系统提示中明确回复基准语言，避免模型"跟丢"。

```javascript
function buildSystemSuffix(user, kbLang) {
  const lang = detectLang(user.lastInput) ?? user.prefLang;
  return [`Always reply in ${langName(lang)}.`,
    kbLang !== lang ? `Sources are in ${langName(kbLang)}; cite them but reply in ${langName(lang)}.` : '',
    user.rtl ? 'Use RTL-friendly formatting (avoid left-only markers).' : ''].join(' ');
}
```

