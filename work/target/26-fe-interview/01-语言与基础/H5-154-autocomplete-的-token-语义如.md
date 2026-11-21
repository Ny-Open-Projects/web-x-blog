---
title: [H5-154] autocomplete 的 token 语义如何指导表单自动填充？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-154：autocomplete 的 token 语义如何指导表单自动填充？
**答**：
- `autocomplete` 是受控词表（HTML 标准 autofill 章节）：`email/name/tel/street-address/cc-number/one-time-code` 等，浏览器据此匹配密码库、联系人、短信验证码——**写错 token 等于关闭自动填充**。
- token 支持组合：`shipping postal-code`、`billing cc-exp` 控制"归属区域"；`section-` 前缀区分多组同义字段。
- 密码管理器锚点：`username` + `current-password`（登录）vs `new-password`（注册，触发"生成强密码"并阻止误填旧密码）。
- 高频考点：短信验证码框用 `autocomplete="one-time-code"` + `inputmode="numeric"`，iOS 键盘才会弹出"来自短信"的建议。

```html
<!-- autocomplete token 决定浏览器能否自动填充 —— 写错就失去免输能力 -->
<form autocomplete="on">
  <!-- 基础字段：token 是受控词表，拼错 = 浏览器按 off 处理 -->
  <input name="email" type="email" autocomplete="email">
  <input name="name" type="text" autocomplete="name">
  <input name="tel" type="tel" autocomplete="tel">

  <!-- 结账地址：token 组合控制归属 -->
  <input name="addr1" autocomplete="shipping street-address">
  <input name="city" autocomplete="shipping address-level2">
  <input name="zip" autocomplete="shipping postal-code">

  <!-- 登录/注册：密码管理器的锚点 -->
  <input name="u" autocomplete="username">
  <input name="p" type="password" autocomplete="current-password">
  <!-- 注册页新密码用 new-password：阻止误填旧密码，并触发"生成强密码" -->

  <!-- 短信验证码：one-time-code 让 iOS 键盘弹出"来自短信"建议 -->
  <input name="otp" inputmode="numeric" autocomplete="one-time-code">

  <!-- 支付卡（真实场景一般在 iframe 内托管） -->
  <input name="cc" autocomplete="cc-number">

  <!-- 该关的时候显式关闭：避免密码管理器误填敏感框 -->
  <input name="secret" type="password" autocomplete="off">
</form>
<script>
// 面试要点：
// 1) type 与 autocomplete 协同：email/tel/url 提供"类型键盘"，token 提供"填充来源"
// 2) token 组合格式：section-x modifier 限定词（如 shipping postal-code）
// 3) one-time-code 前置条件：验证码短信在同一设备收到才可自动填充
// 4) name 属性与 token 一致性是密码管理器识别页面的辅助信号
// 5) autocomplete="off" 在密码框上常被浏览器忽略 —— 用 new-password 才能真正控制
</script>
```
