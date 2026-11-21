---
title: [MP-134] iOS 与 Android 的小程序差异坑有哪些（清单）？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-134：iOS 与 Android 的小程序差异坑有哪些（清单）？
**答**：
- **字体/单位**：iOS 不支持部分粗体字重、rpx 在不同 DPR 的取整差异导致 1px 边框消失（用 transform: scale 或 border 伪元素方案）。
- **输入**：iOS 软键盘弹起顶起页面（position: fixed 元素错位），`adjust-position` 处理；iOS 输入中文联想时 value 与显示不一致（用 bindinput 节流 + composition 事件思路）。
- **时间**：`new Date('2024-01-01')` iOS 必须要 `2024/01/01` 格式（'-' 解析失败返回 Invalid Date）。
- **音频自动播放/音量**、**滚动回弹**、**同层渲染表现**、**localStorage 上限**等均有差异，需真机矩阵验证。
- 规避原则：日期统一用时间戳或手动替换格式；关键交互两端都写回归用例。

```javascript
// 跨端兼容工具集
const compat = {
  parseDate(str) {                      // iOS new Date('2024-01-01') 是 Invalid Date
    if (typeof str === 'string') str = str.replace(/-/g, '/')
    return new Date(str)
  },
  safeAreaPadding() {                   // iPhone 底部安全区
    const { screenHeight, safeArea } = wx.getSystemInfoSync()
    return safeArea ? { paddingBottom: screenHeight - safeArea.bottom + 'px' } : { paddingBottom: 0 }
  },
  isIOS() { return /iOS/i.test(wx.getSystemInfoSync().system) },
  keyboardAvoid() {                     // 输入聚焦时页面顶起处理
    if (this.isIOS()) this.setData({ kbOffset: -260 })
  }
}
```
