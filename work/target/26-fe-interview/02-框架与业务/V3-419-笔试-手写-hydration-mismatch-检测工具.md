---
title: [V3-419] 笔试：手写 hydration mismatch 检测工具
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-419：笔试：手写 hydration mismatch 检测工具
**答**：实现 `diffHtml(serverHtml, clientTree)`：服务端产出 HTML 字符串与客户端水合后的 DOM 树比较，返回首个不匹配的路径（如 `div#app > ul > li[2]`）与两边内容摘要；要求按标签名逐层比较，文本节点归一化空白。

```javascript
function normalizeText(s) { return s.replace(/\s+/g, ' ').trim() }
function parseHtml(html) {
  const doc = new DOMParser().parseFromString(html, 'text/html')
  return doc.body.firstElementChild
}
function diffHtml(serverHtml, clientEl) {
  const serverEl = parseHtml(serverHtml)
  function walk(a, b, path) {
    if (!a && b) return { path, msg: 'client extra node', b: b.outerHTML.slice(0, 100) }
    if (a && !b) return { path, msg: 'server extra node', a: a.outerHTML.slice(0, 100) }
    if (a.tagName !== b.tagName) return { path, msg: 'tag mismatch', a: a.tagName, b: b.tagName }
    const sa = normalizeText(a.childNodes[0]?.textContent ?? '')
    const sb = normalizeText(b.childNodes[0]?.textContent ?? '')
    if (a.childNodes.length !== b.childNodes.length || (a.children.length === 0 && sa !== sb)) {
      return { path, msg: 'content mismatch', a: sa.slice(0, 80), b: sb.slice(0, 80) }
    }
    for (let i = 0; i < a.children.length; i++) {
      const res = walk(a.children[i], b.children[i], `${path} > ${a.children[i].tagName.toLowerCase()}[${i}]`)
      if (res) return res
    }
    return null
  }
  return walk(serverEl, clientEl, serverEl.tagName.toLowerCase())
}
```
**评分点**：
- 逐层标签比较 + 首个不匹配即返回（路径可定位）。
- 文本归一化避免空白噪音误报。
- 两侧节点数不对称的分支处理（extra/missing）。
- 摘要截断（避免日志爆炸）。
