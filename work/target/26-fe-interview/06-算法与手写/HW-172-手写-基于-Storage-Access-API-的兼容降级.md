---
title: [HW-172] 手写第三方 Cookie 降级——Storage Access API 请求访问 + 分区存储语义说明与功能降级链
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---
## HW-172：手写第三方 Cookie 降级——Storage Access API 请求访问 + 分区存储语义说明与功能降级链
**答**：三方 Cookie 退场（PER-196）下的嵌入场景降级：iframe 内需要用户身份（客服插件识别用户）→ Storage Access API（document.requestStorageAccess——用户手势内请求，浏览器弹授权）→ 拒绝/不支持则功能降级（匿名客服会话 + 提示登录）。

```javascript
async function ensureEmbedIdentity() {
  // 场景：自家域名 iframe 嵌在合作伙伴站点，需要读自家 cookie 识别用户
  if (document.hasStorageAccess?.() ? await document.hasStorageAccess() : true) {
    return readUserIdFromCookie();                       // 已有访问权（首次直接加载场景）
  }
  if (typeof document.requestStorageAccess === 'function') {
    try {
      await document.requestStorageAccess();             // 必须在用户手势内调用（点击"客服"按钮）
      if (await document.hasStorageAccess()) return readUserIdFromCookie();
    } catch { /* 用户拒绝或站点无 top-level 交互记录 */ }
  }
  // 降级链：匿名会话（功能保留核心：能聊天，丢失个性化"您上次咨询过"）
  return { anonymous: true, sessionId: crypto.randomUUID?.() ?? String(Math.random()) };
}
// 按钮触发（用户手势内）：customerServiceBtn.onclick = () => ensureEmbedIdentity().then(startChat);
// 语义：
// hasStorageAccess —— 当前帧是否已有第一方存储访问权
// requestStorageAccess —— 请求解锁（浏览器可能弹权限提示；需站点间可信交互历史）
// 降级链：有权限 → 请求成功 → 匿名会话 —— 每级保留核心功能、降级个性化
```

**评分点**：
- hasStorageAccess/requestStorageAccess 的使用与用户手势约束——本题核心。
- 降级链保留核心功能（匿名客服会话）丢失个性化。
- 与三方 Cookie 退场（PER-196）的背景关联。
- 请求被拒的 UX 兜底（提示登录而非报错）。
