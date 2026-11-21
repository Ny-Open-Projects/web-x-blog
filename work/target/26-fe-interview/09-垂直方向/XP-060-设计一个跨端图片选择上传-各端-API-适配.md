---
title: [XP-060] 设计一个跨端图片选择上传（各端 API 适配）？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-060：设计一个跨端图片选择上传（各端 API 适配）？
**答**：
- 适配面拆解：**选取**（相册/拍照/多选上限）、**压缩**（质量/尺寸策略）、**上传**（分片/直传 OSS/凭据）、**预览与删除**，四段各自定义接口。
- 各端差异：小程序 `wx.chooseMedia`+`wx.uploadFile`；H5 `input[type=file]`+Canvas 压缩+FormData/XHR；RN `launchImageLibrary`+原生压缩+ tus/multipart，统一收敛进 `IPicker/IUploader`。
- 大图方案：**服务端签发直传凭据**（STS），客户端直传对象存储，回调业务服务器——绕开业务服务器带宽；分片+断点续传（tus 协议）跨端一致。
- 质量策略：按用途定参（头像压 750px/0.8，长图限 1080），EXIF 方向校正（H5/RN 需处理，小程序端上传一般已带）。
- 失败治理：分片重试、弱网切换（WiFi→蜂窝确认）、上传取消与去重（文件 hash）。

```typescript
// packages/adapter/media —— 图片选择上传适配层
export interface PickResult { path: string; size: number; width: number; height: number }
export interface IPicker { pick(o: { count: number; source: 'album' | 'camera' }): Promise<PickResult[]> }
export interface IUploader { upload(path: string, onProgress: (p: number) => void): Promise<{ url: string }> }

// weapp：
// pick: (o) => wx.chooseMedia({ count: o.count, sourceType: [o.source] }).then(r =>
//   r.tempFiles.map((f) => ({ path: f.tempFilePath, size: f.size, ...imageInfo(f) })))
// upload: (path, onProgress) => new Promise((res, rej) => wx.uploadFile({
//   url, filePath: path, name: 'file', formData: { stsToken }, success: (r) => res(JSON.parse(r.data)),
// })) —— wx.uploadFile 自带 onProgressUpdate

// h5：input[type=file] → createImageBitmap + OffscreenCanvas 压缩（EXIF 用 createImageBitmap 的 imageOrientation:'from-image'）
//     → FormData + XHR.upload.onprogress；大文件走 tus-js-client 分片断点

// rn：TurboModule 桥 launchImageLibrary + 原生压缩（Luban/CGImageSource）+ 原生分片上传

// 通用编排（core）：
export async function pickAndUpload(picker: IPicker, uploader: IUploader, limit = 9) {
  const files = await picker.pick({ count: limit, source: 'album' });
  return Promise.all(files.map(async (f) => {
    const compressed = await compress(f.path, { maxEdge: 1080, quality: 0.8 }); // adapter 提供
    return uploader.upload(compressed, renderProgress);
  }));
}
// 直传安全：STS 临时凭据由服务端签发（15 分钟过期），客户端永不持有长期密钥
```
