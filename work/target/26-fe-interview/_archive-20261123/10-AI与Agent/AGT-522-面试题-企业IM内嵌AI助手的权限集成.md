---
title: [AGT-522] 在飞书/钉钉/企微内嵌 AI 助手，消息卡片与权限集成要注意什么？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-522：在飞书/钉钉/企微内嵌 AI 助手，消息卡片与权限集成要注意什么

**答**：
- 输出降维：IM 卡片只支持受限的 markdown 子集（无复杂表格/公式），生成端要按目标平台做「渲染预算」，超限内容折叠为「查看详情」链接。
- 权限继承：AI 代用户查询数据时，必须以用户身份（user token / on-behalf-of）鉴权，不能拿应用级超级权限绕过——否则越权数据直接出现在群里。
- 交互闭环：卡片按钮（审批/采纳/重试）回传要带幂等键与操作者身份，避免转发卡片后他人误操作。

```javascript
// IM 卡片输出降维：按平台能力裁剪
function toCard(answer, platform) {
  const caps = { feishu: { table: true, katex: false, maxLen: 30000 },
                 wecom: { table: false, katex: false, maxLen: 4096 } }[platform];
  const blocks = answer.blocks.filter(b => caps[b.type] !== false);
  let body = renderBlocks(blocks).slice(0, caps.maxLen);
  if (answer.blocks.length > blocks.length)
    body += '\n[部分内容不支持展示，点击查看详情]';
  return { config: { wide_screen_mode: true }, elements: body };
}
```

