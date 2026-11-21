---
title: [WCN-084] 笔试：手写 Signals 版 Markdown 实时预览（脏检查 + rAF 渲染）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-084：笔试：手写 Signals 版 Markdown 实时预览

**题目**：① `doc` signal 保存 markdown 文本；② 预览渲染是重计算（模拟解析器 `parse(md)` 耗时 >10ms），要求：输入高频变化时不逐键渲染；③ 用 effect + rAF：同帧多次变化只渲染最后一次；④ 渲染结果 HTML 注入用安全方式（textContent 或 sanitize）；⑤ `renderCount` signal 记录渲染次数供测试；⑥ dispose 停止。

**答**：

```javascript
import { createSignal, effect, untrack } from './mini.js';

export function setupPreview(editor, previewEl, parse) {
  const [doc, setDoc] = createSignal('');
  const [renderCount, setRC] = createSignal(0);
  editor.addEventListener('input', () => setDoc(editor.value));

  let scheduled = false;
  const stop = effect(() => {
    doc(); // 建立依赖
    if (scheduled) return;
    scheduled = true;
    requestAnimationFrame(() => {           // 合帧：同帧 N 次输入只渲染 1 次
      scheduled = false;
      const md = untrack(doc);              // rAF 内 activeSub 已恢复，untrack 读快照
      const html = parse(md);               // 重计算：每帧最多一次
      previewEl.innerHTML = sanitize(html); // 必须清洗，md 中可能有 <img onerror>
      setRC(untrack(renderCount) + 1);
    });
  });

  return { doc, renderCount, dispose: stop };
}
// 简化 sanitize：仅允许白名单标签与属性（生产用 DOMPurify）
function sanitize(html) {
  const tpl = document.createElement('template');
  tpl.innerHTML = html;
  const allowed = new Set(['P','B','I','EM','STRONG','CODE','PRE','H1','H2','H3','UL','OL','LI','A']);
  tpl.content.querySelectorAll('*').forEach((el) => {
    if (!allowed.has(el.tagName)) { el.remove(); return; }
    [...el.attributes].forEach((a) => { if (!/^href$/.test(a.name) || !a.value.startsWith('https:')) el.removeAttribute(a.name); });
  });
  return tpl.innerHTML;
}
```

**评分点**：
- 合帧策略：rAF 收敛高频输入，同帧只渲染最后一次（性能考点）。
- rAF 回调里 activeSub 已恢复 null，用 untrack 显式读快照（依赖语义细节）。
- sanitize 白名单思路（至少答出"必须清洗"）；href 只允许 https。
- renderCount 供测试断言（工程意识）；dispose 清理。
