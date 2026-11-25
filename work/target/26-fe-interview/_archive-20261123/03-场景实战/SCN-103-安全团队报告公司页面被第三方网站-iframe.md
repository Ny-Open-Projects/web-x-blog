---
title: [SCN-103] 安全团队报告公司页面被第三方网站 iframe 嵌入做点击劫持，如何处置？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-103：安全团队报告公司页面被第三方网站 iframe 嵌入做点击劫持，如何处置？
**答**：
- 主修复在网关响应头：X-Frame-Options: DENY（老标准）+ CSP frame-ancestors 'none'（现代标准，两者都要加覆盖不同浏览器）；业务确需被信任方嵌入时用 frame-ancestors 白名单。
- JS 兜底检测（top !== self 时反嵌套或替换内容）只能作辅助——它可被 sandbox 属性绕过，不能替代响应头。
- 加头后用 curl 验证响应、用本地 HTML 嵌套测试验证生效，全站网关层统一加而不是各应用自己加。

```nginx
# 点击劫持修复：网关层统一加响应头，全站生效
server {
  location / {
    proxy_pass http://frontend;
    add_header X-Frame-Options "DENY" always;                 # 老标准：禁止任何 iframe
    add_header Content-Security-Policy "frame-ancestors 'none'" always;  # 现代标准
    # 若需允许集团内域名嵌入：
    # add_header Content-Security-Policy "frame-ancestors https://partner.example.com" always;
  }
}
```
