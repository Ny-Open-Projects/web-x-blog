---
title: [H5-029] File 对象从哪来？input file 有哪些常用配置？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-029：File 对象从哪来？input file 有哪些常用配置？
**答**：
- 来源：`<input type="file">` 的 `files`、拖放 `drop` 事件的 `dataTransfer.files`、剪贴板事件。
- `accept` 限制可选类型（MIME 或后缀），`multiple` 多选，`capture` 移动端直接调相机。
- File 继承 Blob，有 `name/size/type/lastModified` 属性；选择同一文件第二次不触发 change，需要手动清空 value。
- 读取内容靠 FileReader（H5-030）或新的 `file.text()/file.arrayBuffer()` Promise API。

```html
<input id="picker" type="file" accept="image/png,image/jpeg,.webp" multiple />

<script>
  const picker = document.getElementById('picker');
  picker.addEventListener('change', () => {
    for (const file of picker.files) {
      console.log(file.name, file.type, file.size, new Date(file.lastModified));
      if (file.size > 5 * 1024 * 1024) alert(`${file.name} 超过 5MB`);
    }
    // 需求：支持反复选择同一个文件
    picker.value = ''; // 清空后 change 可重复触发
  });
</script>
```
