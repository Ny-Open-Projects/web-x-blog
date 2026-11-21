---
title: [MFW-252] 流式响应的压缩与缓冲陷阱
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-252：流式压缩与缓冲陷阱

**答**:
- 陷阱一：CDN/代理缓冲整流（nginx 默认 proxy_buffering 攒齐才发——流式变阻塞，首字节延迟退化到全量渲染时间）——流式路由必须 proxy_buffering off / X-Accel-Buffering: no
- 陷阱二：gzip 等缓冲（压缩器要攒 window 才输出——小 flush 被 hold）——用支持流式压缩的层（Cloudflare 自动）或只压静态段
- 陷阱三：早 flush 的 HTML 不完整被爬虫截断（SEO 抓到半页）——关键 SEO 内容放首段（Shell 内同步出），交互段才后流
- 诊断：curl --no-buffer 逐 chunk 观察到达时间（TTFB 与末字节差 = 流式是否真的在流）

```nginx
# 流式路由反代配置
location /app/ {
  proxy_pass http://next;
  proxy_buffering off;                    # 关键：禁攒批
  proxy_set_header X-Accel-Buffering no;
}
# 诊断：curl -N https://site/app | ts  → chunk 间隔可见即真流式
```
