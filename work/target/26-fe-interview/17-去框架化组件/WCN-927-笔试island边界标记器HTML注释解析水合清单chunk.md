---
title: [WCN-927] 手写 island 边界标记器：从 HTML 注释解析水合清单与依赖 chunk
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-927：手写 island 边界标记器：从 HTML 注释解析水合清单与依赖 chunk

**题目**：实现 `parseIslands(html)`，HTML 中用注释标记岛边界：`<!--island:id=buy-box;chunk=buy.js;priority=0.9-->` 开始，`<!--/island:buy-box-->` 结束。返回 `{ islands: [{ id, chunk, priority, html }] }`。要求：① 解析出每个岛的属性（id/chunk/priority，priority 默认 0.5）；② 提取岛内的 HTML 片段（含注释之间的内容）；③ 支持嵌套标记时只取最外层（内层作为 html 内容保留）；④ 注释格式不合法（缺 id）时跳过并忽略该对标记；⑤ 不依赖 DOM API（用正则/字符串处理），纯函数可测试。请自足实现并给出可运行示例。

**答**：

```javascript
function parseIslands(html) {
  const openRe = /<!--\s*island:([^>]*?)-->/g;
  const islands = [], stack = [];
  let m, cursor = 0;
  while ((m = openRe.exec(html))) {
    const attrs = {};
    m[1].split(';').forEach(p => {
      const i = p.indexOf('=');
      if (i > 0) attrs[p.slice(0, i).trim()] = p.slice(i + 1).trim();
    });
    if (!attrs.id) continue; // 非法：缺 id 跳过
    const start = openRe.lastIndex;
    const closeTag = `<!--/island:${attrs.id}-->`;
    let end = html.indexOf(closeTag, start);
    if (end === -1) continue; // 未闭合，跳过
    islands.push({
      id: attrs.id,
      chunk: attrs.chunk || null,
      priority: attrs.priority ? Number(attrs.priority) : 0.5,
      html: html.slice(start, end),
    });
    cursor = end + closeTag.length;
    openRe.lastIndex = cursor; // 跳过内层标记（简化：不解析嵌套）
  }
  return { islands };
}
const html = `<div><!--island:id=buy-box;chunk=buy.js;priority=0.9-->
  <button>加购</button><!--/island:buy-box--></div>`;
console.log(parseIslands(html).islands[0]);
// { id:'buy-box', chunk:'buy.js', priority:0.9, html:'\n  <button>加购</button>' }
```

**评分点**：
- 正确解析注释属性（id/chunk/priority），priority 默认 0.5。
- 提取岛内 HTML 片段，起止边界准确。
- 缺 id / 未闭合的非法标记被跳过，不抛异常。
- 不依赖 DOM，纯字符串/正则实现，可离线测试。
- 示例输出结构正确、可运行；嵌套处理有明确策略。
