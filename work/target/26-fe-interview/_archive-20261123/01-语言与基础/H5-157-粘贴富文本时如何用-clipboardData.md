---
title: [H5-157] 粘贴富文本时如何用 clipboardData 清洗？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-157：粘贴富文本时如何用 clipboardData 清洗？
**答**：
- `paste` 事件里 `e.clipboardData.getData('text/html')` 保留结构、`getData('text/plain')` 兜底；`e.preventDefault()` 拦下默认的"原样插入"。
- 清洗流程：`DOMParser` 解析 → 白名单标签过滤（非白名单**展开文本内容**而不是直接丢，保住段落内文字）→ 白名单属性（a.href、img.src/alt）→ 移除 script/style/事件属性。
- 图片粘贴（截图）：`clipboardData.items` 里直接有 `image/png` 文件，取 `getAsFile()` 上传。
- 复制方向也能定制：`setData` 同时写 text/plain 与 text/html 双格式，甚至写内部协议 JSON（内部粘贴识别协议、外部降级 HTML）。

```html
<div id="editor" contenteditable="true">粘贴富文本试试</div>
<script>
const ALLOWED = { P: 1, BR: 1, B: 1, STRONG: 1, EM: 1, I: 1, U: 1, A: 1,
                  UL: 1, OL: 1, LI: 1, IMG: 1, H1: 1, H2: 1, H3: 1, BLOCKQUOTE: 1 };
const KEEP_ATTR = { A: ['href', 'title'], IMG: ['src', 'alt'] };

document.getElementById('editor').addEventListener('paste', (e) => {
  e.preventDefault();                        // 拦下默认的"原样插入"
  const dt = e.clipboardData;
  const html = dt.getData('text/html');
  const text = dt.getData('text/plain');

  // 截图粘贴：items 里直接有 image/png
  const imageItem = [...dt.items].find((i) => i.type.startsWith('image/'));
  if (imageItem) return insertImage(imageItem.getAsFile());

  if (html) insertNode(sanitize(html));      // 有 HTML 用清洗后的结构
  else if (text) document.execCommand('insertText', false, text);  // 纯文本兜底
});

function sanitize(html) {
  const doc = new DOMParser().parseFromString(html, 'text/html');
  clean(doc.body);
  return doc.body;
}
function clean(node) {
  [...node.children].forEach((child) => {
    clean(child);
    if (!ALLOWED[child.tagName]) {
      // 非白名单：展开文本内容而不是直接丢（style/script 除外）
      if (child.tagName !== 'SCRIPT' && child.tagName !== 'STYLE')
        child.replaceWith(...child.childNodes);
      else child.remove();
      return;
    }
    // 白名单标签：只保留必要属性
    [...child.attributes].forEach((a) => {
      if (!KEEP_ATTR[child.tagName]?.includes(a.name)) child.removeAttribute(a.name);
    });
  });
}
function insertNode(node) {
  const sel = document.getSelection();
  const r = sel.getRangeAt(0);
  r.deleteContents();
  r.insertNode(node);
  sel.collapseToEnd();
}
function insertImage(file) {
  const img = new Image();
  img.src = URL.createObjectURL(file);       // 实际项目：先上传再插 URL
  insertNode(img);
}
</script>
```

## 二十六、文档与可编辑
