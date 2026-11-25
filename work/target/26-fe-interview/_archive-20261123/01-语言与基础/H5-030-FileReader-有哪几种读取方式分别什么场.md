---
title: [H5-030] FileReader 有哪几种读取方式？分别什么场景用？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-030：FileReader 有哪几种读取方式？分别什么场景用？
**答**：
- `readAsText`：读文本（配置、日志）；`readAsDataURL`：读成 base64 Data URL（小图预览）；`readAsArrayBuffer`：读二进制（加密、解析、媒体处理）。
- FileReader 是事件式 API（onload/onerror/onprogress），现代写法可直接用 `file.text()`、`file.arrayBuffer()`。
- 图片预览更推荐 `URL.createObjectURL(file)`：不生成 base64 大字符串，内存友好，用完 `revokeObjectURL` 释放。
- base64 体积比原文件大 33%，大文件预览别用 readAsDataURL。

```html
<input id="reader" type="file" accept="image/*" />
<img id="preview" alt="预览" style="max-width:200px;display:block" />

<script>
  const input = document.getElementById('reader');
  const img = document.getElementById('preview');

  input.addEventListener('change', async () => {
    const file = input.files[0];
    if (!file) return;

    // 方式一：object URL 预览（推荐，无 base64 膨胀）
    const url = URL.createObjectURL(file);
    img.src = url;
    img.onload = () => URL.revokeObjectURL(url); // 用完释放，防内存泄漏

    // 方式二：FileReader 经典事件式
    const reader = new FileReader();
    reader.onload = (e) => console.log('dataURL:', e.target.result.slice(0, 40), '...');
    reader.onerror = () => console.error('读取失败');
    reader.readAsDataURL(file);

    // 方式三：现代 Promise API（等价于 readAsText）
    const text = await file.text(); // 文本文件可直接读
    console.log(text.slice(0, 20));
  });
</script>
```
