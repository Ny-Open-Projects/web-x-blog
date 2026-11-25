---
title: [WCN-934] 设计稿到代码的 token 像素对齐：rem / dp / pt 单位换算跨端一致怎么做
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-934：设计稿到代码的 token 像素对齐：rem / dp / pt 单位换算跨端一致怎么做

**答**：
- 结论先行：设计稿给的是 px 视觉值，跨端一致靠「编译期单位换算 + 基准统一」——token 存无单位数值，各端按基准换算，避免端上各自硬编码。
- 换算基准：Web 用 root font-size（如 16px 基准，1rem=16px，或 375 设计稿用 vw 方案）；Android 用 dp、iOS 用 pt；小程序用 rpx（750 设计稿基准）。
- 关键坑：1px 描边/分割线不能跟随缩放（否则高分屏变糊），要单独标记为 hairline token，固定设备物理像素。
- 字体与间距分离：字体大小用可缩放单位，间距可适度缩放，但最小点击区域（44pt/48dp）需遵守平台规范，不能纯按比例缩放。
- 追问钩子：面试官问「大字体模式怎么办」——答：token 提供缩放因子，Web 用 rem + 媒体查询、原生端用动态 type size 覆盖，保证可访问性。

```javascript
// 统一数值 token → 各端单位编译
const spacing = { s1: 4, s2: 8, s4: 16, s8: 32 };
const BASE = 16; // Web root font-size
function compileUnit(value, platform) {
  switch (platform) {
    case 'web':    return `${(value / BASE).toFixed(3)}rem`;
    case 'android':return `${value}dp`;
    case 'ios':    return `${value}pt`;
    case 'mini':   return `${value * 2}rpx`; // 375 设计稿 → 750rpx
    default:       return `${value}px`;
  }
}
['web', 'android', 'ios', 'mini'].forEach(p =>
  console.log(p, compileUnit(spacing.s4, p)));
// web 1.000rem / android 16dp / ios 16pt / mini 32rpx
```
