---
title: [H5-088] FileReader 与 URL.createObjectURL 怎么取舍？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-088：FileReader 与 URL.createObjectURL 怎么取舍？
**答**：
- `createObjectURL` 是**零读取引用**：拿到 blob: 地址就返回，数据仍按需被浏览器读取，`img.src` 直连，快且省内存；代价是必须手动 `revokeObjectURL` 防泄漏。
- `FileReader` 是**真实读取**：readAsArrayBuffer/DataURL/Text 产出"数据本身"，适合需要内容做处理（预览+压缩、解析、哈希）的场景。
- 只做**预览/下载**（头像回显、视频封面）一律 objectURL；做**内容加工**（压缩后上传、逐字节解析）才用 FileReader 或 Blob 方法。
- `readAsDataURL` 产出 base64：体积膨胀约 33%，仅在小图标内联、无 objectURL 环境时使用，大图别用。
- 生命周期差异：objectURL 随文档卸载失效，需主动释放；FileReader 结果是普通字符串/Buffer，天然无泄漏问题。

```javascript
const fileInput = document.querySelector('input[type=file]');
const img = document.querySelector('img.preview');

// 场景 A：纯预览 —— objectURL 完胜
fileInput.addEventListener('change', () => {
  const file = fileInput.files[0];

  if (img.dataset.url) URL.revokeObjectURL(img.dataset.url); // 释放上一张
  const url = URL.createObjectURL(file);
  img.src = url;
  img.dataset.url = url;                     // 记录以便下次释放
  // img 实际加载时机由浏览器决定，同步返回，界面不卡
});

// 场景 B：预览 + 压缩 —— FileReader/Blob 方法读内容才有意义
async function compress(file) {
  const bitmap = await createImageBitmap(file);   // 亦可 FileReader->Image
  const cv = document.createElement('canvas');
  cv.width = bitmap.width / 2;
  cv.height = bitmap.height / 2;
  cv.getContext('2d').drawImage(bitmap, 0, 0, cv.width, cv.height);
  return new Promise(r => cv.toBlob(r, 'image/jpeg', 0.8));
}

// 场景 C：小图内联（邮件模板/无独立资源环境）才用 base64
function asDataURL(file) {
  return new Promise((res, rej) => {
    const fr = new FileReader();
    fr.onload = () => res(fr.result);          // data:image/png;base64,...
    fr.onerror = rej;
    fr.readAsDataURL(file);
  });
}
```
