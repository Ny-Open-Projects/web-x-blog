---
title: [SCN-030] 下载接口需要 Authorization 头，window.open 直接打开链接带不上 Token，怎么办？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-030：下载接口需要 Authorization 头，window.open 直接打开链接带不上 Token，怎么办？
**答**：
- 方案一：fetch 以 Blob 拉取文件再触发保存，可带任意 Header，适合中小文件，还能做进度条。
- 方案二：先向后端换一个一次性短时 ticket 拼在下载链接上，window.open / a 标签直接下载，适合大文件走 CDN。
- 服务端要下发 Content-Disposition: attachment，浏览器才会触发下载而不是内联预览。

```javascript
// 方案一：Blob 下载，可携带任意请求头
async function downloadWithAuth(url, filename) {
  const res = await fetch(url, {
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
  });
  if (!res.ok) throw new Error(`下载失败 ${res.status}`);
  const blob = await res.blob();
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = filename;                        // 指定保存文件名
  a.click();
  URL.revokeObjectURL(a.href);                  // 释放内存
}

// 方案二：一次性 ticket，适合大文件直链下载
async function downloadViaTicket(filePath) {
  const { ticket } = await api.getDownloadTicket(filePath); // 30 秒有效、用后作废
  window.open(`/api/download?path=${encodeURIComponent(filePath)}&ticket=${ticket}`);
}
```

## 八、主题与国际化
