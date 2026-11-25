---
title: [AGT-718] 产品截图/操作指引类知识库的索引与问答有什么特殊设计？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-718：产品截图/操作指引类知识库的索引与问答有什么特殊设计

**答**：
- 截图的核心信息是「UI 结构」：入库时用 vision 提取「界面元素树」（按钮/菜单/输入框名称与位置），与操作步骤文本配对索引——问"在哪里设置 XX"检索的是元素名而非截图语义。
- 版本敏感：UI 截图随版本过时（按钮改名/位置变了），截图带产品版本标记，回答时优先返回当前版本的截图并提示旧版本引用。
- 步骤链：操作指引按「步骤序列」组织（步骤 N 的截图+说明），回答时按步骤渲染为图文教程卡而不是散乱引用。

```javascript
async function indexScreenshot(img, guide) {
  const ui = await vision(img, EXTRACT_UI_TREE);   // 界面元素树
  return guide.steps.map((step, i) => ({
    text: step.text,
    uiElements: ui.elements,                       // 元素名可检索
    ref: { img, step: i + 1, productVer: guide.version },
  }));
}
```

