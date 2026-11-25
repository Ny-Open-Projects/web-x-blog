---
title: [MFW-564] 元框架静态资产管线：font 优化与自托管
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-564：font 优化与自托管管线

**答**:
- next/font 的产物管线：1) **构建期子集化**（Google Fonts 构建时下载 → self-host——无第三方请求（GDPR/可用性）+ font-display 处理 RBL-720）；2) **CSS 自动生成**（@font-face + unicode-range 分片自动——浏览器按需拉字符分片）；3) **零布局偏移**（自动 size-adjust/metrics override——fallback 字体度量对齐：CLS 消除）。
- 构建期 vs 运行时下载：构建期下载字体（next/font/google）→ 字体成为构建产物（hash 进产物 RBL-598）——构建机器需要外网（离线构建的字体缓存）；运行时加载 Google CSS = 第三方依赖（隐私 + 不可控）。
- size-adjust 的原理：fallback 字体的 metrics 调整（ascent/descent 缩放对齐主字体——字宽一致 → 换字体时布局不跳）。
- 追问钩子：为什么「字体自托管 + metrics 对齐」能同时解决隐私与 CLS？——自托管消第三方请求（GDPR 合规 + 中国网络可用性——Google Fonts 在国内不稳定）；metrics override 让 fallback 与 webfont 宽度一致（swap 期间布局不跳——FOUT 的 CLS 归零）；两个问题的解法交汇在「构建期处理字体」：构建期拿到字体才能计算 metrics 对齐——构建期处理的价值 = 跨关切（合规/性能/体验）的统一解。

```javascript
// next/font 构建期管线
import { Inter } from 'next/font/google';
const inter = Inter({ subsets: ['latin'], display: 'swap' });
export default function RootLayout({ children }) {
  return <html className={inter.className}><body>{children}</body></html>;
}
// 产物：/_next/static/media/inter.woff2（hash 文件名）+ @font-face CSS（metrics 对齐）
// 自动生成（构建期）
// @font-face {
//   font-family: '__Inter_Fallback_abc';
//   src: local("Arial");
//   size-adjust: 107.64%;                                 ← 度量对齐：CLS=0
//   ascent-override: 90.44%; descent-override: 22.52%;
// }
// 本地字体（无需下载）
import localFont from 'next/font/local';
const myFont = localFont({ src: './MyFont.woff2', display: 'swap' });
```
