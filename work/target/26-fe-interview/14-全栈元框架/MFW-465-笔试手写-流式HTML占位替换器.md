---
title: [MFW-465] 笔试：手写流式 HTML 占位替换器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-465：流式 HTML 占位替换器（loading.js 语义）
**需求**：实现 `createStreamInjector()`：1) 首屏先 flush 含占位注释 `<!--slot:ID-->` 的 HTML 壳；2) 后台分段完成后调用 `inject(id, html)`，生成 `<template data-slot>` + 替换脚本：`<script>$RL(id,html)</script>` 形式推入写出队列（真实框架用隐藏 div + innerHTML 换入）；3) `writeTo(stream)` 保证顺序：壳未 flush 完先排队；4) 注入脚本必须转义 `</script`（防提前闭合注入 XSS——流式注入头号安全问题）。

```javascript
const esc = s => s.replace(/<\/script/gi, '<\\/script') // 关键转义

export function createStreamInjector() {
  const pending = []   // 壳 flush 前积压的注入
  let shellDone = false
  return {
    async writeShell(stream, shellHtml) {
      await stream.write(shellHtml)
      shellDone = true
      for (const chunk of pending.splice(0)) await stream.write(chunk)
    },
    inject(id, html) {
      const chunk =
        `<template data-slot="${id}">${html}</template>` +
        `<script>$RL(${JSON.stringify(id)},${JSON.stringify(html)})</script>`
      const safe = esc(chunk)
      if (shellDone) this.out?.write(safe); else pending.push(safe)
    },
    async flush(stream) {
      this.out = stream
      if (shellDone) for (const c of pending.splice(0)) await stream.write(c)
    },
  }
}
```

**评分点**：
- 占位注释定位 slot（壳与洞解耦——loading.js 本质）
- 壳未完成时注入排队（乱序写出即页面破碎）
- `</script` 转义（内容含脚本闭合标签时 HTML 被劫持）
- template 承载 + 脚本换入两层（真实 RSC 注入的同构思路）
