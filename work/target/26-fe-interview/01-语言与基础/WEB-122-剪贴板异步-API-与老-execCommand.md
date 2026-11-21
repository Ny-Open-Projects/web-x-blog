---
title: [WEB-122] 剪贴板异步 API 与老 execCommand 差在哪？权限如何处理？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-122：剪贴板异步 API 与老 execCommand 差在哪？权限如何处理？
**答**：
- `navigator.clipboard` 是异步 Promise API，支持文本与自定义格式（ClipboardItem 可写图片），是替代 execCommand('copy') 的标准方案。
- 前置条件：仅安全上下文（HTTPS/localhost）、写入通常需用户手势，readText 额外要权限授予且浏览器会弹授权条。
- 粘贴事件侧：paste 事件里 `e.clipboardData` 可拦截处理富文本，二者配合覆盖绝大多数需求。
- execCommand 已废弃但兼容老浏览器，作为 fallback 保留。

```javascript
async function copyCode(text) {
  try {
    await navigator.clipboard.writeText(text);          // 标准路径：HTTPS + 用户手势
  } catch {
    // fallback：隐藏 textarea + execCommand（老浏览器）
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    ta.remove();
  }
}
button.addEventListener('click', () => copyCode(code)); // 必须挂在用户手势上

// 读取剪贴板：需权限授权
navigator.clipboard.readText().then((t) => console.log('剪贴板内容', t));
```
