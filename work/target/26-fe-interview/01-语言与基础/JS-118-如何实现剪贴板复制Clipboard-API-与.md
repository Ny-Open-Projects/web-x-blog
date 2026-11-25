---
title: [JS-118] 如何实现剪贴板复制？Clipboard API 与 execCommand 如何降级？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-118：如何实现剪贴板复制？Clipboard API 与 execCommand 如何降级？

**答**：
- 优先 `navigator.clipboard.writeText`：异步、无 DOM 污染，但要求安全上下文（HTTPS/localhost）且页面获得焦点。
- 降级方案：临时 textarea + `document.execCommand('copy')`，API 已废弃但兼容性最广。
- 降级细节：textarea 必须存在、不可见、有选中内容；调用前同步选区，调用后立即清理。
- 读取剪贴板（readText）需要用户授权，失败要按 NotAllowedError 分类提示。

```javascript
async function copyText(text) {
  // 1. 现代 API
  if (navigator.clipboard && window.isSecureContext) {
    try {
      await navigator.clipboard.writeText(text);
      return true;
    } catch { /* 权限拒绝或环境限制 → 降级 */ }
  }
  // 2. 降级：execCommand
  const ta = document.createElement('textarea');
  ta.value = text;
  ta.setAttribute('readonly', '');
  ta.style.cssText = 'position:fixed;top:0;left:0;opacity:0;pointer-events:none';
  document.body.appendChild(ta);
  ta.select();
  ta.setSelectionRange(0, text.length); // iOS Safari 需要
  let ok = false;
  try {
    ok = document.execCommand('copy'); // 同步执行，返回是否成功
  } catch { ok = false; }
  ta.remove();
  return ok;
}

copyText('hello clipboard').then((ok) => console.log(ok ? '已复制' : '复制失败'));

// 读取剪贴板（需要用户手势与授权）
async function pasteFromClipboard() {
  try {
    return await navigator.clipboard.readText();
  } catch (e) {
    if (e.name === 'NotAllowedError') console.log('用户拒绝了授权');
    return null;
  }
}
```

**追问**：

1. HTTP 页面下 `navigator.clipboard` 一定不可用吗？ → 是，非安全上下文里它是 undefined（localhost 除外），只能直接走 execCommand 分支，所以判断要同时看 `window.isSecureContext`。
2. `execCommand('copy')` 返回 true 就一定写进剪贴板了吗？ → 不一定，它只表示命令被接受；部分浏览器和输入法会静默失败，仍要让用户确认或提供手动复制入口。
3. 复制多行文本或超长文本有什么坑？ → iOS 会折叠连续空白和换行，必须用 textarea 的 value 赋值而非 innerHTML；超长内容还要考虑主线程阻塞，必要时分片或提示。
