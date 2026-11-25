---
title: [AGT-472] 笔试题——实现会话导出格式转换（JSON→Markdown/HTML+附件打包）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-472：手写导出转换器：多格式渲染、附件收集、schema 版本标注

**需求与边界**：
- 输入：会话 JSON、目标格式；输出：可读文件。
- 边界要求：① 消息角色映射（user/assistant/tool 各有样式）；② 结构块渲染（表格/代码转 Markdown）；③ 附件（图片/文件）收集打包（引用相对路径不断链）；④ 导出含 schema 版本与生成时间。

**答**：
```javascript
function exportConversation(session, format) {
  const fmt = { markdown: md, html: html }[format];
  if (!fmt) throw new Error(`不支持格式: ${format}`);
  const files = [];                                 // 附件收集
  const body = session.messages.map(m => {
    const who = { user: '👤 用户', assistant: '🤖 助手',
      tool: '🔧 工具' }[m.role] ?? m.role;
    const content = fmt(m, { collect: (name, data) => {
      const rel = `attachments/${files.length}_${name}`;
      files.push({ rel, data });
      return rel;                                   // 相对路径引用
    }});
    return `### ${who}（${timeOf(m)}）\n\n${content}`;
  }).join('\n\n---\n\n');
  return {
    files: [{ rel: 'conversation.md', data:
      `# 会话导出\n\n> schema v${session.schemaVersion}` +
      ` · 生成于 ${new Date().toISOString()}\n\n${body}` },
      ...files],
  };
}
function md(m, ctx) {
  if (m.role === 'tool')
    return `**调用** ${m.tool}\n\n\`\`\`\n${truncate(m.result)}\n\`\`\``;
  // 结构块：表格转 Markdown 表格
  return m.blocks?.map(b => b.type === 'table'
    ? renderMdTable(b.data) : b.text).join('\n')
    ?? m.content.replace(/!\[[^\]]*\]\(([^)]+)\)/g,
      (_, src) => ctx.collect(fileNameOf(src), src));
}
```

**评分点**:
- 角色映射与时间戳、结构块转 Markdown 表格。
- 附件收集打包+相对路径引用（离线可读不断链）。
- schema 版本与生成时间标注（可解释可追溯）。
- 未知格式显式报错（不静默降级）。
