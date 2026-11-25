---
title: [WEB-571] 笔试：手写 0-RTT 安全请求守卫（客户端 nonce 方案）
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, 安全]
type: 笔试题
---

## WEB-571：笔试：手写 0-RTT 安全请求守卫（客户端 nonce 方案）

**答**：实现 `secureRequest(url, body)`：① 为每个写请求生成唯一 nonce + 时间戳并注入请求体；② 响应 425 时自动等待 1.5s 后重发一次（此时已完成握手，不再有重放窗口）；③ 425 重发最多 1 次；④ 请求体是 FormData 时不可注入，改为注入自定义头。写出实现并说明服务端如何配合校验。

```javascript
const crypto = window.crypto;

async function secureRequest(url, body) {
  const inject = (b) => {
    if (b instanceof FormData) return null; // 无法注入 JSON 字段
    const parsed = b ? { ...b } : {};
    parsed.__guard = { nonce: crypto.randomUUID(), ts: Date.now() };
    return parsed;
  };
  const once = async (b) => {
    const guard = inject(b);
    return fetch(url, {
      method: 'POST',
      headers: guard ? undefined : { 'x-nonce': crypto.randomUUID(), 'x-ts': String(Date.now()) },
      body: guard ? JSON.stringify(guard) : b,
    });
  };
  let res = await once(body);
  if (res.status === 425) {                       // Too Early: 握手完成后重试
    await new Promise(r => setTimeout(r, 1500));
    res = await once(body);
  }
  if (!res.ok) throw new Error(`request failed: ${res.status}`);
  return res.json();
}
// 服务端: 校验 ts 与服务器时间偏差 < 30s; nonce 写入 Redis SETNX TTL=60s,
// 重复 nonce → 409; FormData 场景从 x-nonce/x-ts 头校验
```

**评分点**：
- nonce 用强随机（crypto.randomUUID 而非 Math.random）
- 425 重试等待语义正确：等握手完成再发，而不是立刻重试
- 重试上限 1 次，防止死循环；FormData 走头注入的边界处理
- 能说明服务端校验双要素：时间窗 + nonce 去重表
