---
title: [TST-432] 笔试：SSR HTML 快照的语义归一化（去随机噪声）。
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-432：笔试：SSR HTML 快照的语义归一化（去随机噪声）。
**题目**：归一规则：去 <style> 内容/去随机属性（id 以随机后缀）/时间戳占位替换/空白归一。实现 `normalizeHTML(html, {randomAttrRe, timeRe})` 后做快照对比。

```javascript
export function normalizeHTML(html, { randomAttrRe = /\sid="[^"]*__\w{6}"/g, timeRe = /\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}/g } = {}) {
  return html
    .replace(/<style[\s\S]*?<\/style>/g, '<style/>')
    .replace(randomAttrRe, ' id="__N__"')
    .replace(timeRe, '<TIMESTAMP>')
    .replace(/\s+/g, ' ').trim();
}
// 快照：expect(normalizeHTML(html2)).toBe(normalizeHTML(baselineHtml))

```

**评分点**：
- 三类噪声处理（style/随机属性/时间）。
- 占位替换（<TIMESTAMP>）保留结构。
- 空白归一（跨标签空白折叠）。
- 规则可配置（randomAttrRe 注入）。
