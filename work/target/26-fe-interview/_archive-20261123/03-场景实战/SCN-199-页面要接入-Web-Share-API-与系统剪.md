---
title: [SCN-199] 页面要接入 Web Share API 与系统剪贴板，权限被拒或能力缺失时如何兜底？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-199：页面要接入 Web Share API 与系统剪贴板，权限被拒或能力缺失时如何兜底？
**答**：
- 系统能力接入的统一姿势是"能力检测 → 请求权限 → 优雅降级"三层：能检测支持与否（`navigator.share` / `clipboard`）、能查权限状态（Permissions API）、每一层都有替代路径。
- 分享降级链：Web Share（含文件）→ 复制链接 + toast 提示 → 手动复制引导；桌面端没有 share sheet，直接走复制。
- 剪贴板写入的坑：非安全上下文（http）不可用、需用户手势触发、iOS Safari 需要在 promise 链内同步触达 DOM；复制富文本/图片各有 API 差异（ClipboardItem）。
- 权限被拒后的体验：明确告知"为什么需要 + 如何开启"（引导改设置），而不是静默失败让用户困惑。

```javascript
// 系统能力接入：能力检测 + 权限查询 + 逐层降级
export async function shareContent({ title, text, url, files }) {
  // 层 1：Web Share（支持文件分享）
  if (navigator.canShare?.({ files }) && files?.length) {
    try { await navigator.share({ files, title }); return { level: 'native-files' }; } catch (e) { if (e.name === 'AbortError') throw e; }
  }
  if (navigator.share) {
    try { await navigator.share({ title, text, url }); return { level: 'native' }; }
    catch (e) {
      if (e.name === 'AbortError') throw e;            // 用户主动取消不算失败
      report({ type: 'share-fallback', reason: e.name });
    }
  }
  // 层 2：复制链接 + 提示（桌面主路径）
  const copied = await copyToClipboard(url);
  if (copied) { toast('链接已复制，去粘贴给好友吧'); return { level: 'copy' }; }
  // 层 3：手动复制引导
  showManualCopyDialog(url);                           // 选中文本 + Ctrl C 教程
  return { level: 'manual' };
}

export async function copyToClipboard(text) {
  // 层 1：Async Clipboard API（安全上下文）
  if (navigator.clipboard && window.isSecureContext) {
    try { await navigator.clipboard.writeText(text); return true; }
    catch (e) {
      // 权限被拒：引导用户开权限，而不是静默降级
      if (e.name === 'NotAllowedError') { promptClipboardPermission(); return false; }
    }
  }
  // 层 2：execCommand 兜底（必须在用户手势同步链内）
  try {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.cssText = 'position:fixed;opacity:0';
    document.body.appendChild(ta);
    ta.select();
    const ok = document.execCommand('copy');           // 弃用但仍是最后的兜底
    ta.remove();
    return ok;
  } catch { return false; }
}

// 富文本/图片复制：ClipboardItem 按类型分发
export async function copyRichContent(node) {
  const html = node.innerHTML, blob = await domToPngBlob(node);
  await navigator.clipboard.write([
    new ClipboardItem({
      'text/html': new Blob([html], { type: 'text/html' }),
      'image/png': blob,
    }),
  ]);
}

// 权限状态查询 + 被拒引导
export async function checkClipboardPermission() {
  const st = await navigator.permissions.query({ name: 'clipboard-write' }).catch(() => null);
  return st?.state ?? 'prompt';                        // granted | prompt | denied
}
```
