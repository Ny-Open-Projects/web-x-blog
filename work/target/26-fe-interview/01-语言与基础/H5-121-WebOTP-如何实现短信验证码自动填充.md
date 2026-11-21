---
title: [H5-121] WebOTP 如何实现短信验证码自动填充？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-121：WebOTP 如何实现短信验证码自动填充？
**答**：
- 原理：短信按约定格式携带**域名绑定串**（`@your-domain #123456`），浏览器校验短信来源与页面域匹配后，把验证码直接递给页面。
- 前端调用：`navigator.credentials.get({ otp: { transport: ['sms'] }, signal })`，返回 `{ code }`；需在用户手势链路里发起（进入验证码页时）。
- 输入框标配 `autocomplete="one-time-code"`：iOS Safari 不支持 WebOTP JS 但支持该提示词，从键盘上方直接点填——两者同时部署覆盖双平台。
- AbortController 控制等待窗口：页面离开或倒计时结束 `controller.abort()`，避免悬挂的 get 请求。
- 限制：仅 Android Chrome 系完整支持、需 HTTPS、短信格式必须精确（域名+井号+验证码，末尾可加品牌名）。

```html
<!-- 双平台覆盖：one-time-code 提示词 + WebOTP JS -->
<input id="otp" name="otp" type="text" inputmode="numeric"
       pattern="\d{6}" maxlength="6"
       autocomplete="one-time-code" required>
<button>提交</button>

<script>
  const ac = new AbortController();

  // 1) WebOTP：Android Chrome 自动填充
  if ('OTPCredential' in window) {
    (async () => {
      try {
        const otp = await navigator.credentials.get({
          otp: { transport: ['sms'] },
          signal: ac.signal,
        });
        document.getElementById('otp').value = otp.code;   // 直接回填
        document.getElementById('otp').dispatchEvent(new Event('input')); // 触发自动提交
      } catch (err) {
        // AbortError：页面离开或超时；NotAllowedError：非手势调用
        if (err.name !== 'AbortError') console.warn('WebOTP 失败：', err);
      }
    })();
  }

  // 2) 离开页面时取消等待
  window.addEventListener('pagehide', () => ac.abort());
  // 验证码 60 秒失效同样取消
  setTimeout(() => ac.abort(), 60_000);

  // 3) 自动提交
  document.getElementById('otp').addEventListener('input', (e) => {
    if (e.target.value.length === 6) e.target.form?.requestSubmit();
  });
</script>
```

对应短信格式（服务端下发）：

```text
【示例商城】您的验证码为 123456。

@shop.example.com #123456
```
