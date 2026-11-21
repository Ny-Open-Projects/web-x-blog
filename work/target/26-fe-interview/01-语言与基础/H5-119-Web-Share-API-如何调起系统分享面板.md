---
title: [H5-119] Web Share API 如何调起系统分享面板？能力检测怎么写？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-119：Web Share API 如何调起系统分享面板？能力检测怎么写？
**答**：
- `navigator.share({ title, text, url, files })` 调起**操作系统原生分享面板**（微信、系统分享目标等），是移动端替代自绘分享菜单的标准方案。
- 强约束：必须在**用户手势**内调用；不支持的浏览器直接抛错，必须 `'share' in navigator` 检测并降级。
- 分享文件：`files` 传 File 数组 + `navigator.canShare({ files })` 预检（canShare 比 in navigator 更准，能验证具体数据是否可分享）。
- `navigator.share` 之外还有接收侧：Web Share Target（PWA manifest 声明，让本站出现在别人的分享面板里）。
- 降级链：canShare false → 复制链接 + toast（clipboard API，见 H5-035）。

```javascript
async function sharePage() {
  const data = {
    title: '前端面试工程',
    text: '75 道 HTML5 进阶面试题',
    url: location.href,
  };

  // 1) 能力检测：share 存在 + 数据可分享
  if (navigator.canShare?.(data)) {
    try {
      await navigator.share(data);            // 必须在 click 手势里
      return;
    } catch (err) {
      if (err.name === 'AbortError') return;  // 用户取消，静默
      console.warn('分享失败：', err);
    }
  }

  // 2) 降级：复制链接
  await navigator.clipboard.writeText(data.url);
  toast('链接已复制，去粘贴给朋友吧');
}

shareBtn.addEventListener('click', sharePage);

// 3) 分享文件（图片）：canShare 预检 files
async function shareImage(blob, name) {
  const file = new File([blob], name, { type: blob.type });
  if (navigator.canShare?.({ files: [file] })) {
    await navigator.share({ files: [file], title: name });
  } else {
    downloadFallback(blob, name);
  }
}
```
