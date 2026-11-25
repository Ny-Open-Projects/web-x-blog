---
title: [WCN-782] 笔试：手写组件 a11y 自动检查器（axe 规则子集）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-782：笔试：手写组件 a11y 自动检查器（axe 规则子集）

**答**：
- 需求：实现 `a11yCheck(html)`，用简单正则/DOM 解析检查：① `<img>` 必须有 alt（可为空）；② 交互元素（button/a）无文本内容时检查 aria-label；③ `<input>` 应有对应 `<label for>` 或 aria-label。返回违规数组 `[{ rule, tag, msg }]`。可用 DOMParser（Node 环境假设有 jsdom）。
- 要点：正则匹配或 DOM 查询；alt 存在性用属性判断；label 关联用 for=id；边界：自闭合、大小写标签、空输入返回空数组。

```javascript
function a11yCheck(html) {
  const issues = [];
  const doc = new DOMParser().parseFromString(html, 'text/html');
  doc.querySelectorAll('img').forEach((img) => {
    if (!img.hasAttribute('alt')) issues.push({ rule: 'img-alt', tag: 'img', msg: '缺少 alt' });
  });
  doc.querySelectorAll('button, a').forEach((el) => {
    const text = el.textContent.trim();
    if (!text && !el.hasAttribute('aria-label'))
      issues.push({ rule: 'interactive-name', tag: el.tagName.toLowerCase(), msg: '缺少可访问名称' });
  });
  doc.querySelectorAll('input').forEach((input) => {
    const id = input.getAttribute('id');
    const labeled = (id && doc.querySelector(`label[for="${id}"]`)) || input.hasAttribute('aria-label');
    if (!labeled) issues.push({ rule: 'input-label', tag: 'input', msg: '缺少关联 label' });
  });
  return issues;
}
console.log(a11yCheck('<img src="a"><button></button><input id="x">'));
```

**评分点**：
- 三类规则（img alt / 交互名称 / input label）均覆盖。
- label 关联正确用 for=id 或 aria-label 判断。
- 返回结构化违规数组，含 rule/tag/msg。
- 空输入/大小写有边界防御。
