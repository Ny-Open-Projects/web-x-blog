---
title: [H5-188] 设计一个 Markdown 编辑器（分屏预览/同步滚动）
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-188：设计一个 Markdown 编辑器（分屏预览/同步滚动）
**答**：
- 渲染管线：input 防抖（~150ms）→ `marked.parse()` → **DOMPurify 清洗**（用户 markdown 不可信，XSS 防线必须前置）→ 更新预览。
- 同步滚动：核心是**源行号 ↔ 预览元素**的映射表（渲染时给每个块级元素记 data-src-line），双向跟随 + `rendering` 互斥锁防"滚动乒乓"。
- 工具栏插入（加粗/列表）：操作 textarea 的 `selectionStart/End` 在文本层完成，插完 `setSelectionRange` 恢复光标并触发 input。
- 进阶：CodeMirror 6 做编辑器（行号/高亮/大文件性能）、图片粘贴上传、`prefers-color-scheme` 双主题。

```html
<div class="split">
  <textarea id="md"># 标题</textarea>
  <div id="preview" class="preview"></div>
</div>
<style>
  .split { display: flex; height: 320px; }
  #md { flex: 1; font: 14px/21px monospace; padding: 12px; }
  .preview { flex: 1; overflow: auto; padding: 12px; border-left: 1px solid #eee; }
</style>
<script src="https://cdn.example.com/marked.min.js"></script>
<script src="https://cdn.example.com/purify.min.js"></script>
<script>
const editor = document.getElementById('md');
const preview = document.getElementById('preview');
let rendering = false;                       // 互斥锁防"滚动乒乓"

// 1) 渲染管线：防抖 + XSS 防线（用户 markdown 不可信，必须 sanitize）
let timer;
editor.addEventListener('input', () => {
  clearTimeout(timer);
  timer = setTimeout(() => {
    // DOMPurify 清洗是必须项，不是可选项
    preview.innerHTML = DOMPurify.sanitize(marked.parse(editor.value));
    buildLineMap();
  }, 150);
});

// 2) 同步滚动：源行号 ↔ 预览元素映射（marked lexer 提供 token 位置，简化演示）
let lineMap = [];                            // [{ src: 12, el }]
function buildLineMap() {
  lineMap = [...preview.querySelectorAll('h1,h2,h3,p,li,pre,blockquote')]
    .map((el) => ({ src: +el.dataset.srcLine || lineOf(el), el }));
}
function lineOf() { return 0; }              // 实际由渲染阶段写入 data-src-line
function syncScroll(from) {
  if (rendering) return;
  rendering = true;
  if (from === 'editor') {
    const line = Math.floor(editor.scrollTop / 21);           // 近似行号
    const hit = lineMap.filter((m) => m.src <= line).pop();
    if (hit) preview.scrollTop = hit.el.offsetTop - 16;
  } else {
    const hit = lineMap.find((m) => m.el.offsetTop >= preview.scrollTop);
    if (hit) editor.scrollTop = hit.src * 21;
  }
  requestAnimationFrame(() => (rendering = false));
}
editor.addEventListener('scroll', () => syncScroll('editor'));
preview.addEventListener('scroll', () => syncScroll('preview'));

// 3) 工具栏插入：文本层操作 selectionStart/End，不走 DOM
function wrapSelection(before, after = before) {
  const [s, e] = [editor.selectionStart, editor.selectionEnd];
  const v = editor.value;
  editor.value = v.slice(0, s) + before + v.slice(s, e) + after + v.slice(e);
  editor.setSelectionRange(s + before.length, e + before.length);
  editor.dispatchEvent(new Event('input'));  // 触发渲染管线
  editor.focus();
}
document.getElementById('bold')?.addEventListener('click', () => wrapSelection('**'));
// 4) 进阶：CodeMirror 6 做编辑器、粘贴图片上传、暗色主题跟随 prefers-color-scheme
</script>
```
