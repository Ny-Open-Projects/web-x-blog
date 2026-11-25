---
title: [WEB-440] 点击劫持是什么，X-Frame-Options 与 frame-ancestors
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-440：点击劫持是什么，X-Frame-Options 与 frame-ancestors

**答**：
- 原理：攻击者把你的页面放进透明 iframe 叠在诱导页上，用户点「领奖」实际点到「转账」按钮
- 防御一：`X-Frame-Options: DENY / SAMEORIGIN`，老标准，只支持三个值
- 防御二：CSP 的 `frame-ancestors 'none'`（或白名单），功能超集，优先用它，X-Frame-Options 兜底老浏览器
- JS 兜底：`if (top !== self) top.location = self.location`（可能被 sandbox 拦，只能作辅助）
- 判断标准：凡是有「一键执行资金/权限操作」的页面（管理后台、支付页）必须禁嵌；纯展示页可放宽

```nginx
add_header Content-Security-Policy "frame-ancestors 'none'" always;
add_header X-Frame-Options "DENY" always;
```
