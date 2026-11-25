---
title: [MP-345] 小程序文件上传：直传 OSS 与断点续传
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 面试题, 文件]
type: 面试题
---

## MP-345：小程序文件上传：直传 OSS 与断点续传

**答**：
- 直传链路：前端 wx.chooseMedia → 服务端签发 OSS 直传凭证（STS 临时凭证 + 签名）→ wx.uploadFile 直传 OSS（不走业务服务器带宽）→ 回调确认
- STS 安全：临时凭证（15min 过期 + 最小权限前缀）——「永久凭证下发」是安全事故
- 上传任务管理：wx.uploadFile 的 uploadTask（onProgressUpdate 进度 + abort 取消）——多文件并发队列（2~3 并发）+ 页面卸载取消
- 断点续传：小程序 uploadFile 不原生支持 Range 续传——大文件切片（文件分块 + 分块上传接口 + 合并）或依赖 OSS 分片 API（服务端编排）
- 深水点：上传失败的重试矩阵（网络切换重试/凭证过期重签/服务端 5xx 退避）+ 上传完成的「孤儿文件清理」（业务失败后 OSS 文件清理——生命周期对齐）

```javascript
async function uploadWithRetry(filePath, retries = 2) {
  const { credential } = await api.getUploadCredential();   // STS(15min, 最小权限)
  return new Promise((resolve, reject) => {
    const task = wx.uploadFile({
      url: credential.url, filePath, name: 'file',
      formData: { ...credential.fields },
      success: (r) => { api.confirmUpload(JSON.parse(r.data).key).then(resolve); },
      fail: (e) => { retries > 0 ? uploadWithRetry(filePath, retries - 1).then(resolve, reject) : reject(e); },
    });
    task.onProgressUpdate((p) => this.setData({ [`progress[${idx}]`]: p.progress }));   // 进度
    this._tasks.push(task);                        // 页面卸载 abort
  });
}
onUnload() { this._tasks.forEach((t) => t.abort()); }
```
