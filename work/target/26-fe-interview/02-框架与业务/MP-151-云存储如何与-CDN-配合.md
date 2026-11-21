---
title: [MP-151] 云存储如何与 CDN 配合？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-151：云存储如何与 CDN 配合？
**答**：
- 云存储天然有 CDN 加速域名；大文件（视频/音频）上传用 `wx.cloud.uploadFile` 走直传，避免经业务服务器中转。
- 访问策略：`fileID` 临时链接（`getTempFileURL`）适合私有文件；公开静态资源直接用云存储的 CDN 域名 + 缓存头。
- 图片处理：云存储支持图片处理参数（缩放/裁剪/格式转换），配合 `lazy-load` 与按尺寸取图降内存。
- 生命周期：垃圾文件定期清理（临时上传/未引用附件），云存储容量也是成本项。

```javascript
// 上传直传 + 按尺寸取图 + 临时链接
Page({
  async upload(filePath) {
    const { fileID } = await wx.cloud.uploadFile({
      cloudPath: `ugc/${Date.now()}-${Math.random().toString(36).slice(2)}.jpg`,
      filePath
    })
    return fileID
  },
  thumb(fileID) { return `${fileID}?imageView2/1/w/300/h/300` }  // 云存储图片处理参数
})
// 私有文件：云函数签发临时链接
exports.getPrivate = async ({ fileID }) => {
  const r = await cloud.getTempFileURL({ fileList: [fileID] })
  return r.fileList[0].tempFileURL   // 带 expireTime 的临时 CDN 地址
}
```
