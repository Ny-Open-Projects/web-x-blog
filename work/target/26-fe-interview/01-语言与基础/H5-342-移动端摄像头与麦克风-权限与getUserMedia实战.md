---
title: [H5-342] 移动端摄像头与麦克风：权限与 getUserMedia 实战
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 设备能力]
type: 面试题
---

## H5-342：移动端摄像头与麦克风：权限与 getUserMedia 实战

**答**：
- 权限三层：浏览器权限（Notification/Permission API 查询）、系统权限（被用户在系统设置拒绝后 getUserMedia 直接 NotAllowedError）、App 内还要 WebView 授权（onPermissionRequest 需原生实现）
- 设备选择：enumerateDevices 列出前后摄像头，facingMode: 'user'/'environment' 约束；App 内常见「iframe 里调摄像头失败」——WebView 权限没透传或跨域 iframe 权限策略
- 失败分级处理：NotAllowedError（引导开权限）、NotFoundError（无设备）、NotReadableError（被占用，如原生相机在用）、约束失败 OverconstrainedError（降级约束重试）
- 资源管理：stream.getTracks().forEach(t => t.stop()) 在页面隐藏/组件卸载时释放——摄像头指示灯常亮是线上事故级 bug
- iOS 特有：需要 HTTPS（所有浏览器强制）、video 元素必须 playsinline 否则全屏接管预览

```javascript
async function openCamera() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({
      video: { facingMode: 'environment', width: { ideal: 1280 } }, audio: false,
    });
    video.srcObject = stream; video.play();
    return stream;
  } catch (e) {
    if (e.name === 'NotAllowedError') guideToSettings();
    else if (e.name === 'OverconstrainedError')
      return navigator.mediaDevices.getUserMedia({ video: true }); // 降级约束
    throw e;
  }
}
document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'hidden') currentStream?.getTracks().forEach(t => t.stop());
});
```

## 追问（补充）

**追问**：

1. iframe 里调 getUserMedia 为什么常失败？ → 父页面需给 iframe 加 `allow="camera; microphone"` 做权限策略透传，App 内 WebView 还要原生实现 onPermissionRequest 授权。
2. 系统层拒绝后查询浏览器权限还有意义吗？ → 有意义，Permission API 返回 'denied' 可区分永久拒绝，据此决定是引导去系统设置还是允许重新弹窗申请。
3. iOS 上有哪两个必踩的坑？ → 必须 HTTPS 安全上下文；video 必须加 `playsinline` 否则被系统全屏接管，且 getUserMedia 需用户手势触发。
