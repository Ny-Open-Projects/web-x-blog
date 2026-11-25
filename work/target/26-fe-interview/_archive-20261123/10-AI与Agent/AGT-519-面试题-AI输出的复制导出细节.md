---
title: [AGT-519] 复制/导出 AI 回复有哪些细节坑（格式保留、代码块、图片防盗、水印）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-519：复制/导出 AI 回复有哪些细节坑（格式保留、代码块、图片防盗、水印）

**答**：
- 复制分「富文本复制」（保留 markdown 渲染样式，贴进飞书/Word 好看）与「纯文本复制」（原始 markdown），两个入口都要，默认给用户所在场景更常用的那个。
- 导出含代码块时保留语言标记与缩进；导出含图片时走服务端代理导出（防盗链与权限），并加轻水印（用户 ID+时间）满足合规。
- 复制动作埋点归因到消息，复制率是内容质量的重要信号。

```javascript
async function copyMessage(msgId, mode = 'rich') {
  const msg = getMsg(msgId);
  if (mode === 'rich') {
    const html = await renderRich(msg.content);  // 含样式的 HTML
    navigator.clipboard.write([new ClipboardItem({
      'text/html': new Blob([html], { type: 'text/html' }),
      'text/plain': new Blob([msg.content], { type: 'text/plain' }),
    })]);
  } else {
    await navigator.clipboard.writeText(msg.content);
  }
  track('ai_copy', { msgId, mode, modelVer: msg.modelVersion });
}
```

