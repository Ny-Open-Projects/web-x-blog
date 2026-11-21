---
title: [PER-641] OAuth 前端接入的安全陷阱：state/PKCE 之外的隐蔽坑有哪些？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-641：OAuth 前端接入的安全陷阱：state/PKCE 之外的隐蔽坑有哪些？

**答**：
- state/PKCE 之外的坑：**redirect_uri 校验放宽**（后端允许子串匹配，攻击者注册 `https://app.com.evil.io` 绕过）、**fragment 泄漏**（隐式流的 token 在 URL fragment，会被 Referer/浏览器历史/第三方脚本读到）、**回调页第三方脚本**（回调页带着 code，若引入了广告统计脚本等于送出授权码）、**多标签竞争**（两个 Tab 同时走 OAuth，state 被覆盖导致错绑）、**登出不同步**（本地 session 清了，第三方会话还在，下次自动重登把账号换回攻击者预留的）。
- 排查方法：把 OAuth 全流程画成时序图逐环节问这一步谁可控"；重点审回调页的脚本清单与 URL 处理。
- 修复姿势：redirect_uri 精确匹配（后端职责但要前端提需求）、回调页零第三方脚本 + 立即 history.replaceState 清掉 code、state 存 sessionStorage 按 Tab 隔离、登出时调第三方 end_session_endpoint。
- 追问钩子：为什么 code 而不是 token 要放 URL？——code 一次一换且有后端交换，暴露面小；但回调页自身仍要最小化。

```javascript

const oauthPitfalls = {
  redirectUri: { pit: '后端子串匹配放宽', fix: '精确匹配白名单，前端提需求' },
  callback: { pit: '回调页带 code 却引入第三方脚本', fix: '回调页脚本零清单 + replaceState 清 URL',
    code: `history.replaceState(null, '', location.pathname)` },
  state: { pit: '多 Tab 覆盖 state 造成账号错绑', fix: 'sessionStorage 按 Tab 存储（每 Tab 独立）' },
  logout: { pit: '本地清了第三方 session 还在', fix: '调用 end_session_endpoint 联合登出' },
  flow: { pit: '隐式流 fragment token', fix: '迁移 authorization code + PKCE' },
  review: '时序图逐环节问这一步谁可控"；回调页是重点审区',
};
console.log(oauthPitfalls.callback.fix);
```
