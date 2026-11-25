---
title: [MP-052] 剪贴板、扫一扫等常用 API 有哪些注意点？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-052：剪贴板、扫一扫等常用 API 有哪些注意点？
**答**：
- `wx.setClipboardData`：写入成功系统自带 toast，可用 `wx.hideToast` 覆盖自定义提示；`getClipboardData` 属于**隐私接口**，需声明隐私指引并可能触发弹窗。
- `wx.scanCode`：返回 result、scanType（QR_CODE/A-ZBAR 等）、charSet；`onlyFromCamera` 控制是否允许从相册识别。
- 这类开放 API 普遍要求：真实用户交互触发、类目与隐私声明匹配、真机验证（工具端行为可能不同）。

```javascript
// 复制券码并自定义提示
wx.setClipboardData({
  data: 'COUPON-2026-XXXX',
  success: () => {
    wx.hideToast()
    wx.showToast({ title: '券码已复制', icon: 'success' })
  }
})

// 扫码
wx.scanCode({
  onlyFromCamera: false,
  success: (res) => console.log(res.result, res.scanType, res.charSet)
})
```

---

## 八、审核与合规（053-057）
