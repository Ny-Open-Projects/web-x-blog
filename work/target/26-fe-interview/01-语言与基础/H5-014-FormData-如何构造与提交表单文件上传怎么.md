---
title: [H5-014] FormData 如何构造与提交表单？文件上传怎么处理？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-014：FormData 如何构造与提交表单？文件上传怎么处理？
**答**：
- `new FormData(form)` 收集所有带 name 的控件；也可以不基于表单逐个 `append`。
- 用 fetch/XHR 提交 FormData 时不要手动设 `Content-Type`，浏览器自动生成带 boundary 的 multipart/form-data。
- 文件来自 `input.files`（FileList），File 是 Blob 的子类型，直接 append 即可上传。
- 服务端按 multipart 解析；大文件要配合分片（见 H5-033）。

```html
<form id="upload">
  <input name="title" value="我的头像" />
  <input name="avatar" type="file" accept="image/*" />
  <button type="submit">上传</button>
</form>

<script>
  const form = document.getElementById('upload');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    // 方式一：基于已有表单收集
    const fd = new FormData(form); // 自动带上 title 与 avatar 文件

    // 方式二：手动构造/追加
    // const fd = new FormData();
    // fd.append('title', '我的头像');
    // fd.append('avatar', form.elements.avatar.files[0]);
    fd.append('client', 'web');

    const res = await fetch('/api/upload', {
      method: 'POST',
      body: fd, // 关键：不设置 Content-Type，让浏览器生成 multipart boundary
    });
    console.log(await res.json());
  });
</script>
```
