---
title: [WEB-321] JWT 一旦签发无法撤销，怎么实现"主动踢人下线"？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 笔试题
---

## WEB-321：JWT 一旦签发无法撤销，怎么实现"主动踢人下线"？
**答**：
- 无状态与可撤销天然矛盾：要么引入状态（黑名单/版本号），要么缩短生命周期。
- 常用方案：短效 access（5-15min）+ refresh 换发；登出/封禁时把 refresh 失效或把用户 tokenVersion+1，验签时比对。
- 极端安全（支付后台）：网关维护 jti 黑名单（Redis，TTL=剩余有效期），踢人即时生效，代价是引入了查库。

```javascript
function verify(token, store) {
  const { sub, jti, exp, ver } = decode(token);
  if (Date.now() > exp * 1000) return 401;
  if (store.banned(jti)) return 401;              // 单 token 黑名单
  if (ver !== store.userVersion(sub)) return 401; // 用户级"全体下线"
  return 200;
}
// 改密码 → userVersion++ → 所有旧 token 全部失效
console.log('短效 token + 版本号 = 无状态与可撤销的折中');
```

**评分点**：
- 结论先行，能一句话说清核心机制
- 要点覆盖主流程与关键分支（异常/并发/边界）
- 代码可运行且体现安全或性能意识
- 能主动说出"工程上怎么选"与常见坑
