---
title: [SCN-475] 笔试题——实现 SSO 静默续期（iframe 刷新/失败降级/登出广播）？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-475：手写 SSO 静默续期：token 过期前 iframe 静默刷新、失败降级重登、登出广播

**需求与边界**：
- 输入：token（含过期时间）、认证中心；输出：无感续期。
- 边界要求：① 过期前主动续（剩余 20% 时触发——非过期后才刷）；② iframe 静默刷新（不跳转不闪烁）；③ 刷新失败（第三方 cookie 被禁）→ 降级重登引导；④ 单点登出广播（认证中心登出→全系统同步）。

**答**：
```javascript
class SsoSession {
  constructor({ token, authCenter }) {
    this.token = token; this.authCenter = authCenter;
    this.scheduleRenew();
    bc.onmessage = (e) => e.type === 'logout' && this.logout();
  }
  scheduleRenew() {                            // 剩余 20% 时触发
    const remain = this.token.exp - Date.now();
    setTimeout(() => this.renew(), remain * 0.8);
  }
  async renew() {
    try {
      const iframe = hiddenIframe(`${this.authCenter}/renew?clientId=xx`);
      const newToken = await waitForMessage(iframe);  // postMessage 回传
      this.token = newToken;
      this.scheduleRenew();                    // 递归下次续期
    } catch (e) {
      // 第三方 cookie 禁用等失败 → 降级：提示重新登录
      toast('登录即将过期，请重新登录');
      redirectLogin({ returnTo: currentPath }); // 回跳不丢页面
    }
  }
  logout() { clearLocal(); redirectLogin(); }  // 单点登出广播
}
// bc：认证中心登出 → 各子系统 tab 收到广播 → 全部登出
// （SCN-446 BroadcastChannel 复用）。
// token 存内存+sessionStorage（不进 URL/localStorage）。
```

**评分点**:
- 剩余 20% 提前续期（非过期后才刷——无感关键）。
- iframe 静默刷新+postMessage 回传（无跳转闪烁）。
- 失败降级（cookie 禁用→引导重登+returnTo 回跳）。
- 单点登出广播（BC 全 tab 同步）+token 存储安全。
