---
title: [AGT-296] Agent 输出的渐进渲染——从 token 流到结构化组件？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-296：Agent 输出不只是文本（表格/图表/卡片），渐进渲染怎么设计？

**答**:
- 输出分级渲染：纯文本走 markdown 流式（AGT-153）；结构化块（表格/代码/图表）由 Agent 输出带类型标记的块（`{type:'table', data}`）——结构块整体渲染（数据齐了才渲染，避免半张表），文本块流式渲染——两类节奏不同，渲染器要分流。
- 组件化协议：定义"Agent 组件协议"——服务端输出 UI 描述（组件类型+props），前端白名单组件渲染（不允许任意 HTML——XSS 与一致性风险），组件库版本与服务端约定兼容。
- 占位与骨架：长生成块先骨架屏+进度（"正在生成图表…"），完成后替换——感知性能优于真实等待；流式中断的块显示"生成中断"+重试。
- 缓存与复用：结构块的渲染结果可缓存（数据 hash 相同直接复用 DOM/图片），高频图表类输出（图表渲染贵）收益明显。

```javascript
const RENDERERS = { table: TableV, chart: ChartV, text: MdStream };
function renderBlock(block) {
  const C = RENDERERS[block.type];          // 白名单组件
  if (!C) return fallback(block);           // 未知类型兜底
  if (isStreaming(block.type)) return <C stream={block} />;
  return block.data ? <C {...block.data} /> : <Skeleton />;
}
// 结构块整块渲染，文本块流式；
// 组件协议版本对齐，未知类型不崩。
```
