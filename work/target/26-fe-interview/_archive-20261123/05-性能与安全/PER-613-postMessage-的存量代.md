---
title: [PER-613] postMessage 的存量代码大量使用 targetOrigin 为星号，如何在不破坏业务的前提下收敛？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-613：postMessage 的存量代码大量使用 targetOrigin 为星号，如何在不破坏业务的前提下收敛？

**答**：
- 收敛策略是先观测后收紧三步：第一步**观测**——升级接收端做 origin 日志（收到消息时记录 event.origin），线上跑两周拿到真实来源分布；第二步**收紧接收端**——接收端 origin 白名单先行（发送端 '*' 先不动，接收端校验能挡住伪造）；第三步**收紧发送端**——按观测数据把 '*' 替换为精确 origin，对未知来源的接收方（第三方嵌入）提供配置协商。
- 不破坏业务的兜底：白名单外消息不丢弃而是记录 + 放行开关"（灰度期），开关关闭后仅记录；对确实无法确定 origin 的合法场景（如 sandbox iframe 是 null origin），用消息内容签名替代 origin 校验。
- 验证手段：自动化消息契约测试——枚举所有 postMessage 对，断言 targetOrigin != '*'；上线前跑契约回归。
- 灰度节奏：接收端校验 -> 报警观察 -> 强制丢弃 -> 发送端收紧，每步独立发布可回滚。

```javascript

// 第一步：观测型接收端（可灰度回滚）
const KNOWN = ['https://app.example.com', 'https://embed.partner.com'];
window.addEventListener('message', (e) => {
  const ok = KNOWN.includes(e.origin);
  log({ origin: e.origin, ok, data: typeof e.data });       // 全量记录来源
  if (!ok && STRICT_MODE) return;                            // 第三步后开启强校验
  handle(e.data);
});
// 第二步：契约测试断言无 '*'
// test('no wildcard targetOrigin', () => {
//   const hits = grepSource(/postMessage\([^,]+,\s*['"`]\*['"`]/);
//   expect(hits).toEqual([]);
// });
// 观测两周 -> 接收端白名单 -> STRICT_MODE 灰度 -> 发送端逐个替换 '*'
```
