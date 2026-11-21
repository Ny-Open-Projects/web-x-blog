---
title: [HW-174] 手写 Web Share 分享——canShare 能力检测与多级降级（系统分享→复制链接→手动提示）
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：分享能力三级降级：navigator.share（系统原生分享面板，移动端体验最佳）→ navigator.clipboard.writeText 复制（桌面常用）→ 手动选择文案提示（最老环境）。canShare 先探测（带文件的分享移动端支持差异大）。

```javascript
async function shareContent({ title, text, url, files } = {}) {
  // 层 1：系统分享（支持文件时先 canShare 探测）
  if (navigator.canShare?.({ files }) && navigator.share) {
    try { await navigator.share({ title, text, url, ...(files && { files }) }); return 'native'; }
    catch (e) { if (e.name === 'AbortError') return 'cancelled'; }   // 用户关闭面板：静默
  }
  // 层 2：复制到剪贴板（HTTPS/localhost 约束）
  if (navigator.clipboard?.writeText) {
    try { await navigator.clipboard.writeText(url ?? text); toast('链接已复制'); return 'clipboard'; }
    catch { /* 剪贴板权限拒绝：降级层 3 */ }
  }
  // 层 3：手动提示（传统 execCommand 兜底或展示输入框）
  const input = prompt('请复制链接', url ?? text);
  return input != null ? 'manual' : 'skipped';
}
// 分享按钮（必须用户手势内调用——share/clipboard 都有手势要求）
// 降级语义：每级保留"分享完成"的核心目标，体验递减（原生面板 > 复制 > 手动）
// canShare({files}) 的价值：图片分享在部分安卓 WebView 不支持，硬调 share 会抛错——先探测再调用
```

**评分点**：
- 三级降级链（native share → clipboard → manual）每级语义。
- canShare 带参探测（文件分享的能力差异）。
- 用户手势约束与 AbortError（用户取消）静默处理。
- 剪贴板的安全上下文约束（HTTPS）意识。
