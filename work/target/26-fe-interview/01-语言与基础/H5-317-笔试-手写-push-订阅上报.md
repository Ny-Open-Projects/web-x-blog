---
title: [H5-317] 笔试：手写 push 订阅上报
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 笔试题, PWA]
type: 笔试题
---

## H5-317：笔试：手写 push 订阅上报

**题目**：实现 `subscribePush()`：检查通知权限 → 未授权在用户点击后请求 → pushManager 订阅（VAPID 公钥）→ 把订阅 JSON 上报服务端；权限被拒时返回明确错误；支持取消订阅。

**答**：
```javascript
const VAPID_PUBLIC = urlBase64ToUint8Array('BHIE...key');

async function subscribePush() {
  if (!('PushManager' in window)) return { ok: false, error: '不支持推送' };
  const reg = await navigator.serviceWorker.ready;

  let perm = Notification.permission;
  if (perm === 'default') {
    perm = await Notification.requestPermission(); // 必须在用户手势链路里调用
  }
  if (perm !== 'granted') return { ok: false, error: '通知权限未授权' };

  const sub = await reg.pushManager.subscribe({
    userVisibleOnly: true,
    applicationServerKey: VAPID_PUBLIC,
  });
  await fetch('/api/push/subscribe', { method: 'POST', body: JSON.stringify(sub) });
  return { ok: true, endpoint: sub.endpoint };
}

async function unsubscribePush() {
  const reg = await navigator.serviceWorker.ready;
  const sub = await reg.pushManager.getSubscription();
  if (!sub) return;
  await fetch('/api/push/unsubscribe', { method: 'POST', body: sub.endpoint });
  await sub.unsubscribe();
}
function urlBase64ToUint8Array(b64) {
  const pad = '='.repeat((4 - (b64.length % 4)) % 4);
  const raw = atob((b64 + pad).replace(/-/g, '+').replace(/_/g, '/'));
  return Uint8Array.from([...raw].map(c => c.charCodeAt(0)));
}
```

**评分点**：
- VAPID 公钥的 base64url → Uint8Array 转换（直接传字符串会报错）——细节判分点
- requestPermission 必须用户手势内调用
- userVisibleOnly: true 不可省略
- 取消订阅要同时通知服务端删 endpoint
- 订阅对象直接序列化上报（含 endpoint + keys）
